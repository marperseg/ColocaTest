import requests
import json
import datetime
from rest_framework.response import Response
# from coloca.settings import DATABASE, COLLECTION
from .mongodb.dbconnect import DATABASE, COLLECTION
# from coloca import DATABASE, COLLECTION
from .errorHandler import errorHandler


def renumberJokes(jokeNumber):
    try:
        COLLECTION.update_many({'number': {"$gt": jokeNumber}}, {
            '$inc': {'number': -1}})
        return None
    except Exception as err:
        return errorHandler(err)


def jokeFromApi():
    apijoke = requests.get('https://api.chucknorris.io/jokes/random')
    apijokeJson = json.loads(apijoke.text)
    return apijokeJson['value']


def sendRes(data, message, stCode):
    toSend = {
        "message": message,
        "data": data
    }
    return Response(toSend, status=stCode)


def updateDB():
    try:
        latestJoke = COLLECTION.find().sort('_id', -1).limit(1)
        joke = latestJoke.next()
        print(joke['joke'])
        expireDate = joke['expire_date']

        # Check if joke exists and if it has expired
        if joke and expireDate <= datetime.datetime.now():  # Joke has expired
            print('Joke expired... Getting new one', expireDate)
            try:
                newJoke = jokeFromApi()
                result = jokeToDb(newJoke)
                return result
            except Exception as err:
                return errorHandler(err)
        else:

            message = f'Joke is still current, until: {expireDate}'
            print(message)
            return message
    except Exception as err:
        return errorHandler(err)


def jokeToDb(jokeToStore):
    # Get number of existing documents
    numberOfDocs = COLLECTION.count_documents({})
    print('numberOfDocs: ', numberOfDocs)
    joke = {
        # Number of joke (existing number + 1)
        "number": numberOfDocs + 1,
        # Date of issue
        "issued_date": datetime.datetime.now(),
        "expire_date": datetime.datetime.now() + datetime.timedelta(minutes=5),  # Adds 5 minutes
        "joke": jokeToStore
    }
    # Save joke in DataBase
    savedJoke = COLLECTION.insert_one(joke)
    # Remove id
    del joke['_id']
    return joke
