from flask import Flask, render_template, request, jsonify
from youtube_dl import YoutubeDL

app = Flask(__name__)

ytdl = YoutubeDL()


def getVideoStreamUrl(url):
    videoInformation = ytdl.extract_info(url, download=False)
    streamUrl = videoInformation['formats'][-1]['url']
    return streamUrl


@app.route('/', methods=['GET'])
def home():
    return render_template('home')
