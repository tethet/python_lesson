# -*- coding: utf-8 -*-
import sqlite3
import datetime

conn = sqlite3.connect('task.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY,
              task_name TEXT,
              task_description TEXT,
              notification_time DATETIME,
              task_time TEXT,
              notification_sent BOOLEAN)''')


def add_task():
    task_name = input('タスクのタイトルを入力してください: ')
    task_description = input('タスクの内容を入力してください: ')
    task_time = input('タスクを行う日時を入力してください（yyyy-mm-dd HH:MM形式）: ')
    notification_time = datetime.datetime.strptime(task_time, '%Y-%m-%d %H:%M')

   c.execute('''INSERT INTO tasks (task_name, task_description, task_time, notification_time, notification_sent)
                  VALUES (?, ?, ?, ?, ?)''', (task_name, task_description, task_time, notification_time, False))
   conn.commit()

print('タスクが追加されました。')

def view_tasks():
    c.execute('''SELECT * FROM tasks''')
    all_tasks = c.fetchall()
    if not all_tasks:
        print('タスクはありません。')
    else:
        for task in all_tasks:
        print('ID: ', task[0])
        print('タスク名: ', task[1])
        print('タスクの内容: ', task[2])
        print('タスクを行う日時: ', task[3])
        print('通知の送信時間: ', task[4])
        print('通知の送信状況: ', task[5])
        print('\n')

def edit_task():
    task_id = input('編集するタスクのIDを入力してください: ')

    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = c.fetchone()

    if not task:
       print('指定したIDのタスクが見つかりませんでした')
       return