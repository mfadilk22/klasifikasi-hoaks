from fileinput import filename
from unittest import result
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import os
from werkzeug.utils import secure_filename

import pickle
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask_wtf import FlaskForm
from wtforms import FileField

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_PATH'] = "uploaded_files"
app.config['ALLOWED_EXTENSIONS'] = ['txt']
app.config['UPLOAD_EXTENSIONS'] = ['.txt']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


model_path = 'models/'
# load model
model = tf.keras.models.load_model(model_path+"model_4.h5")

# load tokenizer
token = Tokenizer()
with open(model_path+'token_4.pickle', 'rb') as handle:
    token = pickle.load(handle)
    
def klasifikasi_kata(sentences):
    teks = [sentences]
    sequences = token.texts_to_sequences(teks)
    padded = pad_sequences(sequences, maxlen=40, padding="post", truncating="post")
    res = model.predict(padded)
    res_rounded_value = round((res[0][0]*100),3)
    res_string = res_rounded_value
    return res_string

def klasifikasi_file(sentences):
    teks = [sentences]
    sequences = token.texts_to_sequences(teks)
    padded = pad_sequences(sequences, maxlen=40, padding="post", truncating="post")
    res = model.predict(padded) 
    res_rounded_value = round((res[0][0]*100),3)
    res_string = res_rounded_value
    return res_string

def upload_files():
    if request.method == "POST":        
        f = request.files['file']
        filename = secure_filename(f.filename)
        if filename !='':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                return "File tidak mendukung", 400    
            saved_file = f.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            file = open(app.config['UPLOAD_PATH']+"/"+filename,"r")        
            content = file.read()
            file.close()            
        #return ""   
    os.remove(app.config['UPLOAD_PATH']+"/"+filename)     
    return content

@app.route('/', methods=['GET'])
def index():    
    return render_template('index.html')

@app.route('/klasifikasi', methods=['GET',"POST"])
def prediksi_teks():
    if request.method == "POST":        
        message = request.form['teks']
        hasil_pred = klasifikasi_kata(message)
        # return render_template(('index.html'), prediksi = hasil_pred)    
    return render_template(('index.html'), prediksi = hasil_pred)
    #return redirect(url_for('index', prediksi = hasil_pred))

@app.route('/klasifikasi-file', methods=['GET',"POST"])
def prediksi_file():
    if request.method == "POST":  
        # filename = upload_files()
        # file = open(app.config['UPLOAD_PATH']+"/"+filename,"r")        
        message = upload_files()
        hasil_pred = klasifikasi_file(message)
        
        # return render_template(('index.html'), prediksi = hasil_pred) 
    return render_template(('index.html'), prediksi = hasil_pred)   
    #return redirect(url_for('index', prediksi = hasil_pred))

  

@app.errorhandler(413)
def too_large(e):
    return "Ukuran file melebihi 1 mb", 413

# @app.route('/uploaded_files/<filename>')
# def upload(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == "__main__":
    app.run()