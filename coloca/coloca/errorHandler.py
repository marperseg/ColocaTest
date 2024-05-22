from rest_framework.response import Response
from coloca.settings import BASE_URL


def errorHandler(error, *description):
    if description:
        errToSend = {
            "error": 'Bad Request',
            "message": description,
        }
        stCode = 400
    elif type(error).__name__ == 'ConnectionError':
        print('Something went wrong...', type(error).__name__)

        errToSend = {
            "error": type(error).__name__,
            "message": 'Resource not found...',
        }
        stCode = 404
    response = sendError(errToSend, stCode)
    return response


def sendError(error, stCode):
    error['help'] = f'For further information about the app please go to: GET {BASE_URL}/chuckjokesapi/v0/help'
    print(error, stCode)
    return Response(error, status=stCode)
