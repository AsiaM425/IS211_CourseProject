from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_catalogue.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    page_count = db.Column(db.Integer)
    average_rating = db.Column(db.Float)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    isbn = request.form['isbn']
    book_data = fetch_book_data(isbn)
    if book_data:
        # Process book data and store it in the database
        book = Book(
            title=book_data['title'],
            author=book_data['author'],
            page_count=book_data['pageCount'],
            average_rating=book_data['averageRating']
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return "Book not found"

def fetch_book_data(isbn):
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and data['items']:
            book_info = data['items'][0]['volumeInfo']
            title = book_info.get('title', 'Unknown Title')
            author = ", ".join(book_info.get('authors', ['Unknown Author']))
            page_count = book_info.get('pageCount', 0)
            average_rating = book_info.get('averageRating', 0.0)
            return {
                'title': title,
                'author': author,
                'pageCount': page_count,
                'averageRating': average_rating
            }
    return None

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
