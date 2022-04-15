from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from api.apis import itemlist
from api.apis import Itemform
from api.apis import Cart_list
from api.apis import CartForm
from api.apis import Cart_login
from api.apis import Cart_logout
from api.apis import Updated_cart__location



urlpatterns = [
    path('', views.index, name='index'),
    path('items/', itemlist.itemslist.as_view(), name='itemlist'),
    path('Itemform/', Itemform.Itemform.as_view(), name='itemform'),
    path('Cart_list/', Cart_list.Cart_list.as_view(), name='Cart_list'),
    path('Cart_login/', Cart_login.Cart_login.as_view(), name='Cart_login'),
    path('Cart_form/', CartForm.Cart_form.as_view(), name='Cart_form'),
    path('Cart_logout/', Cart_logout.Cart_logout.as_view(), name='Cart_logout'),
    path('Loction_update/', Updated_cart__location.location_Update.as_view(), name='Cart_logout'),

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
