#!/usr/bin/python
#-*- coding: utf-8 -*-

import waltz
from waltz import track, render, web

urls = ('/analytics/?', 'waltz.modules.Analytics',
        '/(.+)', 'Entry',
        '/', 'Index',
        '.*', 'Error')


env = {'ctx': web.ctx}
app = waltz.setup.dancefloor(urls, globals(), env=env)

class Entry:
    def GET(self, entry):
        try:
            return getattr(render2, entry, None)()
        except:
            return render.index()

class Index:
    @track
    def GET(self):
        return render().index()

class Error:
    def GET(self):
        raise web.notfound("404")

if __name__ == "__main__":
    app.run()
