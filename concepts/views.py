from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Concept
from .serializers import ConceptListSerializer


# Create your views here.
# concept들 조회 (10개씩 pagination)
class ConceptListView(ListAPIView):
    queryset = Concept.objects.all()
    serializer_class = ConceptListSerializer
    pagination_class = PageNumberPagination


# 키워드 검색
class ConceptSearchView(APIView):
    def get(self, request, keyword):
        concept = get_object_or_404(Concept, concept_name=keyword)
        concept_serializer = ConceptListSerializer(concept)
        return Response(concept_serializer.data)