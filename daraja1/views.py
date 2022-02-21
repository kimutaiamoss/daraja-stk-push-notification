from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
import logging
import json
from django.urls import reverse
from .models import Log
# Create your views here.
#getting logger instance
logger = logging.getLogger('daraja')



def index(request):
    logs = Log.objects.all()[:50]
    page_context = {
        'logs': logs
    }
    return render(request, 'index.html', context=page_context)

def clear_logs(request):
    '''
    clearing  application logs
    '''
    Log.objects.all().delete()
    home_url = reverse('index')
    response = '<p>Logs cleared.</p> <a href="' + home_url + '">Back Home</a>'
    
    return HttpResponse(response)


