from django.db import models
import uuid


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + '\t\t\t' + \
               str(self.name) + '\t\t\t' + \
               str(self.email)


class Pixel(models.Model):
    class pixel_type(models.TextChoices):
        MAIN = 'tracking',
        CONVERSION = 'conversion',

    pixel = models.UUIDField(primary_key=True,
                             default=uuid.uuid4, editable=False, unique=True)
    pixel_type = models.CharField(max_length=20, choices=pixel_type.choices)
    client_id = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created) + '\t\t\t' + \
               str(self.client_id) + '\t\t\t' + \
               str(self.pixel)


class PixelPostData(models.Model):
    id = models.AutoField(primary_key=True)
    pixel = models.ForeignKey(Pixel,
                              on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(max_length=250)
    page = models.CharField(max_length=250, default=None)
    ip = models.CharField(max_length=50, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(id) + '\t\t\t' + \
               str(self.created) + '\t\t\t' + \
               str(self.user) + '\t\t\t' + \
               str(self.pixel)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)