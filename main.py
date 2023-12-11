# Import
from flask import Flask, render_template,request, redirect
from datetime import datetime

year = (datetime.now().year) - 2008 #nice

app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ana_sayfa')
def ana_sayfa():
    return render_template("ana_sayfa.html")

@app.route('/hakkımızda')
def hakkimizda():
    return render_template("hakkimizda.html")

@app.route('/iletişim')
def iletişim():
    return render_template("iletişim.html")

@app.route('/ürünler')
def ürünler():
    return render_template("ürünler.html")

@app.route('/hizmetler')
def hizmetler():
    return render_template("hizmetler.html")

@app.route('/dfits')
def dfits():
    return render_template("daha_fazlasi_icin_tiklayin_sitesi.html")

@app.route('/dfits2')
def dfits2():
    return render_template("daha_fazlasi_icin_tiklayin_sitesi2.html")

# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python,
                           year = year)



if __name__ == "__main__":
    app.run(port=4000, debug=True)
