import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,current_app
)

from .lib import indexer,keywords,matcher

bp = Blueprint('search', __name__, url_prefix='/')
k = keywords.keywords()
mymatcher = matcher.matcher()

i = None

@bp.route('/'      , methods=("GET",))
@bp.route('/search', methods=("GET",))
def search():
    global i
    return render_template('search/search.html' , indexer=i, keywords="" )

@bp.route('/index', methods=("GET",))
def index():
    global i
    i = indexer.indexer( url=current_app.config["MEDIA_ROOT"] , kw=k )
    return render_template('index/index.html' , documents=i.documents )

@bp.route('/show', methods=("GET",))
def show():
    return render_template('index/index.html' , documents=i.documents )

@bp.route('/query', methods=("POST",))
def query():
    global i

    search_string = request.form["query"]
    print( search_string )
    keywords = k.search_words( search_string )

    if i:
        result = mymatcher.simple_match( i.documents , keywords )
        return render_template('search/search.html' , indexer=i , keywords=keywords , matches=result )

    return render_template('search/search.html' , indexer=i , keywords=keywords , matches=None )
