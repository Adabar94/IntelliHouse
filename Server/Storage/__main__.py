import sys
import socket
from DBOperations import *

def handleInput(data, db):
    if data == 'exit':
        return 1

    splited_data = data.split('|')
    actual = splited_data.pop(0)

    args_count = len(splited_data)

    if args_count == 0:
        if actual == 'getAll':
            return getAll(db)
        if actual == 'remAll':
            return remAll(db)

    elif args_count == 1:
        if actual == 'get':
            return get(db, splited_data.pop(0))
        if actual == 'getProtocol':
            return getAllByProtocol(db, splited_data.pop(0))
        if actual == 'rem':
            return rem(db, splited_data.pop(0))

    elif args_count == 4 and actual == 'add':
        return add(db, splited_data)

    throwIllegalMessage(data)

def throwIllegalMessage(message):
    print "Illegal message " + message

if __name__ == '__main__':
    db = TinyDB(sys.argv[1])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((sys.argv[2], int(float(sys.argv[3]))))

    while True:
        data, addr = sock.recvfrom(1024)
        output = handleInput(data, db)

        if output == 1:
            print 'Exiting ModulesStorage'
            sock.close()
            sys.exit()

        sock.sendTo(output, addr)
