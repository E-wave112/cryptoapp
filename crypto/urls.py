from django.urls import path,include
from . import views
from .views import SignUpView,home
from django.views.generic.base import TemplateView

# app_name  = 'crypto'

urlpatterns = [
    
    path('',views.home,name='base'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.index,name='login'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/',include('allauth.urls'))
]