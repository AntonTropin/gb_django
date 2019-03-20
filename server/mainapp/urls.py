from django.urls import path

from .views import (
    main, support
)

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
    path('support/', support, name='support')
]