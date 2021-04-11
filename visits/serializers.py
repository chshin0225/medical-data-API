from rest_framework import serializers

from concepts.models import Concept


class VisitTypeListSerializer(serializers.Serializer):
    visit_concept_id = serializers.IntegerField()
    visit_type = serializers.SerializerMethodField('get_visit_type')
    count = serializers.IntegerField()

    def get_visit_type(self, visit_type):
        visit_type = Concept.objects.get(concept_id=visit_type['visit_concept_id']).concept_name
        return visit_type


class VisitGenderSerializer(serializers.Serializer):
    gender = serializers.SerializerMethodField('get_gender')
    count = serializers.IntegerField()

    def get_gender(self, gender):
        gender = Concept.objects.get(concept_id=gender['gender']).concept_name
        return gender


class VisitRaceSerializer(serializers.Serializer):
    race = serializers.SerializerMethodField('get_race')
    count = serializers.IntegerField()

    def get_race(self, race):
        race = Concept.objects.get(concept_id=race['race']).concept_name
        return race


class VisitEthnicitySerializer(serializers.Serializer):
    ethnicity = serializers.SerializerMethodField('get_ethnicity')
    count = serializers.IntegerField()

    def get_ethnicity(self, ethnicity):
        ethnicity = Concept.objects.get(concept_id=ethnicity['ethnicity']).concept_name
        return ethnicity