from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'elen6770_zb2244'
app.config['UPLOAD_FOLDER'] = 'app/static/upload'

from app import routes