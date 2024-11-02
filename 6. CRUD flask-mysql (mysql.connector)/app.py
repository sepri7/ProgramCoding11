from flask import *
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sekolah",
    password="")

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods = ["POST", "GET"] )
def simpan():

    cursor = mydb.cursor()
    nama = request.form["nama"]
    kelas = request.form["kelas"]
    alamat = request.form["alamat"]
    query = ("insert into siswa values( %s, %s, %s, %s)")
    data = ( "", nama, kelas, alamat )
    cursor.execute( query, data )
    mydb.commit()
    cursor.close()
    return redirect("/tampil")

@app.route('/tampil')
def tampil():
    cursor = mydb.cursor()
    cursor.execute("select * from siswa")
    data = cursor.fetchall()
    return render_template('tampil.html',data=data) 

@app.route('/hapus/<id>')
def hapus(id):
    cursor = mydb.cursor()
    query = ("delete from siswa where id = %s")
    data = (id,)
    cursor.execute( query, data )
    mydb.commit()
    cursor.close()
    return redirect('/tampil')

@app.route('/update/<id>')
def update(id):
    cursor = mydb.cursor()
    query = ("select * from siswa where id = %s")
    data = (id,)
    cursor.execute( query, data )
    value = cursor.fetchone()
    return render_template('update.html',value=value) 


@app.route('/aksiupdate', methods = ["POST", "GET"] )
def aksiupdate():
    cursor = mydb.cursor()
    id = request.form["id"]
    nama = request.form["nama"]
    kelas = request.form["kelas"]
    alamat = request.form["alamat"]
    query = ("update siswa set nama = %s, kelas = %s, alamat = %s where id = %s")
    data = ( nama, kelas, alamat,id, )
    cursor.execute( query, data )
    mydb.commit()
    cursor.close()
    return redirect('/tampil')

if __name__ == "__main__":
    app.run(debug=True)