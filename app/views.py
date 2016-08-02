"""
Definition of views.
"""

from django.shortcuts import render_to_response
from django.db.models import Avg
from app.models import *

def site(request):
    sites = Site.objects.all()
    return render_to_response('app/sitesTemplate.html',{'sites':sites})

def siteDetails(request,id):
    site = Site.objects.get(pk = id)
    siteDetails = site.sitedetails_set.all()
    return render_to_response('app/siteDetailsTemplate.html',{'site' : site,'siteDetails':siteDetails})

def summary(request):
    sites = Site.objects.all()
    for site in sites:
        siteDetails = site.sitedetails_set.all()
        site.aggAValue   = sum([detail.a_value for detail in siteDetails])
        site.aggBValue   = sum([detail.b_value for detail in siteDetails])
    return render_to_response('app/summaryTemplate.html',{'isSum':True,'sites':sites})


def average(request):
    sites = Site.objects.all()
    for site in sites:
        site.aggAValue = site.sitedetails_set.aggregate(Avg('a_value'))['a_value__avg']
        site.aggBValue = site.sitedetails_set.aggregate(Avg('b_value'))['b_value__avg']
    return render_to_response('app/summaryTemplate.html',{'isSum':False,'sites':sites})


