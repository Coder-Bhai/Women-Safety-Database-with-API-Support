from django.shortcuts import render,HttpResponse
import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import utc
from .models import PlaceDetails
from .serializers import DetailsSerializer



# serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#tutorial-2-requests-and-responses


class DatabaseList(APIView):
    def get(self,request):
        obj = PlaceDetails.objects.all()
        serializer = DetailsSerializer(obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DetailsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Create your views here.
def index(request):
    obj = PlaceDetails.objects.all()
    params = {
        'total_records':len(obj)
    }
    return render(request,"database/index.html",params)

def license(request):
    return render(request,"database/license.html")

def table(request):
    obj = PlaceDetails.objects.all()
    params = {
        'time': datetime.datetime.utcnow().replace(tzinfo=utc),
        'data':obj
    }
    return render(request,"database/tables.html",params)