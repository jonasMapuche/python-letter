from pymongo import MongoClient
client = MongoClient('mongodb+srv://usuario:freedown@cluster0.28oko.azure.mongodb.net/stomach?retryWrites=true&w=majority')
print(client.list_database_names())
bd = client['stomach']
collection = bd['letter']
query = collection.find_one()
print(query)