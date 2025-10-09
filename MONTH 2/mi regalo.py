from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Lee las imágenes de la carpeta static/imagenes
    imagenes = os.listdir('static/imagenes')
    frases = [
        "Eres mi lugar favorito en el mundo 💖",
        "Contigo todo es mejor 🌹",
        "Te amo hasta el infinito y mas allá ✨",
        "Te amo más de lo que puedo decir 💞",
        "Mi corazón es todo tuyo💫"
        "Te amo ahora y te amare siempre🥰"
         "Felices dos meses mi amor💙"
    ]
    return render_template('index.html', imagenes=imagenes, frases=frases)

if __name__ == '__main__':
    app.run(debug=True)
