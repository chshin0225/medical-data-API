from django.shortcuts import get_object_or_404
from django.db.models import Count, F, Subquery

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import VisitOccurrence, ConditionOccurrence, DrugExposure
from .serializers import VisitListSerializer, ConditionOccurrenceListSerializer, DrugExposureListSerializer, VisitTypeListSerializer, VisitGenderSerializer, VisitRaceSerializer, VisitEthnicitySerializer
from patients.models import Person

# Create your views here.
# visit list 조회 (10개씩 pagination)
class VisitListView(ListAPIView):
    queryset = VisitOccurrence.objects.all().order_by('visit_occurrence_id')
    serializer_class = VisitListSerializer
    pagination_class = PageNumberPagination


# condition occurrence list 조회 (10개씩 pagination)
class ConditionOccurrenceListView(ListAPIView):
    queryset = ConditionOccurrence.objects.all().order_by('visit_occurrence_id')
    serializer_class = ConditionOccurrenceListSerializer
    pagination_class = PageNumberPagination


# drug exposure list 조회 (10개씩 pagination)
class DrugExposureListView(ListAPIView):
    queryset = DrugExposure.objects.all().order_by('visit_occurrence_id')
    serializer_class = DrugExposureListSerializer
    pagination_class = PageNumberPagination


# 방문 유형별 방문 수
class VisitTypeView(APIView):
    def get(self, request):
        visit_cnt_by_type = VisitOccurrence.objects.values('visit_concept_id').order_by('visit_concept_id').annotate(count=Count('visit_concept_id'))
        visit_type_serializer = VisitTypeListSerializer(visit_cnt_by_type, many=True)
        return Response(visit_type_serializer.data)


# 성별 방문 수
class VisitGenderView(APIView):
    def get(self, request):
        visit_cnt_by_gender = VisitOccurrence.objects.values('person__gender_concept_id').annotate(gender=F('person__gender_concept_id')).order_by('gender').annotate(count=Count('gender')).values('gender', 'count')
        visit_gender_serializer = VisitGenderSerializer(visit_cnt_by_gender, many=True)
        return Response(visit_gender_serializer.data)


# 인종별 방문 수
class VisitRaceView(APIView):
    def get(self, request):
        visit_cnt_by_race = VisitOccurrence.objects.values('person__race_concept_id').annotate(race=F('person__race_concept_id')).order_by('race').annotate(count=Count('race')).values('race', 'count')
        visit_race_serializer = VisitRaceSerializer(visit_cnt_by_race, many=True)
        return Response(visit_race_serializer.data)


# 민족별 방문 수
class VisitEthnicityView(APIView):
    def get(self, request):
        visit_cnt_by_ethnicity = VisitOccurrence.objects.values('person__ethnicity_concept_id').annotate(ethnicity=F('person__ethnicity_concept_id')).order_by('ethnicity').annotate(count=Count('ethnicity')).values('ethnicity', 'count')
        visit_ethnicity_serializer = VisitEthnicitySerializer(visit_cnt_by_ethnicity, many=True)
        return Response(visit_ethnicity_serializer.data)


# 방문시 연령대(10세 단위) 방문 수