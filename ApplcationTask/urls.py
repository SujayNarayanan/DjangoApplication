"""
Definition of urls for ApplcationTask.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views


urlpatterns = [
    # Examples:
    url(r'^$',app.views.site,name='sites'),
    url(r'^sites$',app.views.site,name='sites'),
    url(r'^sites/(?P<id>\d+)/$',app.views.siteDetails,name='sitedetails'),
    url(r'^summary$',app.views.summary,name = 'summary'),
    url(r'^summary-average$',app.views.average,name = 'summary-average'),
    ]
