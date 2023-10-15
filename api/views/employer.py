from elasticsearch_dsl import Q

from django.core.exceptions import ObjectDoesNotExist
from core.exceptions import ClientError

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.exceptions import SerializerValidationError

from api.models import Employer
from api.documents import EmployerDocument
from api.serializers import EmployerDocumentSerializer, EmployerSerializer


__all__ = ['EmployerListCreate', 'EmployerById']

class CustomPaginator(PageNumberPagination):
    page_size = 15  # Number of items per page
    page_size_query_param = 'page_size'  # Query parameter to change page size (optional)
    max_page_size = 100  # Maximum page size (optional)

class EmployerListCreate(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = EmployerDocumentSerializer
    queryset = EmployerDocument.search()
    pagination_class = CustomPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        if 'query' in params and params.get('query') is not None:
            query = params.get('query')

            # Define the fields you want to search in
            search_fields =  ['company', 'industries', 'country_territory']

            # Initialize a list to hold Q objects for each field
            field_queries = []

            # Loop trough search_fields
            for field in search_fields:
                field_query = Q("wildcard", **{field: f"*{query}*"})
                field_queries.append(field_query)

            # Check searches using OR operator
            q = Q("bool", should=field_queries, minimum_should_match=1)

            # Fire the search
            search = EmployerDocument.search().query(q)
            queryset = search.execute()

        return queryset

    def get(self, request, *args, **kwargs):      
        # call default super function of get
        response = super().get(request,  *args, **kwargs)
        data = response.data

        return Response({
            "status": "success", 
            "data": data
        }, 200)
            

    def post(self, request, *args, **kwargs):
        try:
            data =request.data
            serializer = EmployerSerializer(data = data)
            serializer.is_valid()
            serializer.save()

            return Response({
                "status": "success", 
                "data": serializer.data
            }, 200)
            
        except SerializerValidationError as err:
            return Response({
                "status": "fail", 
                "errors": err.detail
            }, 400)
        
class EmployerById(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    lookup_field = 'id'

    def get_object(self):
        try:
          obj = self.queryset.all().get(id = self.kwargs['id'])
          return obj       
        
        except ObjectDoesNotExist as err:   
            raise ClientError(code=404, detail='Resource not found.')
        
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data

        return Response({
            "status": "success",
            "data": data,
        }, 404)
    
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            data = response.data

            return Response({
                "status": "success",
                "data": data,
            }, 404)
        
        except SerializerValidationError as err:
            return Response({
                "status": "fail", 
                "errors": err.detail
            }, 400)
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        data = response.data

        return Response({
            "status": "success",
            "data": data,
        }, 404)


