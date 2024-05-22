from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from pathlib import Path
from .errorHandler import errorHandler


@api_view(['GET'])
def getReadme(request):
    try:
        path = Path(__file__).resolve().parent
        file_location = f'{path}/resources/Help.md'

        response = FileResponse(open(file_location, 'rb'), status=200)

        response['Content-Type'] = 'text/md; charset=utf-8'
        return response
    except Exception as err:
        return errorHandler(err)
