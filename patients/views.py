from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response 

from patients.models import Person
from patients.serializers import PersonListSerializer


# Create your views here.
# 데이터 10줄 조회
class TestView(APIView):
    def get(self, request):
        patients = Person.objects.all()[:10]
        patient_serializer = PersonListSerializer(patients, many=True)
        return Response(patient_serializer.data)


# 전체 환자 수
class PatientView(APIView):
    def get(self, request):
        patients_cnt = Person.objects.all().count()
        data = {
            'patients_cnt': patients_cnt
        }
        return Response(data)


# 성별 환자 수
class PatientGenderView(APIView):
    def get(self, request):
        # concept_id 8532는 여성
        female_patients_cnt = Person.objects.filter(gender_concept_id=8532).count()
        # concept_id 8507는 남성
        male_patients_cnt = Person.objects.filter(gender_concept_id=8507).count()
        data = {
            'female_patients_cnt': female_patients_cnt,
            'male_patients_cnt': male_patients_cnt
        }
        return Response(data)


# 인종별 환자 수
# 민족별 환자 수
# 사망 환자 수