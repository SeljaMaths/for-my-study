from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from . serializers import employeeserializer
from . models import *
from . pagination import employee_pagination,custompagination,employee_limitpagination,employee_cursorpagination
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    data={
        'hello': 'welcome'
    }
    return JsonResponse(data)


@ api_view(['GET', 'POST'])
def fun_employee_details(request):
    if request.method == "GET":
        all_blogs = employee_details.objects.all()
        serializer = employeeserializer(all_blogs, many=True)
        pagination_class=employee_pagination
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = employeeserializer(data=request.data)
        pagination_class = employee_pagination

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class employee_details_class(APIView):

    def get(self, request,pk):
        all_blogs = employee_details.objects.get(pk=pk)
        serializer = employeeserializer(all_blogs)
        return Response(serializer.data)

    def put (self, request, pk):
        blog = employee_details.objects.get(pk=pk)
        serializer = employeeserializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def patch(self,request,pk):
        data = request.data
        obj = employee_details.objects.get(pk=data['id'])
        serializer = employeeserializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        blog = employee_details.objects.get(pk=pk)
        blog.delete()
        return Response()


from rest_framework.generics import ListAPIView


class employee_list(ListAPIView):
    queryset = employee_details.objects.all()
    serializer_class = employeeserializer
    # pagination_class = employee_pagination
    # pagination_class = employee_limitpagination
    # pagination_class = employee_cursorpagination
    pagination_class = custompagination