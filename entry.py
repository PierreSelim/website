import os


class Entry(object):

    def __init__(self, page):
        self.page = page
        if page.endswith('.md'):
            self.page = page.replace('.md', '')
        if page.endswith('.html'):
            self.page = page.replace('.html', '')

    @property
    def title(self):
        return self.page.replace('_', ' ').title()

    @property
    def content(self):
        with open('entries/{}.md'.format(self.page)) as p:
            return p.read().decode('utf-8')

    @property
    def link(self):
        return './entry/{}.html'.format(self.page)


def allentries():
    lines = []
    files = os.listdir('./entries')
    sort_fun = lambda x: os.path.getctime('./entries/{}'.format(x))
    for filename in sorted(files, key=sort_fun):
        if filename.endswith('.md'):
            entry = Entry(filename)
            lines.append("* [{}]({})".format(entry.title, entry.link))
    return '\n'.join(lines)
