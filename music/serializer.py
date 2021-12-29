from rest_framework import serializers
from .models.Actor import Actor
from .models.Movie import Movie
from rest_framework.exceptions import ValidationError
from datetime import date

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'gender')

    def validate_birthdate(self, value):
        if value >= date(1950,1,1):
            return ValidationError


class MovieSerializers(serializers.ModelSerializer):
    actors = ActorSerializers(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genree', 'actors')
