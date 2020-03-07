from rest_framework import viewsets, status
from .models import Pet, Service, PetService, Room
from .serializers import PetSerializer, ServiceSerializer, PetServiceSerializer, RoomSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse 
from rest_framework.response import Response
from django.http import Http404
# import requests


class PetViewSet(viewsets.ModelViewSet):#ViewSet
    queryset = Pet.objects.all()
    serializer_class = PetSerializer




class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
"""    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""


class PetServiceViewSet(viewsets.ModelViewSet):
    queryset = PetService.objects.all()
    serializer_class = PetServiceSerializer

    def create(self, request, *args, **kwargs):
        # obj = get_object_or_404(Pet, pk = request.data['idPet'])
        # objService = get_object_or_404(Pet, pk = request.data['idService'])
        pkPet = request.data['idPet']
        pkService = request.data['idService']
        try:
            objPet = Pet.objects.get(pk=pkPet)
        except Pet.DoesNotExist:
            return Response({'detail':'pet not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            objService = Service.objects.get(pk=pkService)
        except Service.DoesNotExist:
            return Response({'detail':'service not found'}, status=status.HTTP_404_NOT_FOUND)
        obj2 = None
        try:
            obj2 = Room.objects.get(idPet =pkPet)#idPet=pkPet
        except Room.DoesNotExist:
            return Response({'detail':'Not allocated pet'}, status=status.HTTP_404_NOT_FOUND)


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        pkPet = request.data['idPet']
        pkService = request.data['idService']
        try:
            objPet = Pet.objects.get(pk=pkPet)
        except Pet.DoesNotExist:
            return Response({'detail':'pet not found'}, statuscmd=status.HTTP_404_NOT_FOUND)
        try:
            objService = Service.objects.get(pk=pkService)
        except Service.DoesNotExist:
            return Response({'detail':'service not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status = status.HTTP_200_OK)


class LodgeViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    def create(self, request, *args, **kwargs):
        pkPet = request.data['idPet']
        try:
            # obj = get_object_or_404(Pet, pk = request.data['idPet'])
            obj = Pet.objects.get(pk=pkPet)
        except Pet.DoesNotExist:
            return Response({'detail':'pet not found'}, status=status.HTTP_404_NOT_FOUND)
        # resp = requests.get('/api/v1/pets/'+pkPet)
        obj2 = None
        try:
            obj2 = Room.objects.get(idPet =pkPet)#idPet=pkPet
        except Room.DoesNotExist:
            print("not")
        if(obj2):
            return Response({'detail':'allocated pet'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        pkPet = request.data['idPet']
        try:
            # obj = get_object_or_404(Pet, pk = request.data['idPet'])
            obj = Pet.objects.get(pk=pkPet)
        except Pet.DoesNotExist:
            return Response({'detail':'pet not found'}, status=status.HTTP_404_NOT_FOUND)
        
        obj2 = None
        try:
            obj2 = Room.objects.get(idPet =pkPet)#idPet=pkPet
        except Room.DoesNotExist:
            print("not")
        if(obj2):
            return Response({'detail':'allocated pet'}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status = status.HTTP_200_OK)

# class AllocatedPetViewSet(viewsets.ModelViewSet):
   
#     def list(self, request,*args, **kwargs):
#         responsePet = requests.get('http://192.168.1.5:8000/api/v1/pets/').json()
#         responseAllo = requests.get('http://192.168.1.5:8000/api/v1/lodgement/').json()#mascotas alojadas
#         result = list()
#         raise Exception ('gol')
#         for i in range (len(responseAllo)):
#             for j in range (len(responsePet)):
#                 if responsePet[j]['id'] == responseAllo[i]['idPet']:
#                     result.append(responsePet[j])
#                     continue
        
#         serializer = self.get_serializer(data=result)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
        
#         return Response(serializer.data, status = status.HTTP_200_OK)


"""
para debuguear
# raise Exception({request.data['idPet']})
# return HttpResponse({request.data['idPet']})
"""     