from django.http import JsonResponse
from datetime import datetime

def ping(request):
    data = {'dateTime': datetime.now()}
    return JsonResponse(data)
