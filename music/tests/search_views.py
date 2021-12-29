# import os
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Netflix.settings')
# import django
# from django.test import TestCase, Client
# from music.models import Movie, Actor
#
# django.setup()
#
# class Test_Movi_ViewSet(TestCase):
#     def setUp(self):
#         self.movie = Movie.objects.create(name='Test search')
#         self.actor = Actor.objects.create(Actor=self.movie, name='mains')
#         self.client = Client()
#
#     def test_search(self):
#         response = self.client.get('/movies/?search=Test')
#         data = response.data
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(data), 1)
#         self.assertEqual(data[0]['title'] == 'Test search')
