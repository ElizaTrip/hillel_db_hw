from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)


@app.route('/')
def main():
    return 'Вывод постов.'


@app.route('/add')
def add():
    return 'Добавление записи.'


@app.route('/edit')
def edit():
    return 'Изменение поста'


@app.route('/delete')
def delete():
    return 'Удаление постов.'


