"""growing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from food.views import (
    ApiUrlsView,
    VegetableDeleteView,
    VegetableGetView,
    VegetableUpdateView,
    VegetableView,
    VegetableTypeView,
    VegetableCreateView,
)


router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include(router.urls)),
    path("", ApiUrlsView.as_view()),
    path("vegetables/", VegetableView.as_view({"get": "list"})),
    path("vegetables-type/", VegetableTypeView.as_view({"get": "list"})),
    path("vegetable-create/", VegetableCreateView.as_view()),
    path("vegetable/<int:pk>/", VegetableGetView.as_view()),
    path("vegetable-delete/<int:pk>/", VegetableDeleteView.as_view()),
    path("vegetable-update/<int:pk>/", VegetableUpdateView.as_view()),
]
