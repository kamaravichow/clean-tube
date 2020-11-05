from flask import Flask, render_template, request, jsonify
from youtube_dl import YoutubeDL

app = Flask(__name__)

ytdl = YoutubeDL()


@app.route('/', methods=['GET'])
def home():
    return render_template('home')