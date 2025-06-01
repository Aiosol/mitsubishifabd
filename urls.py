"""
eshop_project/urls.py
~~~~~~~~~~~~~~~~~~~~~
Project-level URL dispatcher.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ---------------------------------------------------------------------------
#  If order-management is supposed to live at project level, import its view.
#  Otherwise, remove these two lines and define the URL in eshop/urls.py.
# ---------------------------------------------------------------------------
from eshop import views as eshop_views  # noqa: E402  (import after Django)

urlpatterns = [
    # --- Django / Jazzmin admin --------------------------------------------
    path("admin/", admin.site.urls),         # only ONE admin/ entry

    # --- App routes ---------------------------------------------------------
    path("", include("eshop.urls")),         # everything else is handled by the app

    # --- Optional: Order management page -----------------------------------
    path(
        "order-management/",
        eshop_views.order_management_view,   # ⚠️ make sure this exists
        name="order_management",
    ),
]

# ---------------------------------------------------------------------------
#  Media (dev only).  For production you’d serve media via Nginx, *not* Django.
# ---------------------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
