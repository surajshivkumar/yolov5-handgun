import os
def predict(x,response):
	options = {"conf-thresh":0.25,"iou-thresh":0.45,"hide-labels":"","hide-conf":""}
	for i in options.keys():
		options[i] = response[i]
	command = 'python detect.py --weights last.pt --img 640 --source {} --conf {} --iou {} --name outs --project flask_app/static/images/  {}  {}'.format(x,options["conf-thresh"],options["iou-thresh"],options["hide-conf"],options["hide-labels"])
	os.chdir('../')
	path = 'python detect.py --weights last.pt --img 640 --conf 0.25 --source ' + x  + ' --name outs --project flask_app/static/images/'
	os.system(command)
	os.chdir('./flask_app/')
#python detect.py --weights last.pt --img 640 --conf 0.25 --source flask_app/static/images/ins/P00660h.jpg --name outs --project flask_app/static/images/
