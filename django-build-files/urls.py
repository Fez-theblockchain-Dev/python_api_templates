"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.utils.timezone import now

class APIRootView(APIView):
    def get(self, request, user_data_object=True):
        user_data_object = {
            "user": request.user.username,
            "passcode": input("Please enter your passcode associated with your account "),
            "timestamp": now(),
            "DOB": input("Please enter your date of birth in the format YYYY-MM-DD: "),
            "location": input("Please enter your location: "),
            



        }
        return Response({
            "users": reverse('user-list', request=request),
            "snippets": reverse('snippet-list', request=request),
            "user_data_object": user_data_object
        })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('route/', route.list.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
