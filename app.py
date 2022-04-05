from datetime import datetime
import sqlite3

from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def main():
    """Получает посты из таблицы. """

    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    cur.execute("SELECT * FROM posts;")

    posts = cur.fetchall()
    print(posts)

    connection.close()

    return {
        'posts': posts
    }


@app.get('/add')
def create_posts():
    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    title = request.args.get('title')
    description = request.args.get('description')
    date = datetime.now().strftime('%d-%m-%y %H:%M')

    if title and description:
        cur.execute(f"INSERT INTO posts (title, description, date) VALUES('{title}', '{description}', '{date}')")
        connection.commit()

    connection.close()

    return redirect('/')


@app.route('/edit')
def edit():
    return 'Изменение поста'


@app.route('/delete')
def delete_post():
    connection = sqlite3.connect('blog.sqlite')
    cur = connection.cursor()

    id = int(request.args.get('id'))

    cur.execute(f"DELETE FROM posts WHERE ID={id};")
    connection.commit()

    connection.close()

    return redirect('/')


