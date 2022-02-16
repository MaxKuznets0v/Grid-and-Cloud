# make a server for speed comparison
# locally through mongodb docs
# cloud through mongodb.com/cloud
# docker container
# to fill data into db implement some generator
# first_name, second_name, age, gender, phone, country, occupation, education
import pymongo
import seed
import random
from flask import Flask, request
import time

app = Flask(__name__)


def generate(num):
    res = list()
    for i in range(num):
        elem = {'first_name': random.choice(seed.first_names),
                'second_name': random.choice(seed.second_names),
                'age': random.randint(18, 99),
                'gender': 'Male' if random.randint(0, 1) else 'Female',
                'phone': '+7' + str(random.randint(1000000000, 9999999999)),
                'country': random.choice(seed.countries),
                'occupation': random.choice(seed.occupations),
                'education': random.choice(seed.educations)}
        res.append(elem)
    
    if num == 1:
        return res[0]
    return res


def fill_up():
    element = generate(1)
    local = pymongo.MongoClient('localhost', 27017)
    db = local['Database']
    col = db['clients']
    col.insert_one(element)

    cloud = pymongo.MongoClient('mongodb+srv://albert:hYDNdH56R0cyL8fN@cluster0.1kkjx.mongodb.net/Database?retryWrites=true&w=majority')
    db = cloud['Database']
    col = db['clients']
    col.insert_one(element)

    docker = pymongo.MongoClient('localhost', 27001)
    db = docker['Database']['clients']
    db.insert_one(element)


def make_move(db, insert: bool):
    start = time.time()
    if insert:
        db.insert_many(generate(size))
    else:
        db.delete_many({})
    return time.time() - start
    

@app.route('/eval', methods=['POST', 'DELETE'])
def eval():
    ins = request.method == 'POST'
    local_client = pymongo.MongoClient('localhost', 27017)
    local_db = local_client['Database']['clients']
    l_time = make_move(local_db, ins)

    web_client = pymongo.MongoClient('mongodb+srv://albert:hYDNdH56R0cyL8fN@cluster0.1kkjx.mongodb.net/Database?retryWrites=true&w=majority')
    web_db = web_client['Database']['clients']
    w_time = make_move(web_db, ins)

    docker_client = pymongo.MongoClient('localhost', 27001)
    docker_db = docker_client['Database']['clients']
    d_time = make_move(docker_db, ins)

    return ({"l_time": l_time, "w_time": w_time, "d_time": d_time}, 200)


if __name__ == '__main__':
    size = 1000
    fill_up()
    app.run()
