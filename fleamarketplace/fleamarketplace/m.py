from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
import json as simplejson
import urlparse
from django.conf import settings
from django.db.models.sql.aggregates import Avg
#from _mysql import NULL
from django.shortcuts import render_to_response
from models import Market, Product
import settings
import os

def index(request):
    response = render(
        request,
        'm/index.html',
        {

        }
    )
    return response
