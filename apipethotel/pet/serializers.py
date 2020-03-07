from .models import Pet, Service, PetService, Room
from rest_framework import serializers

class PetSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Pet
        # fields = '__all__'
        fields = ['id','name','race','gender','age','weight',]




class ServiceSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Service
        # fields = '__all__'
        fields = ['id','name','description',]


class PetServiceSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PetService
        # fields = '__all__'
        fields = ['id','idPet','idService','fecha','hora',]



class RoomSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Room
        # fields = '__all__'
        fields = ['id','idPet','roomNumber','floor','description']
