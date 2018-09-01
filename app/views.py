from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the page and and its data
    '''

    # Getting breaking news source
    general_source = get_sources('general')
    sports_source = get_sources('sports')
    technology_source = get_sources('technology')
    entertainment_source = get_sources('entertainment')
    business_source = get_sources('business')
    title = 'Home - Welcome to the NewsHighlights '
    return render_template('index.html',title = title, general = general_source, sports = sports_source,technology =technology_source, entertainment = entertainment_source, business =business_source)

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    view source page function that returns the source details page and its data
    '''
    title = f'You viewing {movie_id}'
    return render_template('source.html',title = title)    
