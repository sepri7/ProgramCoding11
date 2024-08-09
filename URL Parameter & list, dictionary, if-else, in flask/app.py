from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

Data = [
    {
        'judul' : 'Hari Hari di IGS',
        'isi' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo nulla et ea qui accusantium praesentium molestiae deleniti similique. Fugiat reiciendis harum ipsa dolore aspernatur consequatur molestias labore deserunt recusandae id.',
        'tanggal' : 'jumat 9 ags 2004'
    },
    {
        'judul' : 'Hari CODING',
        'isi' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo nulla et ea qui accusantium praesentium molestiae deleniti similique. Fugiat reiciendis harum ipsa dolore aspernatur consequatur molestias labore deserunt recusandae id.',
        'tanggal' : 'KAMIS 8 ags 2004'
    },
    {
        'judul' : 'Hari DI RUMAH',
        'isi' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo nulla et ea qui accusantium praesentium molestiae deleniti similique. Fugiat reiciendis harum ipsa dolore aspernatur consequatur molestias labore deserunt recusandae id.',
        'tanggal' : 'SABTU 10 ags 2004'
    },
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/biodata')
def biodata():
    if 'namas' in request.args.keys() and 'umurs' in request.args.keys():
        nama = request.args['namas']
        umur = request.args['umurs']
        kelas = request.args.get('kelass')
        return render_template("biodata.html", nama = nama, umur=umur,kelas=kelas)
    else:
        return render_template("home.html")
    
@app.route('/blog')
def blog():
    DayCoding = ["kamis","jumat","sabtu"]
    # for day in DayCoding:
    #     print(day)

    day = datetime.now().day
    month = datetime.now().month

    return render_template("blog.html", DayCoding = DayCoding, Datas = Data, day = day, month = month)



if __name__ == "__main__":
    app.run(debug=True)