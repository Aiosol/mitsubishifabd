# my_eshop_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# import the one view that really lives at the project-level
from eshop import views as eshop_views      # <-- only for order-management

urlpatterns = [
    path("admin/", admin.site.urls),

    # one project-level view (lives in eshop.views)
    path("order-management/", eshop_views.order_management_view,
         name="order_management"),

    # everything else comes from the eshop app
    path("", include("eshop.urls")),
]

# serve uploaded files in DEBUG mode only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
