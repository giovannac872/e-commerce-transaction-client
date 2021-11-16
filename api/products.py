from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .controllers import sellers_sell_product


urlpatterns = {
    path('<slug:product_id>', sellers_sell_product, name="sellers_sell_product")
}

urlpatterns = format_suffix_patterns(urlpatterns)