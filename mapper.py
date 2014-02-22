from socket import *
import json
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.sendto('hello', ('127.0.0.1', 1055))

    while True:
        # i = raw_input("Message: ")
        # i = str(x)
        sock.sendto('Job Request', ('127.0.0.1', 1055))

        curJob = sock.recvfrom(4096)
        # print "Got a new job: " + str(curJob)

        val = process_data(curJob[0])
        # print "Sending Back: " + str(val)
        sock.sendto(str(val), ('127.0.0.1', 1055))


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
