from datetime import datetime, timedelta
from django.http import JsonResponse

# Create your views here.
def getData(request):
    slack_name = request.GET.get('slack_name', 'Maxim_K')
    track = request.GET.get('track', 'backend')

    current_day = datetime.now().strftime("%A")
    utc_time = (datetime.utcnow() + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ")

    github_file_url = "https://github.com/Ishiukwu/zuri_backend/tree/main/myapp"
    github_repo_url = "https://github.com/Ishiukwu/zuri_backend"

    person = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(person)




