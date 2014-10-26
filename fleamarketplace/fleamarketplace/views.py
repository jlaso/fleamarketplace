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

def getImageList(pk):
    path = settings.BASE_DIR + '/fleamarketplace/' + settings.STATIC_URL
    return os.listdir(path + '/media/' + str(pk))

def index(request):
    markets = Market.objects.all() #filter(pk=request.market.id)
    products = Product.objects.all() #filter(market=request.market.id)

    #images = []

    for p in products:
        p.images = getImageList(p.id)

    response = render(
        request,
        'index.html',
        {
            'products': products,
            'markets': markets,
     #       'images': images,
        }
    )
    return response
