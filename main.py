#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import speech_recognition as sr
import os

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    transcript = ""
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST", )
    else:
        return render_template("index.html")


def lower(param):
    pass


@app.route("/transcribe", methods=['POST', 'GET'])
def transcribe():
    transcript = ""
    if request.method == "POST":

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
        return render_template('transcribe.html', transcript=transcript.lower())

    else:
        return render_template('transcribe.html')


if __name__ == "__main__":
    app.run(debug=True)
