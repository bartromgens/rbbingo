from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import CardsView
from website.views import CheckFieldView
from website.views import HomeView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')), # the django-registration module
    url(r'^cards/', CardsView.as_view()),
    url(r'^field/toggle/(?P<field_id>[0-9]+)/$', CheckFieldView.as_view()),
)
