from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hotel_image_view),
    path('display/', views.display_img),
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
