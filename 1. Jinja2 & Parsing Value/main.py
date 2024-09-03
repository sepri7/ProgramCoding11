from flask import Flask, render_template, request
app = Flask( __name__ )

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
#str
@app.route('/about/<string:author>')
def about(author):
    return render_template("about.html", author = author)
#int
@app.route('/about_int/<int:author>')
def about_int(author):
    return render_template("about.html", author = author)
#none
@app.route('/about_none/<author>')
def about_none(author):
    return render_template("about.html", author = author)
#parser
@app.route('/about_parser')
def about_parser():
    data = request.args.get("value")
    return render_template("about.html", author = data)


@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/contact')
def contact():
    return "<h1>contact Page</h1>"




if __name__ == "__main__":
    app.run( debug=True )