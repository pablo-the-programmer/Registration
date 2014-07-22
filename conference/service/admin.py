from django.contrib import admin
from service.models import Domain
from service.models import Event
from service.models import Registration
from service.models import Question
from service.models import Email, EQLink


class EQLinkInline(admin.TabularInline):
    model = EQLink


class EventAdmin(admin.ModelAdmin):
    inlines = [EQLinkInline,]


#class QuestionAdmin(admin.ModelAdmin):
#    inlines = [QELinkInline,]


admin.site.register(Domain)
admin.site.register(Event, EventAdmin)
admin.site.register(Registration)
admin.site.register(Question)
admin.site.register(Email)
