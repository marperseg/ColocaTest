
from rest_framework.decorators import api_view
# from django.http import HttpRequest as request
import requests
from . import controllers


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def jokesRouter(request):
    match request.method:
        case 'GET':
            return controllers.randomjoke(request)
        case 'POST':
            return controllers.newjoke(request)
        case 'PATCH':
            return controllers.updatejoke(request)
        case 'DELETE':
            return controllers.deletejoke(request)
