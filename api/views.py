import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    person = {
        'name': 'maxim k',
        'current_day': 'Thursday',
        'utc_time': datetime.datetime.now()
    }
    return Response(person)