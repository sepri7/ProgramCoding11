from flask import*
app = Flask(__name__)

userAdmin = {
    "username" : "admin",
    "password" : "1234"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    render_template("admin.html")

@app.route('/anggota')
def anggota():
    render_template("anggota.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == userAdmin["username"] and password == userAdmin["password"]:
        return redirect(url_for('admin'))
    else:
        return f"salah...."

if __name__ == "__main__":
    app.run(debug=True)