import json
from pymongo import MongoClient

client = MongoClient()
db = client['bookstore']
collection = db['books']

all_docs = collection.find()
one_doc = all_docs[1]
pretty_json = json.dumps(one_doc, indent=4, default=str)
print(pretty_json)

count = collection.count_documents({})
print(f'Число записей в базе данных: {count}')

def find():
    #query = {"price" : {"$gt" : 20, "$lte" : 40}}
    query = {"in_stock" : {"$lte" : 19}}
    #query = {"title" : {"$gte" : "A", "$lt" : "N"}}
    #query = {"description" : {"$regex" : "[Ee]rotic"}}
    # query = {"description" : {"$regex" : "[Ee]rotic | [Oo]nly"}}

    projection = {"_id" : 0, "title" : 1}

    books = db.books.find(query, projection)
    
    num_books = 0
    for i in books:
        print(i)
        num_books += 1
        
    print('Число книг: %d' % num_books)

    for a in books:
        print(a)
        
if __name__ == '__main__':
    find()
