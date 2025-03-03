from django.db import models

# Create your models here.

class Network (models.Model):
    name = models.CharField(max_length=40)
 
    def __str__(self):
        return self.name


class DataType (models.Model):
    datatype = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ReqData (models.Model):
    name = models.CharField(max_length=124)
    network = models.ForeignKey(Network, on_delete=models.SET_NULL, blank=True, null=True)
    datatype = models.ForeignKey(DataType, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name