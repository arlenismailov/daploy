from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('carorspareparts/', CarorSparepartsView.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('products/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}), name='product_list'),

]