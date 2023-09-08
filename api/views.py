import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    person ={
        "slack_name": "Maxim K",
        "current_day": datetime.datetime.today().strftime("%A"),
        "utc_time": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": "backend",
        "github_file_url": "https://github.com/Ishiukwu/zuri_backend/tree/main/api",
        "github_repo_url": "https://github.com/Ishiukwu/zuri_backend",
        "status_code": 200,
   }
    return Response(person)