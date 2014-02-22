# from socket import *
import socket
import json
import time
def main():
    jobs_processed = 0
    # sock = socket(AF_INET, SOCK_DGRAM)
    addr = '107.170.73.117'
    # addr = 'localhost'
    TCP_IP = addr
    TCP_PORT = 5005
    BUFFER_SIZE = 32768

    # addr = 'localhost'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))

    sock.sendall('hello')
    time.sleep(.01)
    # sock.sendto('hello', (addr, 1055))
    state = 'requesting'
    oldJob = -1
    # sock.sendall('Job Request')

    while True:
        # time.sleep(.0001)
        # if state == 'requesting':
        time.sleep(.01)

        sock.send('Job Request')

        # time.sleep(.0001)
        curJob = sock.recv(BUFFER_SIZE)
        print curJob
        if curJob == 'done':
            return -1
        # print str(curJob)

        sock.sendall(str(process_data(curJob)))
        time.sleep(.01)
        # # print curJob
        # state = 'processing'
        # print str(len(curJob)) + "\n"
        # print "Got a new job: " + str(jobs_processed)

        # # elif state == 'processing':
        # val = process_data(curJob)
        # jobs_processed += 1
        # # print "Sending Job: " + str(jobs_processed)
        # # print "Sending Back: " + str(val)

        # sock.sendall(str(val))
        # state = 'requesting'



    sock.close()




def letter_count(data):
    chars = {chr(x + 97): 0 for x in range(26)}

    for c in data:
        if ord(c) < 97 or ord(c) > (97 + 26):
            pass
        else:
            chars[c.lower()] += 1
    # for x in sorted(chars.keys()):
    #     print str(x) + ": " + str(chars[x])


    return str(json.dumps(chars))

def process_data(data, fun = letter_count):
    return fun(data)




if __name__ == "__main__":
    main()
