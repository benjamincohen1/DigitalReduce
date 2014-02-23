import sys
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/Users/bencoh/Dropbox/McHacks/uploads'
UPLOAD_FOLDER = '/root'
import distributer

import spinner
# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import json
import flask

# import auth

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
client = None

@app.route('/')
def homepage():
    global client
    client = spinner.initialize()
    return "Initialized"



@app.route('/new_job', methods = ['GET', 'POST'])
def new_job():
    if request.method == 'POST':
        print "POSTING"
        fl = request.files['datafile']
        map_fl = request.files['mapfile']

        print "GOT FILE"
        if fl and map_fl:
            filename = secure_filename(fl.filename)
            print os.path.join(app.config['UPLOAD_FOLDER'], 'datafile')

            fl.save(os.path.join(app.config['UPLOAD_FOLDER'], 'datafile'))
            map_fl.save(os.path.join(app.config['UPLOAD_FOLDER'], 'funcfile'))

            print "SAVED"
            return redirect(url_for('start_job'))


    print "NOT POST"
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=datafile>
        <p><input type=file name=mapfile>

         <input type=submit value=Upload>
        </form>
        '''


@app.route('/start_job')
def start_job():
    print "EH"
    try:
        data_path =  os.path.join(app.config['UPLOAD_FOLDER'], 'datafile')
        function_path = os.path.join(app.config['UPLOAD_FOLDER'], 'funcfile')
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'datafile'))

    except:
        print "Failed to open file"
    distributer.main(data_path, function_path)
    # thread.start_new_thread(distributer.main, ('data_file.txt', 'func_file.txt'))
    # distributer.main('data_file.txt', 'func_file.txt')
    s = ""
    pth = os.path.join(app.config['UPLOAD_FOLDER'], 'results.txt')
    #return pth
    fl = open(pth)
    for line in fl:
	s += str(line.strip()) + "\n"
    return s



@app.route('/kill_all')
def kill_all():
    try:
        spinner.destroy_all_droplets(client)
    except:
        return "Something went wrong"

    return "Killed Em"

@app.route('/off_all')
def turn_off_all():
    try:
        spinner.kill_all_droplets(client)
    except:
        return "Something went wrong"
    return "Turned Em Off"


@app.route('/spawn/<num_instances>')
def spawn(num_instances):
    spinner.spawn(client, num_instances = int(num_instances))
    return "Spawned " + str(num_instances) + " instances."


@app.route('/turn_on/<num_instances>')
def on(num_instances):
    # spinner.on(client, num_instances = int(num_instances))
    numOn = 0
    for x in client.show_active_droplets():
        if numOn > int(num_instances):
            break
        else:
            numOn += 1
            print "Turning On: " + str(numOn-1)
            spinner.turn_on_droplet(client, x.id)

    return "Turned on " + str(num_instances) + " instances."



if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0',port=80)   
