import sqlite3
import datetime

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              published_date TEXT,
              date_added TEXT,
              read INTEGER)''')
def add_book():
    title = input('タイトルを入力してください: ')
    author = input('著者名を入力してください: ')
    published_date = input('出版日を入力してください（yyyy-mm-dd形式）: ')
    date_added = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    read = 0

    c.execute('''INSERT INTO books (title, author, published_date, date_added, read)
                  VALUES (?, ?, ?, ?, ?)''', (title, author, published_date, date_added, read))
    conn.commit()
    print('本が追加されました。')

def view_books():
    c.execute('''SELECT * FROM books''')
    all_books = c.fetchall()
    if not all_books:
        print('本が登録されていません。')
    else:
        for book in all_books:
            print('ID: ', book[0])
            print('タイトル: ', book[1])
            print('著者: ', book[2])
            print('出版日: ', book[3])
            print('登録日: ', book[4])
            print('読了状況: ', book[5])
            print('\n')

while True:
    print('1. 本を追加する')
    print('2. 全ての本を表示する')
    print('3. 本を検索する')
    print('4. 本を読了済みにする')
    print('5. 本を削除する')
    print('6. 終了')

    choice = input('選択してください: ')

    if choice == '1':
     add_book()
    elif choice == '2':
     view_books()
    elif choice == '3':
     search_book()
    elif choice == '4':
     mark_as_read()
    elif choice == '5':
     delete_book()
    elif choice == '6':
        break
    else:
     print('選択肢に含まれていない数字が入力されました。もう一度やり直してください。')
conn.commit()
conn.close()
