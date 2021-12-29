import os

from django.db import migrations

from music.models import Movie
from music.serializer import MovieSerializers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Netflix.settings')
from django.test import TestCase, Client
import django

django.setup()

class Test_MovieViewSet(TestCase):
    def setUp(self):
        self.Movie = Movie.objects.create(name='new-5', year='2000-10-02', imdb='5', genree='Comedy', )
        self.Movie = Movie.objects.create(name='new-6', year='2000-10-02', imdb='4', genree='Comedy', )
        self.client = Client()
        self.Movie_all = Movie.objects.all()


    def test_imdb(self):
        response = self.client.get('/movies/?ordering=-imdb')
        all = self.Movie_all.order_by('-imdb')
        serializer = MovieSerializers(all, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    # def test_search(self):
    #     response = self.client.get('/movies/?search=new-5')
    #     all = Movie.objects.filter(name__icontains='new-5')
    #     serializer = MovieSerializers(all, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_get_all_movie(self):
    #     response = self.client.get('/movies/')
    #     all = Movie.objects.all()
    #     serializer = MovieSerializers(all, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, 200)
    #     print(response.data)
