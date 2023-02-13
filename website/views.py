from flask import Blueprint, render_template, request
from .load_data import load_data

views = Blueprint('view', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        search_key = request.form.get('search_key')
        items = load_data(search_key)
        return render_template('items.html', items=items, title=search_key)
    else:
        return render_template('base.html')