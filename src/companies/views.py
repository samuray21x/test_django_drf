from rest_framework import generics

from django.http import HttpResponse
from companies.serializers import companies_inline_serializer
from companies.selectors import companies_all
import orjson

from companies import selectors, serializers


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = selectors.companies_all().prefetch_related('entities_objects', 'entities_objects__sub_objects')
    serializer_class = serializers.CompanySerializer

    def get_queryset(self):
        queryset = super(CompanyListCreateAPIView, self).get_queryset()
        if self.request.GET.get('fields'):
            fields = [field.strip() for field in self.request.GET['fields'].split(',')]
            if 'entities_objects' in fields:
                queryset = queryset.prefetch_related('entities_objects')
        return queryset


class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = selectors.companies_all().prefetch_related('entities_objects', 'entities_objects__sub_objects')
    serializer_class = serializers.CompanySerializer


def simple_companies_api(request):
    companies = companies_all().prefetch_related('entities_objects', 'entities_objects__sub_objects')
    result = orjson.dumps(companies_inline_serializer(companies))
    return HttpResponse(result, content_type='application/json')

