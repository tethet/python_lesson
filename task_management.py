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
              task_time TEXT)''')