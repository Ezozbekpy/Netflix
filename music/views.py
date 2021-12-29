from django.contrib.postgres.search import TrigramSimilarity
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models.Actor import Actor
from .models.Movie import Movie
from .serializer import ActorSerializers, MovieSerializers


class ActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class MovieAPIView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializers = MovieSerializers(movie, many=True)
        return Response(data=serializers.data)

    def post(self, request):
        pass


class ActorAPIView(APIView):
    def get(self, request):
        actor = Actor.objects.all()
        serializers = ActorSerializers(actor, many=True)
        return Response(data=serializers.data)




class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['imdb', '-imdb']


    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Movie.objects.annotate(
                similarity=TrigramSimilarity('name', query)
            ).filter(similarity__gt=0.2).order_by('-similarity')
        return queryset

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        movi = self.get_queryset()
        movi = movi.order_by('-imdb')[:10]
        serializer = MovieSerializers(movi, many=True)
        return Response(data=serializer.data)












    # @action(detail=True, methods=['POST'])
    # def add_actor(self, requerst, *args, **kwargs):
    #     data = requerst.data
    #     name = data['name']
    #     year = data['year']
    #     imdb = data['imdb']
    #     genree = data['genree']
    #     actors = data['actors']
    #     actor = Actor.objects.create(
    #         name=name,
    #         year=year,
    #         imdb=imdb,
    #         genree=genree,
    #         actors=actors
    #     )
    #     movie = self.get_object()
    #     movie.actors.add(actor)
    #     movie.save()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)


