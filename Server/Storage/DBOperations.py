#http://tinydb.readthedocs.io
from tinydb import TinyDB, Query

def get(db, moduleCode):
    return db.search(Query().moduleCode == moduleCode)

def getAll(db):
    return db.all()

def getAllByProtocol(db, protocol):
    return db.search(Query().addr.protocol == protocol)

def add(db, data):
    if get(db, data[0]):
        print "module " + data[0] + " already exists, overwriting"
        rem(db, data[0])

    db.insert(
        {'moduleCode': data.pop(0),
         'addr':
            {'IP': data.pop(0),
             'port': data.pop(0),
             'protocol': data.pop(0)}
        })
    return 0

def rem(db, moduleCode):
    db.remove(Query().moduleCode == moduleCode)
    return 0

def remAll(db):
    db.purge()
    return 0
