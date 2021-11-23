from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FizzBuzz
from .serializers import FizzBuzzSerializer

class FizzBuzzView(APIView):
    """
    Endpoint at /fizzbuzz

    GET returns a list of all fizzbuzz messages

    POST returns new entry data
    
    'message' - (optional) empty if not included
    """
    def get(self, request, format=None):
        """
        Get and return all FizzBuzz objects
        """
        fizzList = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Store 'message' if any and get useragent
        """
        message = ''
        if 'message' in request.data:
            message = request.data['message']
        useragent = request.META['HTTP_USER_AGENT']
        serializerData = {
            'message': message,
            'useragent': useragent
        }
        serializer = FizzBuzzSerializer(data=serializerData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FizzBuzzDetail(APIView):
    """
    Endpoint at /fizzbuzz/<int>

    GET returns the info of a FizzBuzz object with id <int>
        if not found return 404
    """
    def get_object(self, pk):
        try:
            return FizzBuzz.objects.get(pk=pk)
        except FizzBuzz.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        fizzBuzz = self.get_object(pk)
        serializer = FizzBuzzSerializer(fizzBuzz)
        return Response(serializer.data, status=status.HTTP_200_OK)
