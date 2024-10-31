from flask import *
from flask_mysqldb import *

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "sekolah"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""

mysql = MySQL(app)

@app.route('/') 
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods = ["POST", "GET"] )
def simpan():
    nama = request.form["nama"]
    kelas = request.form["kelas"]
    alamat = request.form["alamat"]
    cursor = mysql.connection.cursor()
    query = ("insert into siswa values( %s, %s, %s, %s)")
    data = ( "", nama, kelas, alamat )
    cursor.execute( query, data )
    mysql.connection.commit()
    cursor.close()
    return f"sukses disimpan.."

@app.route('/tampil')
def tampil():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from siswa")
    data = cursor.fetchall()
    cursor.close()
    return render_template('tampil.html',data=data) 

@app.route('/hapus/<id>')
def hapus(id):
    cursor = mysql.connection.cursor()
    query = ("delete from siswa where id = %s")
    data = (id,)
    cursor.execute( query, data )
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')

@app.route('/update/<id>')
def update(id):
    cursor = mysql.connection.cursor()
    sql = ("select * from siswa where id = %s")
    data = (id,)
    cursor.execute( sql, data )
    value = cursor.fetchone()
    return render_template('update.html',value=value) 


@app.route('/aksiupdate', methods = ["POST", "GET"] )
def aksiupdate():
    id = request.form["id"]
    nama = request.form["nama"]
    kelas = request.form["kelas"]
    alamat = request.form["alamat"]
    cursor = mysql.connection.cursor()
    query = ("update siswa set nama = %s, kelas = %s, alamat = %s where id = %s")
    data = ( nama, kelas, alamat,id, )
    cursor.execute( query, data )
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')


if __name__ == "__main__":
    app.run(debug=True)