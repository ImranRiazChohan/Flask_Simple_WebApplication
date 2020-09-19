from flask import Flask,render_template

app=Flask(__name__)
all_post=[{
    "title":"Post1",
    "Content":"Hey Hello world",
    "Author":"Usama"},{
    "title":"Post2",
    "Content":"Hello world"
   }]

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/posts")
def post():

    return  render_template("posts.html",data=all_post)

if __name__=="__main__":
    app.run(debug=True)
