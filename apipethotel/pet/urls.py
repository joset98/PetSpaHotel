from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from pet import views
from pet.views import *

router = DefaultRouter()
router.register(r'pets', viewset=PetViewSet)

router.register(r'services', viewset=ServiceViewSet)
router.register(r'service/petservices', viewset=PetServiceViewSet)
router.register(r'lodgement', viewset=LodgeViewSet)


# urlpatterns = router.urls
urlpatterns = [
    url (r'', include(router.urls)),
    # url (r'allocated_pet', AllocatedPetViewSet.as_view ),
    # url (r'^pets/$', PetList.as_view(), name = 'pets' )
 
]