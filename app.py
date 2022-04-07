from datetime import datetime
import sqlite3

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Создание базы данных происходит в файле database.py


@app.route('/')
def main():
    """
     Вывод всех постов пользователю.

      Работа функци:
       1. Подключается к базе данных.
       2. Получает все записи из таблицы.
       3. Передаёт записи в теплейт.
    """

    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    cur.execute("SELECT * FROM posts;")

    posts = cur.fetchall()
    print(posts)

    connection.close()

    return render_template('post_all.html', posts=posts)


@app.get('/add')
def create_posts():
    """
    Добавление новых постов.

    Работа функции:
     1. Соединяется с базой данных.
     2. Получает заголовок и описание из параметров адр. строки.
     3. Получает дату из системы.
     4. Если есть И заголовок, И описание:
        Создаёт запрос INSERT, в которые подставляет заголовок, описание и дату.
     5.Редиректит на главную страницу.

    """
    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    title = request.args.get('title')
    description = request.args.get('description')
    date = datetime.now().strftime('%d-%m-%y %H:%M')

    if title and description:
        cur.execute("INSERT INTO posts (title, description, date) VALUES(?, ?, ?);", (title, description, date))
        connection.commit()

    connection.close()

    return redirect('/')


@app.route('/edit')
def edit():
    """
    Изменение постов.

    Работа функции:
      1. Подкючается к базе.
      2. Из параметров адр. строки получает id, заголовок и описание.
      3. Формирует запрос к базе.
       3.1. Если есть И id, И заголовок, И описание:
           Изменяет заголовок И описание.
       3.2. Если есть id и заголовок:
            Изменяет ТОЛЬКО заголовок.
       3.3. Если есть id и описание:
            Изменяет ТОЛЬКО описание.
       3.4. В ином случае: ничего не делает.
      4. Редирект на главную страницу.
    """
    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    id_post = request.args.get('id')
    title = request.args.get('title')
    description = request.args.get('description')

    if id_post and title and description:
        cur.execute("UPDATE posts SET title= ?, description = ? WHERE id = ?;", (title, description, id_post))
        connection.commit()
    elif id_post and title:
        cur.execute("UPDATE posts SET title= ? WHERE id = ?;", (title, id_post))
        connection.commit()
    elif id_post and description:
        cur.execute("UPDATE posts SET description= ? WHERE id = ?;", (description, id_post))
        connection.commit()
    connection.close()
    return redirect('/')


@app.route('/delete')
def delete_post():
    """
    Удаление постов.

    Работа функции:
     1. Подключается к базе.
     2. Получает id из адресной строки.
     3. Если id есть, удаляет нужный пост.
     4. Редирект на главную страницу.
    """
    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    id_post = request.args.get('id')
    if id_post:
        cur.execute("DELETE FROM posts WHERE id=?;", (id_post,))
        connection.commit()
    connection.close()

    return redirect('/')
