import os
from flask_frozen import Freezer

from view import app


freezer = Freezer(app)


@freezer.register_generator
def display_page():
    for filename in os.listdir('./entries'):
        if filename.endswith('.md'):
            # Generate an html file
            yield {'page': filename.replace('.md', '.html')}


if __name__ == '__main__':
    freezer.freeze()
