from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # 메인 페이지
    path('mingeon/', views.mingeon, name='mingeon'),   # Hello 페이지
    path('dohun/', views.dohun, name='dohun'),
    path('hg/', views.hg, name='hg'),
]
