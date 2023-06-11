from django.shortcuts import render
from .models import apiModel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import serializeClass
# Create your views here.

class apiClassView(APIView):
    def get(self,request):
        obj=apiModel.objects.all()
        serobj=serializeClass(obj,many=True)   # here many=True is used for the multiple records serialization
        return Response(serobj.data)

    def post(self,request):
        serobj=serializeClass(data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        obj=apiModel.objects.get(id=id)
        serobj=serializeClass(obj,data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        obj=apiModel.objects.get(id=id)
        serobj=serializeClass(obj,data=request.data,partial=True)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        obj=apiModel.objects.get(id=id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)