from flask import Blueprint, url_for, render_template


web = Blueprint('web', __name__, static_folder='../../front/templates')


@web.route('/')
def home():
    return web.send_static_file('index.html')

