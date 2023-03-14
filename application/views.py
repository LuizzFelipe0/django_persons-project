from rest_framework.views import APIView
from .serializers import personSerializers
from .models import Person
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PersonList(APIView):

    def get(self, request):  # GET Request to retrieve all persons in the list
        persons = Person.objects.all()
        serialize = personSerializers(persons, many=True)
        return Response(serialize.data)

    def post(self, request):  # POST Request when data for a single person can be posted
        serializer = personSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonByID(APIView):  # It will be able to process multiple HTTP Requests

    # GET Request for a particular person by ID
    def get_object(self, pk):  
        return Person.objects.get(pk=pk)

    def get(self, request, pk):
        person_obj = self.get_object(pk)
        serialize_obj = personSerializers(person_obj)
        return Response(serialize_obj.data)
    
    def put(self, request, pk):  # PUT Request to update person's handler instance with new data, that has been passed along the request data
        person_obj = self.get_object(pk)
        serialize_obj = personSerializers(person_obj, data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(serialize_obj.data, status=status.HTTP_200_OK)
        return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):  # DELETE Request to get a especific person to be removed
        person_obj = self.get_object(pk)
        person_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
