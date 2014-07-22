from django.db import models
from django.forms import ModelForm
from uuid import uuid1

class Question(models.Model):
    text = models.CharField(max_length=100)
    flags = models.CharField(max_length=50, blank=True)
    def __unicode__(self):
        return self.text


class Event(models.Model): # Table with information about event
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)
    contact_mail = models.EmailField(max_length=254)
    date_begin = models.DateTimeField('data startu konferencji')
    date_end = models.DateTimeField('data konca konferencji')
    cost = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    questions = models.ManyToManyField(Question, through = 'EQLink')
    image = models.ImageField(upload_to='logos')
    def __unicode__(self):
        return self.name


class RQLink(models.Model):
    question  = models.ForeignKey(Question)
    registration = models.ForeignKey('Registration')
    answer = models.CharField(max_length=100)


class EQLink(models.Model):
    question = models.ForeignKey(Question)
    event = models.ForeignKey(Event)
    required = models.BooleanField()


class Domain(models.Model):  # Table with domains
    name = models.CharField(max_length=50)
    email_adress = models.EmailField(max_length=254)
    logo = models.ImageField(upload_to='logos')
    events = models.ManyToManyField(Event, blank=True)
    def __unicode__(self):
        return self.name


def UUID():
    return uuid1().hex

class Registration(models.Model):
    event = models.ForeignKey(Event) # Using class Event
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_email = models.EmailField(max_length=254)
    contact_phone = models.CharField(max_length=20)
    answers = models.ManyToManyField(Question, through = RQLink)
    uuid = models.CharField(max_length=32,default=UUID, editable = False)
    def __unicode__(self):
        rv = ''
        if self.last_name is not None: rv += self.last_name + " "
        if self.name is not None: rv += self.name + " "
        if self.event is not None: rv += ' - ' + self.event.name
        return rv 

class RegistrationForm:
    class Meta:
        model = Registration


class Email(models.Model):
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=1000)
    from_email = models.CharField(max_length=254)
    to_email = models.CharField(max_length=254)
    header = models.CharField(max_length=100)
    when = models.DateTimeField(auto_now_add = True, editable=False)
