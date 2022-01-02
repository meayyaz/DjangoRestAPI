from django.test import TestCase

# Create your tests here.

from pixel_api.models import Hero
from pixel_api.serializers import HeroSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

hero = Hero(name='SuperMan3',alias="SuperManManMan")
hero.save()

serializer = HeroSerializer(hero)
print(serializer.data)
