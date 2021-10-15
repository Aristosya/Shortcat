from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CHOICES = (('male', 'Мужской пол'),('female', 'Женский пол'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    sexy = models.CharField('Пол', max_length=40, choices=CHOICES, default='Мужской пол')
    agree = models.BooleanField('Согласен получать спам на почту', default='True')

    def __str__(self):
        return f'Профайл пользователя : {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 512 or image.width > 512:
            resize = (512, 512)
            image.thumbnail(resize)
            image.save(self.img.path)


    class Meta:
        verbose_name = ' Профиль'
        verbose_name_plural = 'Профили'
