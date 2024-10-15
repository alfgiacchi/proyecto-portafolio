from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from abaut import views as abaut_views


urlpatterns = [
    path('', core_views.home, name='home'),
    path('abaut/', abaut_views.abaut, name='abaut'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

from django.conf import settings


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
