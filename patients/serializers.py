from rest_framework import serializers

from .models import Person, Death
from concepts.models import Concept


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class DeathListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Death
        fields = '__all__'


class RaceListSerializer(serializers.Serializer):
    race_concept_id = serializers.IntegerField()
    race = serializers.SerializerMethodField('get_race')
    count = serializers.IntegerField()

    def get_race(self, race):
        race = Concept.objects.get(concept_id=race['race_concept_id']).concept_name
        return race


class EthnicityListSerializer(serializers.Serializer):
    ethnicity_concept_id = serializers.IntegerField()
    ethnicity = serializers.SerializerMethodField('get_ethnicity')
    count = serializers.IntegerField()

    def get_ethnicity(self, ethnicity):
        ethnicity = Concept.objects.get(concept_id=ethnicity['ethnicity_concept_id']).concept_name
        return ethnicity
