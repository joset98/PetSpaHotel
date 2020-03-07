from django.db import models

DATE_INPUT_FORMATS = ['%d-%m-%Y']
# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length = 255)
    race = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 1)
    age = models.IntegerField()
    weight = models.FloatField()
    
    def __str__(self):
        return "%s %s" % (self.name, self.race)

class Service(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)

    def __str__(self):
        return "%s" % (self.name)

class PetService(models.Model):
    fecha = models.DateField(max_length=50)
    idPet = models.ForeignKey(Pet, on_delete=models.CASCADE)    
    idService = models.ForeignKey(Service, on_delete=models.CASCADE)
    hora = models.DurationField(max_length=50)
    # hora = models.DurationField¶(max_length=50, default=get_default_my_hour) 
    # idService = models.IntegerField()
    # idPet = models.IntegerField()


class Room(models.Model):
    floor = models.IntegerField()
    roomNumber = models.IntegerField()
    # idPet = models.IntegerField()
    idPet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    description = models.CharField(max_length = 255)