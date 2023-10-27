from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def principal():
    return render_template("index.html")

@app.route('/contacto')

def contacto():
    return render_template("contacto.html")
@app.route('/mapas')

def home():
    return render_template("home.html")
@app.route('/home')

def mapas():
    return render_template("SolarScout.html")

if __name__ == '__main__':
    app.run(debug=True)

