from flask import*
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

userAdmin = {
    "username" : "admin",
    "password" : "1234"
}
userAnggota = {
    "username" : "anggota",
    "password" : "4321"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    if session.get("user"):
        return render_template("admin.html")
    else:
        return redirect(url_for("home"))
        

@app.route('/anggota')
def anggota():
    return render_template("anggota.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == userAdmin["username"] and password == userAdmin["password"]:
        session["user"] = username
        return redirect(url_for('admin'))
    elif username == userAnggota["username"] and password == userAnggota["password"]:
        session["user"] = username
        return redirect(url_for('anggota'))
    else:
        return f"salah...."

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)