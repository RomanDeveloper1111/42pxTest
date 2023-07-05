from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from back.models import Reducer
import os


class TestReducer(APITestCase):

    def setUp(self):
        image_path = os.path.join(settings.BASE_DIR,
                                  '../back/tests/images/example.jpg')
        self.image = SimpleUploadedFile(name='example.jpg', content=open(image_path, 'rb').read(),
                                        content_type='image/jpeg')

    def test_post_correct(self):
        url = reverse('resize_picture-list')

        data = {
            'image': self.image,
            'width': 250,
        }
        response = self.client.post(url, data, format='multipart')

        self.assertTrue(Reducer.objects.filter(natural_image_name='example.jpg').exists())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_bad(self):
        url = reverse('resize_picture-list')

        data = {
            'image': self.image,
        }
        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_2(self):
        data = {
            'image': self.image,
            'width': 0
        }
        url = reverse('resize_picture-list')
        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
