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
