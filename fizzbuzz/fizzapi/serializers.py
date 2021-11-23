from .models import FizzBuzz
from rest_framework import serializers

class FizzBuzzSerializer(serializers.ModelSerializer):
    """
    Serializer handles all fields in FizzBuzz specified below
    """
    class Meta:
        model=FizzBuzz
        fields=('fizzbuzz_id', 'useragent', 'creation_date', 'message')
