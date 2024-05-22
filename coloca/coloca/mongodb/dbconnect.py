import pymongo


print('Waiting for DataBase connection... ... ...')


def dbconnect():
    uri = "mongodb+srv://marperseg:colocatest@cluster0.olevbkq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Connect to MongoDB
    try:
        client = pymongo.MongoClient(uri)
        print("DB connected successfully...")
        # Send a ping to confirm a successful connection
        # client.admin.command('ping')
        # print("DB connected successfully...")
    except Exception as e:
        print(e, type(e).__name__)

    DataBase = client['coloca']
    Collection = DataBase['jokes']

    return DataBase, Collection


[DATABASE, COLLECTION] = dbconnect()
