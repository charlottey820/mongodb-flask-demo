# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import datetime

import model

load_dotenv()

# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = datetime.datetime.now()


MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")

app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@cluster0.94cb3.mongodb.net/{MONGO_DBNAME}?retryWrites=true'

mongo = PyMongo(app)

# -- Routes section --

@app.route('/')
@app.route('/index')
def index():
    data = {
    }
    return render_template('index.html', data=data)

@app.route('/users')
def users_view():
    data = {
    'users':mongo.db.users.find({}),
    }
    return render_template('usersView.html', data=data)

@app.route('/users/<USER>')
def users_detail(USER):
    data = {
    'user':mongo.db.users.find_one({'name':USER}),
    'reviews':mongo.db.reviews.find({'user':USER}),
    }
    return render_template('usersDetail.html', data=data)

@app.route('/users/add', methods=['GET','POST'])
def users_add():
    if request.method == 'GET':
        data = {
        }
        return render_template('usersAdd.html', data=data)
    else:
        form = request.form
        user = {
        'name':form['userName'],
        }
        mongo.db.users.insert(user)
        return redirect(url_for('users_view'))

@app.route('/books')
def books_view():
    data = {
    'books':mongo.db.books.find({}),
    }
    return render_template('booksView.html', data=data)

@app.route('/books/<title>')
def books_detail(title):
    data = {
    'book':mongo.db.books.find_one({'title':title}),
    'reviews':mongo.db.reviews.find({'title':title}),
    }
    return render_template('booksDetail.html', data=data)

@app.route('/books/add', methods=['GET','POST'])
def books_add():
    if request.method == 'GET':
        data = {
        }
        return render_template('booksAdd.html', data=data)
    else:
        form = request.form
        book = {
        'title':form['bookTitle'],
        'author':form['bookAuthor'],
        'genre':form['bookGenre'],
        }
        data = {
        'book':book
        }
        mongo.db.books.insert(book)
        return render_template('booksDetail.html', data=data)

@app.route('/reviews')
def reviews_view():
    data = {
    'reviews':mongo.db.reviews.find({}),
    }
    return render_template('reviewsView.html', data=data)

@app.route('/review/add', methods=['GET','POST'])
def reviews_add():
    if request.method == 'GET':
        data = {
            'books':mongo.db.books.find({}),
            'users':mongo.db.users.find({}),
        }
        return render_template('reviewsAdd.html', data=data)
    else:
        form = request.form
        review = {
        'title':form['bookTitle'],
        'user':form['reviewUser'],
        'rating':int(form['reviewRating']),
        'review':form['reviewText'],
        }
        data = {
        'review':review
        }
        mongo.db.reviews.insert(review)
        return render_template('reviewsDetail.html', data=data)

#### Add new routes below this line ###
