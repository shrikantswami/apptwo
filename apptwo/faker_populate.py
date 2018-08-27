import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','apptwo.settings')
import django
django.setup()
import random
from image.models import Topic,data
from faker import Faker

fake = Faker()
topics =['search','news','game']

def add_topic():
    t=Topic.objects.get_or_create(webname=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for _ in range(n):
        top = add_topic()
        fake_date=fake.date()
        fake_url=fake.url()

        webnm= data.objects.get_or_create(name=top,date=fake_date,url=fake_url)[0]

if __name__=='__main__' :
    print('populating ')
    populate(10)
    print("Populating Completed")
