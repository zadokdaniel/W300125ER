from django.urls import path, register_converter, re_path
from .converters.year_converter import YearConverter
from .views import index, users, users_details, by_year

register_converter(YearConverter, 'yyyy')


urlpatterns = [
    path('', index),
    path('users/', users),
    path('users/<int:id>', users_details),
    # path('users/<id>', users_details),
    path("byYear/<yyyy:year>", by_year),
    re_path(r'^(?P<year>[2][0-9]{3})/$', by_year)
]
