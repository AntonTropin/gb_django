from django.urls import path

from .views import (
    product_detail, product_list
)

app_name = 'productsapp'

urlpatterns = [
    path('<int:pk>', product_list, name='main'),
    path('detail/', product_detail, name='detail')
]