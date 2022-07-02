from fileinput import filename
from tkinter import ANCHOR
from unittest import result
from click import option
from flask import Flask,flash, redirect, url_for, render_template, request, send_from_directory
import os
from jinja2 import Markup
from werkzeug.utils import secure_filename
import spacy
from spacy.util import minibatch, compounding
from spacy import load, displacy
from spacy.training.example import Example
from pathlib import Path

import pickle
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask_wtf import FlaskForm
from wtforms import FileField
from flaskext.markdown import Markdown

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["DEBUG"] = True
app.config['UPLOAD_PATH'] = "uploaded_files"
app.config['ALLOWED_EXTENSIONS'] = ['txt']
app.config['UPLOAD_EXTENSIONS'] = ['.txt']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
Markdown(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

model_path = 'models/'
# load model
model = tf.keras.models.load_model(model_path+"model_FINAL.h5")
model_ner = spacy.load(model_path+"NER_3")


colors= {'ORGANISASI':'#54dda4', "ORANG":'#54dda4', "LOKASI":'#54dda4', "PENYAKIT":'#54dda4', "VAKSIN":'#54dda4'}
options = {'ents': ['ORGANISASI',"ORANG","LOKASI","PENYAKIT","VAKSIN"], 'colors':colors}

# load tokenizer
token = Tokenizer()
with open(model_path+'token_FINAL.pickle', 'rb') as handle:
    token = pickle.load(handle)
    
def klasifikasi_kata(sentences):
    hasil_dict = dict()

    teks = [sentences]
    sequences = token.texts_to_sequences(teks)
    padded = pad_sequences(sequences, maxlen=20, padding="post", truncating="post")
    res = model.predict(padded)
    res_rounded_value = round((res[0][0]*100),2)
    res_string = res_rounded_value
    hasil_dict["klasifikasi"] = res_string

    doc = model_ner(sentences)
    hasil_doc = displacy.render(doc, style="ent", options=options)
    hasil_doc = Markup(hasil_doc)
    # hasil_doc = hasil_doc.replace("\n\n","\n")
    hasil_dict['ner'] = hasil_doc

    return hasil_dict

def klasifikasi_file(sentences):
    hasil_dict = dict()

    teks = [sentences]
    sequences = token.texts_to_sequences(teks)
    padded = pad_sequences(sequences, maxlen=20, padding="post", truncating="post")
    res = model.predict(padded) 
    res_rounded_value = round((res[0][0]*100),2)
    res_string = res_rounded_value  
    hasil_dict["klasifikasi"] = res_string

    doc = model_ner(sentences)
    hasil_doc = displacy.render(doc, style="ent", options=options)
    hasil_doc = Markup(hasil_doc)
    # hasil_doc = hasil_doc.replace("\n\n","\n")
    hasil_dict['ner'] = hasil_doc

    return hasil_dict

def upload_files():
    content = dict()
    
    if request.method == "POST":   

        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('index'))              
        
        f = request.files['file']                
        
        if f.filename == '':
            flash('No selected file')
            return redirect(url_for('index'))

        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            # file_ext = os.path.splitext(filename)[1]

            # if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            #     return "File tidak mendukung", 400  

            saved_file = f.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            file = open(app.config['UPLOAD_PATH']+"/"+filename,"r")   
            content['filename'] = filename     
            content['isi'] = file.read()
            file.close()

            os.remove(app.config['UPLOAD_PATH']+"/"+filename)     
            return content   
        # else:
        #     flash("Pilih 1 file")
        #     return render_template('index.html')       
        #return ""   
    

@app.route('/', methods=['GET'])
def index():    
    return render_template('index.html')

@app.route('/klasifikasi', methods=['GET',"POST"])
def prediksi_teks():
    if request.method == "POST":        
        message = request.form['teks']
        hasil_pred = klasifikasi_kata(message)
        # return render_template(('index.html'), prediksi = hasil_pred)    
    return render_template(('index.html'), prediksi_teks = hasil_pred['klasifikasi'], ner_teks = hasil_pred['ner'],pesan = message)
    #return redirect(url_for('index', prediksi = hasil_pred))

@app.route('/klasifikasi-file', methods=['GET',"POST"])
def prediksi_file():
    content = dict()
    
    if request.method == "POST":   

        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('index'))              
        
        f = request.files['file']                
        
        if f.filename == '':
            flash('No selected file')
            return redirect(url_for('index'))

        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            # file_ext = os.path.splitext(filename)[1]

            # if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            #     return "File tidak mendukung", 400  

            saved_file = f.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            file = open(app.config['UPLOAD_PATH']+"/"+filename,"r")   
            content['filename'] = filename     
            content['isi'] = file.read()
            file.close()

            os.remove(app.config['UPLOAD_PATH']+"/"+filename)     
            # return content

    # if request.method == "POST":  
        # filename = upload_files()
        # file = open(app.config['UPLOAD_PATH']+"/"+filename,"r")        
        # message = upload_files()
        hasil_pred = klasifikasi_file(content['isi'])
        
        # return render_template(('index.html'), prediksi = hasil_pred) 
    return render_template(('index.html'),prediksi_file = hasil_pred['klasifikasi'], ner_file = hasil_pred['ner'], display="flex", filename = content['filename'])   
    #return redirect(url_for('index', prediksi = hasil_pred))

  

@app.errorhandler(413)
def too_large(e):
    return "Ukuran file melebihi 1 mb", 413
    

# @app.route('/uploaded_files/<filename>')
# def upload(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == "__main__":
    app.run()