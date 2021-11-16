from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .controllers import products_sell_sellers


urlpatterns = {
    path('<slug:seller_id>', products_sell_sellers, name="products_sell_sellers")
}

urlpatterns = format_suffix_patterns(urlpatterns)