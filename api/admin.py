from django.contrib import admin

from api.models import EventRegistration, Event

admin.site.register(Event)
admin.site.register(EventRegistration)
