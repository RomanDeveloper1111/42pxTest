from django.db import models


class Reducer(models.Model):
    image = models.FileField(upload_to='', verbose_name='image')
    natural_image_name = models.CharField(max_length=128,  unique=True, verbose_name='not_hashable_name')

    class Meta:
        verbose_name = 'reducer'
        verbose_name_plural = 'reducers'

    def __str__(self):
        return str(self.image)



