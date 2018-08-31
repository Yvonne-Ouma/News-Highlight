from flask import render_template
from app import app

# Views
@ap.route('')
def index():
    '''
    View root page function that returns the page and and its data
    '''
    return render_tenplate('index.html')