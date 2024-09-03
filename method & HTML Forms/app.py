from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/aksi', methods=['POST', 'GET'])
def aksi():
    return render_template('bio.html',
                        nama = request.form['nama'],
                        kelas = request.form['kelas'],
                        email = request.form['email'],
                        tempat = request.form['tempat'],
                        tgl = request.form['tgl'],
                        cita_cita = request.form['cita_cita'],
                        agama = request.form['agama'],
                        tentang = request.form['tentang']
                             )

if __name__ == "__main__":
    app.run(debug=True)
