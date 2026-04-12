from flask import Flask

# ...
# It create an instance of the flask class,
# ...
### WSGI APPLICATION
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to this flask work.its amazing</H1></html>"

@app.route("/index")
def index():
    return "welcome to the index page"

if __name__=="__main__":
    app.run(debug=True)