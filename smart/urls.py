from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve


urlpatterns = [
     path('admin/', admin.site.urls),
     path("", include("supply.urls", namespace="supply")),
     path("accounts/", include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                      view=cache_control(no_cache=True, must_revalidate=True)(serve))