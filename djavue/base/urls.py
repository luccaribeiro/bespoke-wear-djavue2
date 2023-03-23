from django.urls import path, include
from . import views



urlpatterns = [
    path("list", views.list_products),
    path("add", views.create_product),
    path("shoppingcart", views.list_shopping_cart),
    path("shoppingcart/<id>", views.get_product_id, name ="product_id"),
    path("addcart", views.add_to_cart),
    path("removecart/<id>", views.delete_of_cart, name='remove_cart'),
    path("removeproduct/<id>", views.delete_product, name='remove_product'),
    path("editproduct/<id>", views.edit_product, name='remove_product'),
    path("create", views.create_coupon),
    path("apply", views.apply_coupon),
]
