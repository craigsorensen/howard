import json
import os

SCRIPT_EXC_DIR = os.path.dirname(os.path.realpath(__file__))
database = "{0}/database.json".format(SCRIPT_EXC_DIR)

#db = '{"shows": [["mon", "oct", "1"],["mon","oct","8"],["mon","oct","15"]]}'
show = ["mon","oct","22"]
with open(database, 'r') as f:
    print("read lock file")
    db = f.read()


db = json.loads(db)
#print(db)
print(len(db['shows']))

if show not in db['shows']:
    db['shows'].append(show)
    print('sending push notification')

print(len(db['shows']))

with open(database, 'w+') as f:
    print("writing lock file")
    f.write(json.dumps(db))