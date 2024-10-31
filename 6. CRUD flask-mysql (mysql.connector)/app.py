from flask import *
import mysql.connector

app = Flask(__name__)

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sekolah",
    password="")

# Get a cursor
cur = cnx.cursor()

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods = ["POST", "GET"] )
def simpan():
    nama = request.form["nama"]
    kelas = request.form["kelas"]
    alamat = request.form["alamat"]
    query = ("insert into siswa values( %s, %s, %s, %s)")
    data = ( "", nama, kelas, alamat )
    cur.execute( query, data )
    cnx.commit()
    cur.close()
    return f"sukses disimpan.."

@app.route('/tampil')
def tampil():
    cur.execute("select * from siswa")
    data = cur.fetchall()
    cur.close()
    return render_template('tampil.html',data=data) 

@app.route('/hapus/<id>')
def hapus(id):
    query = ("delete from siswa where id = %s")
    data = (id,)
    cur.execute( query, data )
    mysql.connection.commit()
    cur.close()
    return redirect('/tampil')

@app.route('/update/<id>')
def update(id):
    sql = ("select * from siswa where id = %s")
    data = (id,)
    cur.execute( sql, data )
    value = cur.fetchone()
    return render_template('update.html',value=value) 


@app.route('/aksiupdate', methods = ["POST", "GET"] )
def aksiupdate():
    id = request.form["id"]
    nama = request.form["nama"]
    kelas = request.form["kelas"]
    alamat = request.form["alamat"]
    query = ("update siswa set nama = %s, kelas = %s, alamat = %s where id = %s")
    data = ( nama, kelas, alamat,id, )
    cur.execute( query, data )
    mysql.connection.commit()
    cur.close()
    return redirect('/tampil')

if __name__ == "__main__":
    app.run(debug=True)