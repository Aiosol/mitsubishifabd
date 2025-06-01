# eshop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),

    # product / catalogue
    path("product/<str:sku>/", views.product_detail_view, name="product_detail"),
    path("fx-series/", views.fx_series_view, name="fx_series"),
    path("vfd/", views.vfd_view, name="vfd"),
    path("category/<str:cat_name>/", views.category_filter_view,
         name="category_filter"),
    path("brand/<int:brand_id>/", views.brand_detail_view, name="brand_detail"),
    path("series/<str:series_name>/", views.series_filter_view,
         name="series_filter"),
    path("parent/<slug:parent_slug>/", views.parent_detail_view,
         name="parent_detail"),

    # search / filter
    path("search/", views.search_view, name="search"),
    path("filter/", views.product_filter_search_view,
         name="product_filter_search"),
    path("product-suggestions/", views.product_search_suggestions,
         name="product_search_suggestions"),

    # quotation / discount / orders
    path("ask-discount/<str:sku>/", views.ask_for_discount_view,
         name="ask_for_discount"),
    path("quotation/<int:pk>/", views.quotation_detail_view,
         name="quotation_detail"),
    path("discount-submitted/<int:quotation_id>/",
         views.discount_submitted_view, name="discount_submitted"),
    path("order/edit/<int:pk>/", views.edit_order_view, name="edit_order"),
    path("all-vfd-inverters/", views.all_vfd_inverters_view,
         name="all_vfd_inverters"),
]
