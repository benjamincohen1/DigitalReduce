# from socket import *
import socket
import json
import time
def main():
    while True:
        try:
            jobs_processed = 0
            # sock = socket(AF_INET, SOCK_DGRAM)
            addr = '107.170.73.117'
            addr = 'localhost'
            TCP_IP = addr
            TCP_PORT = 5005
            BUFFER_SIZE = 1024

            # addr = 'localhost'
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((TCP_IP, TCP_PORT))

            sock.sendall('hello')
            fun = sock.recv(1024)

            exec fun
            # sock.sendto('hello', (addr, 1055))
            state = 'requesting'
            oldJob = -1
            # sock.sendall('Job Request')
            while True:

                sock.send('Job Request')

                curJob = sock.recv(BUFFER_SIZE)

                print "GOT A JOB"

                print curJob
                if curJob == 'done':
                    return -1
                    sock.close()
                    main()

                sock.sendall(str(process_data(curJob, hsh2)))
            sock.close()

        except:
            pass






def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


    return str(json.dumps(chars))

def process_data(data, fun):
    return fun(int(data))




if __name__ == "__main__":
    main()
