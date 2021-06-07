import os
def empty():
    os.chdir('static/images/')
    #os.system('cd flask_app/static/images/')
    p = os.listdir()
    if "outs" in p:
        os.system('rmdir /s /q outs')
    os.chdir('../')
    os.chdir('../')
