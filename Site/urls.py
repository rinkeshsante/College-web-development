
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user managemanet
    # path('accounts/', include('allauth.urls')),


    # local apps
    # path('', include('pages.urls')),
    path('', include('repo.urls')),
]
