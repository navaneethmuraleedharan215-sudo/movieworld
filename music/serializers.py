from rest_framework import serializers

from music.models import song

class SongSerializer(serializers.ModelSerializer):


    class Meta:

        model = song

        fields = "__all__"

        read_only_fields = ["id","created_at","updated_at","created_by","movie"]