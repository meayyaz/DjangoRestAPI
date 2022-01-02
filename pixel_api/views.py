from rest_framework import viewsets
from pixel_api.models import User, Pixel, PixelPostData
from pixel_api.serializers import UserSerializer, PixelSerializer, PixelPostDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PixelViewSet(viewsets.ModelViewSet):
    queryset = Pixel.objects.all()
    serializer_class = PixelSerializer


class PixelPostDataViewSet(viewsets.ModelViewSet):
    queryset = PixelPostData.objects.all()
    serializer_class = PixelPostDataSerializer

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        else:
            return request.META.get('REMOTE_ADDR')

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['ip'] = self.get_client_ip(request)
        return super(PixelPostDataViewSet, self).create(request, *args, **kwargs)

from rest_framework import viewsets
from pixel_api.models import Student
from pixel_api.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer