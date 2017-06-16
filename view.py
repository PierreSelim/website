import markdown
from flask import Flask, render_template, Markup

from entry import Entry, allentries


app = Flask(__name__)


@app.route('/entry/<page>')
def display_page(page):
    entry = Entry(page)
    content = Markup(markdown.markdown(entry.content))
    return render_template('entry.html', title=entry.title, content=content)


@app.route('/')
def index():
    content = Markup(markdown.markdown(allentries()))
    return render_template('index.html', title='Pages', content=content)
