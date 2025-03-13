from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Datatype(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Dataplan(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    datatype = models.ForeignKey(Datatype, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Permode(models.Model):
    network = models.ForeignKey(Network, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=124)
    datatype = models.ForeignKey(Datatype, on_delete=models.SET_NULL, blank=True, null=True)
    dataplan = models.ForeignKey(Dataplan, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name