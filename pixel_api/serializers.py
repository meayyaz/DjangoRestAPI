from rest_framework import serializers

from .models import User
from .models import Pixel
from .models import PixelPostData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'created')


class PixelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pixel
        fields = ('pixel', 'client_id', 'pixel_type', 'created')


class PixelPostDataSerializer(serializers.HyperlinkedModelSerializer):
    created = serializers.CharField(required=False)
    user = serializers.CharField(required=True)
    page = serializers.CharField(required=True)
    ip = serializers.CharField(required=False)
    pixel = serializers.PrimaryKeyRelatedField(queryset=Pixel.objects.all(), many=False)
    serializers.IntegerField
    class Meta:
        model = PixelPostData
        fields = ('id', 'pixel', 'user', 'page', 'ip', 'created')


from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    grade = serializers.IntegerField(required=False)
    phone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'grade', 'phone','email')

