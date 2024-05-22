from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests
import json
import datetime
from pymongo import ReturnDocument
from .utils import jokeFromApi, sendRes, renumberJokes, jokeToDb, updateDB
from .errorHandler import errorHandler
from django.conf import settings
from .mongodb.dbconnect import DATABASE, COLLECTION


# @api_view(['GET'])
def randomjoke(request):
    try:
        # Get params to select source
        params = request.query_params
        source = params.get('source', '')

        # Source is External API
        if source == 'Chuck':
            print(source)
            joke = jokeFromApi()
            message = 'Random joke from external API'
            stCode = 200

        # Source is DataBase
        else:
            # Get random joke from DB.
            dbJokes = COLLECTION.aggregate([{'$sample': {'size': 1}}])
            joke = dbJokes.next()
            # Delete _id
            del joke['_id']
            # Set message and status code
            message = 'Random joke from internal DB'
            stCode = 200
            # Send response
        return sendRes(joke, message, stCode)
    # Capture exeptions and send errors
    except Exception as err:
        return errorHandler(err)


# @ api_view(['POST'])
def newjoke(request):
    try:
        # Get request body data
        body = request.data
        jokeBody = body.get('joke', '')
        print(jokeBody)

        # Check if body is correct
        if jokeBody:
            joke = jokeToDb(jokeBody)

            # Set message and status code
            message = 'Joke successfully added to DB.'
            stCode = 201

            # Send response
            return sendRes(joke, message, stCode)

        # If body is not correct, send error
        else:
            message = 'Please provide a joke in the request body.'
            return errorHandler(0, message)

    # Capture exeptions and send errors
    except Exception as err:
        return errorHandler(err)


# @ api_view(['PATCH'])
def updatejoke(request):
    try:
        # Get request body data
        body = request.data
        jokeBody = body.get('joke', '')
        jokeNumber = body.get('joke number', '')

        # Get number of documents from DB
        numberOfDocs = COLLECTION.count_documents({})

        # Check if body and number exists
        if jokeBody and jokeNumber:
            # Check if number is correct
            if type(jokeNumber) is int and jokeNumber <= numberOfDocs and jokeNumber > 0:

                # Update joke
                updatedJoke = COLLECTION.find_one_and_update({'number': jokeNumber},
                                                             {'$set': {
                                                                 "joke": jokeBody}},
                                                             return_document=ReturnDocument.AFTER)
                # Remove id
                del updatedJoke['_id']

                # Set message and status code
                message = 'Joke successfully upadted in DB. New document:'
                stCode = 200

                # Send response
                return sendRes(updatedJoke, message, stCode)

            # If joke number is not correct, send error
            else:
                message = f'Joke number is invalid. Pleas provide an integer between 1 and {numberOfDocs}'
                return errorHandler(0, message)
        # If body is not correct, send error
        else:
            message = 'Please provide a the text to update the joke and a valid joke number.'
            return errorHandler(0, message)

    # Capture exeptions and send errors
    except Exception as err:
        return errorHandler(err)


# @ api_view(['DELETE'])
def deletejoke(request):

    try:
        # Get joke number to delete
        params = request.query_params
        jokeNumber = params.get('joke_number', '')

        # Check if the parameter is numeric
        if jokeNumber.isnumeric():
            jokeNumber = int(jokeNumber)

        # Get number of documents from DB
        numberOfDocs = COLLECTION.count_documents({})

        # Check if number is correct
        if type(jokeNumber) is int and jokeNumber <= numberOfDocs and jokeNumber > 0:
            print(jokeNumber)
            deletedJoke = COLLECTION.find_one_and_delete(
                {'number': jokeNumber})
            print(deletedJoke)

            # Check if joke exists
            if deletedJoke:

                # Remove id
                del deletedJoke['_id']

                # Set message and status code
                message = 'Joke successfully deleted in DB.'
                stCode = 204

                renumberJokes(jokeNumber)
                # Send response
                return sendRes(deletedJoke, message, stCode)
            # Joke number is not in the DB
            else:
                message = f'Joke not found'
                return errorHandler(0, message)
        else:
            message = f'Joke number is invalid. Pleas provide an integer between 1 and {numberOfDocs}'
            return errorHandler(0, message)
    # Capture exeptions and send errors
    except Exception as err:
        return errorHandler(err)
