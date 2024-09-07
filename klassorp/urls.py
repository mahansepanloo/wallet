

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("transacion.url")),
    path('b',include('budget.url')),
    path('a',include("accounts.url"))
]
