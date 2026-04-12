from flask import Flask

# ...
# It create an instance of the flask class,
# ...
### WSGI APPLICATION
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flask work.its amazing"

if __name__=="__main__":
    app.run(debug=True)