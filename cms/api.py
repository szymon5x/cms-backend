from rest_framework import routers
from cms.cms.views import NewsViewset as NewsViewset
from cms.cms.views import CarViewset as CarViewset
from cms.cms.views import GeneralViewset as GeneralViewset
from cms.cms.views import ContactViewset as ContactViewset

router = routers.DefaultRouter()
router.register(r'news', NewsViewset)
router.register(r'car', CarViewset)
router.register(r'general', GeneralViewset)
router.register(r'contact', ContactViewset)
