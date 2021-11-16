from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .controllers import products_from_category


urlpatterns = {
    path('<slug:product_category_name>', products_from_category, name="product_category_name")
}

urlpatterns = format_suffix_patterns(urlpatterns)