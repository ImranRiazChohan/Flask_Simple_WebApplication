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
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.now)

    # from App import db
    # from App import db_name
    # db.create_all()
    # db.session.add() add the data into the database
    # db_name.query.all() show all data from database
    # db.session.commit() save the data into database
    # db.session.delete(db_name.query.get()) delete the data from database

    def __repr__(self):
        return "Blog Post"+str(self.id)
    # def __init__(self,author,title,Blog):
    #     self.author=author
    #     self.title=title
    #     self.Blog=Blog
    #     self.id
    #     self.date_posted

all_posts=[
    {
        "title":"Post1",
        "content":"This is a content of post1.dasdjasgdfhuyg",
        "author":"usama"},
    {
        "title":"Post2",
        "content":"this is a content of post2.asdasfsdf",

    }]
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/posts",methods=['GET','POST'])
def posts():
    if request.method == "POST":
        post_title=request.form["title"]
        post_blog=request.form["blog"]
        post_author=request.form["author"]
        new_post=PostInfo(author=post_author,title=post_title,Blog=post_blog)
        # new_post=PostInfo(post_author,post_title,post_blog)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts=PostInfo.query.all()
        return render_template("posts.html",post=all_posts)

@app.route('/posts/delete/<int:id>')
def  delete(id):
    post=PostInfo.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/posts")
@app.route("/posts/edit/<int:id>",methods=['GET',"POST"])
def edit(id):
    post = PostInfo.query.get_or_404(id)
    if request.method=='POST':
        # post = PostInfo.query.get_or_404(id)
        post.title=request.form["title"]
        post.Blog=request.form["blog"]
        post.author=request.form["author"]
        db.session.commmit()
        return redirect("/posts")
    else:
        return render_template('edit.html',post=post)
@app.route("/posts/new",methods=['GET','POST'])
def new():
    if request.method == "POST":
        post_title=request.form["title"]
        post_blog=request.form["blog"]
        post_author=request.form["author"]
        new_post=PostInfo(author=post_author,title=post_title,Blog=post_blog)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts=PostInfo.query.all()
        return render_template("new.html",post=all_posts)


@app.route("/about")
def About():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
