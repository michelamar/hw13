from flask import Flask, render_template
import urllib2
import json
my_app = Flask (__name__)

@my_app.route('/')
def root():
    u=urllib2.urlopen("https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=a7e4cb2fa4bf4516b1ca846478b5db68&query=%27dirty+dancing%27")
    data=u.read()
    j=json.loads(data)
    summ = j["summary_short"]
    u1=urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=8ZqNehYsRGtfJng2QF1ZkPlcNUjBc6emMIu7CavP")
    data=u1.read()
    j1=json.loads(data)
    pic = j1["url"]
    caption = j["explanation"]
    return render_template("restAPI.html", pic, caption, summ)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
