import sys
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/Users/bencoh/Dropbox/McHacks/uploads'
# UPLOAD_FOLDER = '/root'
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
    print 'hrr'
    global client
    client = spinner.initialize()

    return render_template("main.html", **{'content' : 'Initialized'})


@app.route('/results')
def view_results():
    pth = os.path.join(app.config['UPLOAD_FOLDER'], 'results.txt')
    v = ""
    for line in open(pth):
        v += line

    return v
    
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
            map_fl.save(os.path.join(app.config['UPLOAD_FOLDER'], 'func_def.py'))

            print "SAVED"
            return redirect(url_for('start_job'))


    print "NOT POST"
    return render_template('main.html', **{'new_job' : True, 'content': "New Job Creation"})


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
    return redirect(url_for('view_results'))



@app.route('/kill_all')
def kill_all():
    try:
        spinner.destroy_all_droplets(client)
    except:
        return render_template('main.html', **{'content': "Couldn't kill all instances"})


    return render_template('main.html', **{'content': "Sucessfully Killed All Instances"})


@app.route('/off_all')
def turn_off_all():
    try:
        spinner.kill_all_droplets(client)
    except:
        return render_template("main.html", **{'content' : 'Something Went Wrong'})
    return render_template("main.html", **{'content' : 'Turned Machines off Sucessfully'})



@app.route('/spawn/<num_instances>')
def spawn(num_instances):
    spinner.spawn(client, num_instances = int(num_instances))

    return render_template('main.html', **{'content': "Sucessfully Spawned New Instances"})


@app.route('/spawn_form', methods = ['POST', 'GET'])
def spawn_form():
    if request.method == 'POST':

        print "POSTING"
        fl = request.form['num']


        if fl != None:
            u = url_for('spawn',num_instances=fl)
            return redirect(u)

    return render_template('main.html', **{'Spawn' : True, 'content': "How Many Machines do you want spawned?"})


@app.route('/on_form', methods = ['POST', 'GET'])
def turn_on_form():
    if request.method == 'POST':

        print "POSTING"
        fl = request.form['num']


        if fl != None:
            u = url_for('on',num_instances=fl)
            return redirect(u)

    return render_template('main.html', **{'onn' : True, 'content': "How Many Machines do you want turned on?"})




@app.route('/turn_on/<num_instances>')
def on(num_instances):
    # spinner.on(client, num_instances = int(num_instances))
    numOn = 0
    for x in client.show_active_droplets():
        print x.id
        if numOn > int(num_instances):
            break
        else:
            numOn += 1
            print "Turning On: " + str(numOn-1)
            spinner.turn_on_droplet(client, x.id)

        return render_template('main.html', **{'content': "Machines Turned On"})




if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0',port=80)   
