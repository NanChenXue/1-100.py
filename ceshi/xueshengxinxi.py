import flask
app = flask.Flask(__name__)

@app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
# if __name__=="__main__":
#     app.run()
def index():
    fobj=open("css入门1.html","rb")
    data=fobj.read()
    fobj.close()
    return data
if __name__=="__main__":
    app.run()



