from flask import Flask, render_template
import urllib2
import json
my_app = Flask (__name__)

@my_app.route('/')
def root():
    u=urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=8ZqNehYsRGtfJng2QF1ZkPlcNUjBc6emMIu7CavP")
    str = u.read()
    j=json.loads(read)
    pic = j["url"]
    caption = j["explanation"]
    return render_template("restAPI.html", pic, explanation)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
