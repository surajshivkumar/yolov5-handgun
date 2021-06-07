import os
def predict(x):
	#os.chdir('../')
	path = 'python detect.py --weights last.pt --img 640 --conf 0.25 --source ' + x  + ' --name outs --project flask_app/static/images/'
	os.system(path)
#python detect.py --weights last.pt --img 640 --conf 0.25 --source flask_app/static/images/ins/P00660h.jpg --name outs --project flask_app/static/images/
