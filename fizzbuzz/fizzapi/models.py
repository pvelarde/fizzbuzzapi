from django.db import models

class FizzBuzz(models.Model):
    """
    Stores a single FizzBuzz entry
    """
    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
