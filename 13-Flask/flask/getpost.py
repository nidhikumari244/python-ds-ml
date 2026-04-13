from flask import Flask,render_template,request 

# ...
# It create an instance of the flask class,
# ...
### WSGI APPLICATION
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to this flask work.its amazing</H1></html>"

@app.route("/index",method=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',method=['GET','POST'])
def form():
    if request.method=='POST':
      name=request.method['name']
      return f'Hello{name}!'  
    return render_template('form.html')



if __name__=="__main__":
    app.run(debug=True)