from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from registration.forms import RegistrationFormUniqueEmail

from website.views import CardView
from website.views import CheckFieldView
from website.views import EventsView
from website.views import GamesView
from website.views import HomeView
from website.views import JoinGameView
from website.views import NewEventView
from website.views import EditEventView
from website.views import NewGameView
from website.views import RBBingoNewRegistrationView


urlpatterns = patterns(
    '',
    url(r'^$', login_required(HomeView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/', RBBingoNewRegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'), # include before the simple.urls to override register url
    url(r'^accounts/', include('registration.backends.simple.urls')), # the django-registration module
    url(r'^card/(?P<card_id>[0-9]+)/$', login_required(CardView.as_view())),
    url(r'^games/$', login_required(GamesView.as_view())),
    url(r'^game/new/$', login_required(NewGameView.as_view())),
    url(r'^events/$', login_required(EventsView.as_view())),
    url(r'^event/new/$', login_required(NewEventView.as_view())),
    url(r'^event/edit/(?P<id>[0-9]+)/$', login_required(EditEventView.as_view())),
    url(r'^field/toggle/(?P<field_id>[0-9]+)/$', login_required(CheckFieldView.as_view())),
    url(r'^game/join/(?P<game_id>[0-9]+)/$', login_required(JoinGameView.as_view())),
)
