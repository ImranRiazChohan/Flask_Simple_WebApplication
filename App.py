from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///posts.db"
db=SQLAlchemy(app)

class PostInfo(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    author=db.Column(db.String(32),nullable=False)
    title=db.Column(db.String(100),nullable=False)
    Blog=db.Column(db.Text,nullable=False,default='N/A')
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    # from App import db
    # from App import db_name
    # db.create_all()
    # db.session.add() add the data into the database
    # db_name.query.all() show all data from database
    # db.session.commit() save the data into database

    def __repr__(self):
        return "Blog Post"+str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/posts",methods=['GET','POST'])
def posts():
    if request.method == "POST":
        post_title=request.form["title"]
        post_blog=request.form["blog"]
        post_author=request.form['author']
        new_post=PostInfo(author=post_author,title=post_title,Blog=post_blog)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts=PostInfo.query.all()
        print(all_posts)
        return render_template("posts.html",post=all_posts)

if __name__=="__main__":
    app.run(debug=True)
