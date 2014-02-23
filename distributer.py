from utils import *
from socket import *
import thread
import time
import json
import inspect
import os
UPLOAD_FOLDER = '/Users/bencoh/Dropbox/McHacks/uploads'

UPLOAD_FOLDER = '/root'
totals = {}
t = 100
class job_list(object):
    def __init__(self, text_file, fun_file):
        print "HURR 1"
        allJobs = []
        # UPLOAD_FOLDER = '/Users/bencoh/Dropbox/McHacks/uploads'
        p = os.path.join(UPLOAD_FOLDER, text_file)
        print p
        i = open(p)
        print "HURR 2"

        for line in i:
            allJobs.append(line.strip())

        # self.allJobs = [x for x in range(1000,1150)]
        self.allJobs = allJobs
        self.num = 0
        self.jobs = len(self.allJobs)


    def __iter__(self):
        return self

    def __next__(self):
        return self.allJobs.next()

    def next_job(self):
        if self.num >= self.jobs:
            return -1
        else:
            self.num += 1
            return self.allJobs[self.num - 1]



def handler(clientsock,addr, jobs):

    BUFFER_SIZE = 1024
    jobs_sent = 0
    f = inspect.getsource(hsh2)

    print f
    clientsock.send(str(f))
    while 1:
        try:
            data = clientsock.recv(88)


            # print data
            if data == 'Job Request':
                print "Giving out a job: " + str(jobs_sent)
                jobs_sent += 1
                next_job = jobs.next_job()
                print "NJ: " + str(next_job)
                if next_job == -1 or next_job == str(-1):
                    clientsock.sendall('done');
                    print totals
                    pth = os.path.join(UPLOAD_FOLDER, 'results.txt')
                    print pth
                    f = open(pth, 'w')
                    f.write(str(totals))
                    f.close()
                    # import os
                    os._exit(-1)

                    print str(time.time() + t) + " seconds"
                    return -1
                clientsock.sendall(str(next_job))
                try:
                    data = clientsock.recv(BUFFER_SIZE)
                except:
                    data = ""
                while(data == ""):
                    try:
                        data = clientsock.recv(BUFFER_SIZE)
                    except:
                        pass
                print data
                totals[next_job] = data
               

                for x in data:
                    totals[x] += data[x]
        except:
            pass


def main(fl, fl2):
    print "STARTING"
    totals = {chr(x + 97): 0 for x in range(15)}

    BUFF = 32768
    HOST = '127.0.0.1'# must be input parameter @TODO
    HOST = '0.0.0.0'
    PORT = 5005 # must be input parameter @TODO
    print "BEFORE JOBS LIST"
    jobs = job_list(fl, fl2)

    print "GOT A JOBS LIST"
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(50)
    first = True
    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        if first:
            global t 
            t  = -1 * time.time()
            first = False
        print '...connected from:', addr
        v = thread.start_new_thread(handler, (clientsock, addr, jobs))
        print "WE HAVE V: " + str(v)
        if v == -1:
            return str(-1)

def job_generator(job_list):
    i = len(job_list)
    x = 0
    while x < i:
        yield job_list[x]
        x += 1

def hsh2(h):
    import hashlib

    for r in range(1000000):
        h = hashlib.sha384(str(h)).hexdigest()

    return h


def prepare_jobs(text_file, num_jobs):
    flat_text = open(text_file).readline()

    length = len(flat_text)
    allJobs = []
    for x in range(num_jobs):
        allJobs.append(flat_text[x * (length/num_jobs):(x+1) * (length/num_jobs)])


    # print allJobs[:5]
    return allJobs

if __name__ == "__main__":
    main('datafile', 'tmp')
    # prepare_jobs('out.txt', 1000000)