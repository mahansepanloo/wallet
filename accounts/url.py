from django.urls import path  
from .views import WaletListCreateView,WaletUpdate

urlpatterns = [  
    path('wallets/', WaletListCreateView.as_view(), name='walet-list-create'),  
    path('wallets/<int:pk>/',WaletUpdate.as_view(), name='walet-detail'),
]