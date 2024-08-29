from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tester1')
def tester1():
    return redirect('/contact')

@app.route('/tester2/<nama>')
def tester22(nama):
    if nama == "budi":
        return f"Hello ...{ nama } "
    else:
        return redirect('/')
    
@app.route('/tester3/<nama>')
def tester3(nama):
    if nama == "santo":
        return redirect(url_for('tester22', nama = "budi"))# redirect : function
    elif nama == "luis":
        return redirect("/contacts") # redirect : route
    else:
        redirect("/")

@app.route('/googlesc/<kata>')
def googlesc(kata):
    return redirect( f"https://www.google.com/search?q={kata}" )

@app.route('/gc')
def gc():
    return render_template('gc.html')

@app.route('/action_gc', methods = ['POST','GET'])
def action_gc():
    if request.method == "POST":
        return redirect( f"https://scholar.google.co.id/scholar?hl=id&q={request.form['keyword']}" )

if __name__ == "__main__":
    app.run(debug=True)