from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import VisitOccurrence
from .serializers import VisitTypeListSerializer

# Create your views here.
# 방문 유형별 방문 수
class VisitTypeView(APIView):
    def get(self, request):
        visit_cnt_by_type = VisitOccurrence.objects.values('visit_concept_id').order_by('visit_concept_id').annotate(count=Count('visit_concept_id'))
        visit_type_serializer = VisitTypeListSerializer(visit_cnt_by_type, many=True)
        return Response(visit_type_serializer.data)