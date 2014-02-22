from utils import *
from socket import *
import thread

import json
totals = {}

class job_list(object):
    def __init__(self, text_file, num_jobs):
        # flat_text = open(text_file).readline()

        # length = len(flat_text)
        # allJobs = []

        # for x in range(num_jobs):
            
        #     allJobs.append(flat_text[x * (length/num_jobs):(x+1) * (length/num_jobs)])


        # self.allJobs = allJobs
        # self.num = 0
        # self.jobs = len(allJobs)
        # print "CREATED WITH " + str(length/128) + " jobs"

        self.allJobs = [x for x in range(1000,1050)]
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
    while 1:
        try:
            data = clientsock.recv(88)


            # print data
            if data == 'Job Request':
                print "Giving out a job: " + str(jobs_sent)
                jobs_sent += 1
                next_job = jobs.next_job()
                print "NJ: " + str(next_job)
                if next_job == -1:
                    clientsock.sendall('done');
                    print totals
                    import os
                    os._exit(0)
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


def main():
    totals = {chr(x + 97): 0 for x in range(26)}

    BUFF = 32768
    HOST = '127.0.0.1'# must be input parameter @TODO
    HOST = '0.0.0.0'
    PORT = 5005 # must be input parameter @TODO
    jobs = job_list('out.txt', 600)


    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr, jobs))

def job_generator(job_list):
    i = len(job_list)
    x = 0
    while x < i:
        yield job_list[x]
        x += 1

def prepare_jobs(text_file, num_jobs):
    flat_text = open(text_file).readline()

    length = len(flat_text)
    allJobs = []
    for x in range(num_jobs):
        allJobs.append(flat_text[x * (length/num_jobs):(x+1) * (length/num_jobs)])


    # print allJobs[:5]
    return allJobs

if __name__ == "__main__":
    main()
    # prepare_jobs('out.txt', 1000000)