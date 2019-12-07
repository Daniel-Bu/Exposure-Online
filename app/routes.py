import sys
import os
from flask import render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
from exposure.app_evaluate import evaluate

DOWNLOAD_FOLDER = 'app/static/download'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif', 'tiff'}

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('enhance', filename=filename))

    return render_template('upload.html')

@app.route('/enhance', methods=['GET', 'POST'])
def enhance():
    if request.method == 'POST':
        filename = request.values.get('fn')
        os.chdir('./exposure')
        file_path = os.path.join('..', app.config['UPLOAD_FOLDER'], filename)
        evaluate([file_path])
        os.chdir('../')
        nfilename = filename + '.retouched.png'
        if not os.path.exists(os.path.join(DOWNLOAD_FOLDER, nfilename)):
            nfilename = None

        return redirect(url_for('download', filename=filename, nfilename=nfilename))
    
    return render_template('enhance.html', filename=request.args.get('filename'))

@app.route('/download', methods=['GET'])
def download():
    return render_template('download.html',
                            filename=request.args.get('filename'),
                            nfilename=request.args.get('nfilename'))
