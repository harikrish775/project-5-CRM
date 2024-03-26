from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.landing_page,name='landing_page'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('archives',views.archives,name='archives'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    # path('abc',views.abc,name='abc'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)