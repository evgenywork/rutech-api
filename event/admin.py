from django.contrib import admin
from event.models import Event, EventConversation, EventMessage

# Register your models here.
admin.site.register(Event)
admin.site.register(EventConversation)
admin.site.register(EventMessage)
