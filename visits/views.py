from django.shortcuts import get_object_or_404
from django.db.models import Count, F, Subquery

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import VisitOccurrence
from .serializers import VisitTypeListSerializer, VisitGenderSerializer
from patients.models import Person

# Create your views here.
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


# 민족별 방문 수


# 방문시 연령대(10세 단위) 방문 수