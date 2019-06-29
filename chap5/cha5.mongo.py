from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db['students']

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}


result = collection.find_one({'name':'Mike'})
print(type(result))
print(result)