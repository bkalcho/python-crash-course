from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all pizzas.
    url(r'^pizza_list/$', views.pizza_list, name='pizza_list'),

    # Toppings for each pizza
    url(r'^pizza_list/(?P<pizza_id>\d+)/$', views.pizza, name='pizza')
]