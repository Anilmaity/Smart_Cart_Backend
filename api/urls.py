from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from api.apis import itemlist
from api.apis import Itemform


urlpatterns = [
    path('', views.index, name='index'),
    path('items/', itemlist.itemslist.as_view(), name='itemlist'),
    path('Itemform/', Itemform.Itemform.as_view(), name='itemform'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
