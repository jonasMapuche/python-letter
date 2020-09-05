from pymongo import MongoClient
import json, datetime
client = MongoClient('mongodb+srv://usuario:freedown@cluster0.28oko.azure.mongodb.net/stomach?retryWrites=true&w=majority')
print(client.list_database_names())
bd = client['stomach']
collection = bd['letter']
query = collection.find({'frase.name': {'$eq': 'lesson 1'}})
for doc in query:
    #lista = client['stomach'].get_collection('letter').find({}).limit(1)
    print('\n id: ', doc['_id'])
    for sub in doc['frase']:
        print(' frase: ', sub['name'])
        for ora in sub['oracao']:
            print('\nsujeito: ', ora['sujeito'])
            print('\npredicado: ', ora['predicado'])
    #print(lista)