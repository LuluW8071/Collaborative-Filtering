from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle 
from math import ceil

from algoliasearch.search_client import SearchClient
from api import ALGOLIA_APP_ID, ALGOLIA_API_KEY, ALGOLIA_INDEX_NAME

popular_df = pickle.load(open('model/popular.pkl', 'rb'))
pt = pickle.load(open('model/pt.pkl', 'rb'))
books_df = pickle.load(open('model/books.pkl', 'rb'))
similarity_scores = pickle.load(open('model/similarity_scores.pkl', 'rb'))
                                
app = Flask(__name__)

#Static location config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'static'

#Setting up home page
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 12
    book_data = popular_df[popular_df['avg_rating'] > 3][['Book-Title', 
                                                          'Book-Author', 
                                                          'Image-URL-L',
                                                          'num_ratings', 
                                                          'avg_rating', 
                                                          'ISBN', 
                                                          'Year-Of-Publication', 
                                                          'Publisher']]

    book_data = book_data.iloc[(page-1)*per_page: page*per_page]

    book_name = list(book_data['Book-Title'].values)
    author = list(book_data['Book-Author'].values)
    image = list(book_data['Image-URL-L'].values)
    votes = list(book_data['num_ratings'].values)
    rating = list(book_data['avg_rating'].values)
    isbn = list(book_data['ISBN'].values)
    year_of_publication = list(book_data['Year-Of-Publication'].values)
    publisher = list(book_data['Publisher'].values)

    #Pagination
    num_pages = ceil(len(popular_df) / per_page)
    prev = '/?page=' + str(page-1) if page > 1 else '#'
    next = '/?page=' + str(page+1) if page < num_pages else '#'

    return render_template('home.html', book_name=book_name, 
                                        author=author, 
                                        image=image, 
                                        votes=votes, 
                                        rating=rating, 
                                        isbn=isbn,
                                        year_of_publication=year_of_publication, 
                                        publisher=publisher,
                                        num_pages=num_pages,
                                        page=page, 
                                        prev=prev, 
                                        next=next)
        
# Algolia Search
client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
index = client.init_index(ALGOLIA_INDEX_NAME)

#Search function
@app.route('/search')
def search():
    query = request.args.get('query')
    format = request.args.get('format', 'html')

    if not query:
        if format == 'json':
            return jsonify({'error': 'query parameter is required'})
        else:
            return render_template('search.html', 
                                   error='query parameter is required')

    results = index.search(query)
    hits = results['hits']

    if format == 'json':
        return jsonify(hits)
    return render_template('search.html', hits=hits, query=query)


    
if __name__ == '__main__':
    app.run(debug=True)