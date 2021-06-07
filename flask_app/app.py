from flask import Flask , render_template , flash , request, redirect , url_for,jsonify
from werkzeug.utils import secure_filename
from empty import empty
from detector import predict
from PIL import Image
import io
import os
import time
from main import add
import datetime
UPLOAD_FOLDER = "./static/images/ins"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4'])

global op
global tk
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
@app.route('/home')

def index():
	return render_template('base.html')



@app.route('/uploader', methods=['GET', 'POST'])
 
def upload_image():  
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file= request.files['file']  
	conf, iou = request.form['Confidence'],request.form['IOU']
	hide_conf,hide_label = "--hide-conf" if request.form.get('isHiddenConf') else "","--hide-labels" if request.form.get('isHiddenLabel') else ""
	toggle = request.form.get('toggle')
	options =  {"conf-thresh":conf,"iou-thresh":iou,"hide-labels":hide_label,"hide-conf":hide_conf}
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		print(filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('Image successfully uploaded and displayed below')
		val = request.get_json()
		pathin = "flask_app/static/images/ins/" + filename
		empty()
		start = datetime.datetime.now()
		predict(pathin,options)
		end =  datetime.datetime.now()
		delta = end  - start
		time_taken = str(int(delta.total_seconds()*1000))
		ouput_path = "static/images/outs/" + filename
		global op 
		global tk
		op = ouput_path
		tk= time_taken
		return render_template('pred.html', res2=[ouput_path,time_taken,options,toggle])

    
@app.route('/predictions')
def pred():
    return render_template('pred.html', res2=[op,tk])
@app.route('/modelperformace')
def modelperformace():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
