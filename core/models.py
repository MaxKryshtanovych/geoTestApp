from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    balance = models.FloatField(null=False, blank=False, default=0.0)


class Operation(models.Model):
    client_id = models.IntegerField()
    summary = models.FloatField(null=False, blank=False, default=0.0)
    desc = models.TextField()
    op_date = models.DateTimeField(auto_now_add=True)
