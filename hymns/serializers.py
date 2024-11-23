from rest_framework import serializers
from .models import Hymn, Verse, Line

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ('text',)


class VerseSerializer(serializers.ModelSerializer):
    lines = LineSerializer(many=True) # Lines are read-only from this perspective

    class Meta:
        model = Verse
        fields = ('type', 'lines')


class HymnSerializer(serializers.ModelSerializer):
    verses = VerseSerializer(many=True)

    class Meta:
        model = Hymn
        fields = ('name', 'number', 'author', 'year', 'favorite', 'verses')

    def create(self, validated_data):
        verses_data = validated_data.pop('verses')
        hymn = Hymn.objects.create(**validated_data) # Crea el himno primero

        for verse_data in verses_data:
            lines_data = verse_data.pop('lines')
            verse = Verse.objects.create(hymn=hymn, **verse_data)
            for line_data in lines_data:
                Line.objects.create(verse=verse, **line_data)

        return hymn
    

