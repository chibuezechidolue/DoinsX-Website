"""
URL configuration for Doinsx project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header="DoinsXtmc Administration"
admin.site.site_title="DoinsXtmc Administration"
admin.site.index_title="DoinsXtmc Admin"
admin.site.empty_value_display = "(None)"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Website.urls"))
]

# if settings.DEBUG:        #  note this line is commented out because this app is intended to run media files from the server backend storage and debug will still need to be trurned of
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
