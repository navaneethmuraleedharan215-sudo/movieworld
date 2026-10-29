from rest_framework import serializers

from films.models import movie
from music.models import song

from music.serializers import SongSerializer

class MovieSerializer(serializers.ModelSerializer):

    track_count =serializers.SerializerMethodField(read_only=True)

    tracks=serializers.SerializerMethodField(read_only=True)


    class Meta:

        model = movie

        fields ="__all__"

        read_only_fields = ["id","created_at","updated_at","created_by"]


    def get_track_count(self,obj):

        return song.objects.filter(movie=obj).count()


    def get_tracks(self,obj):

        track_objects=song.objects.filter(movie=obj)

        serializer_instance=SongSerializer(track_objects,many=True)

        return serializer_instance.data