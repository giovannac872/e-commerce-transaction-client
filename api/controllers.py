import json
from django.conf import settings
import redis
import environ
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

env = environ.Env()
environ.Env.read_env() 

redis_instance = redis.Redis(
    host=env('REDIS_HOST'),
    username=env('REDIS_USERNAME'),
    port=env('REDIS_PORT'), 
    password=env('REDIS_PWD'))


@api_view(['GET'])
def sellers_sell_product(request, *args, **kwargs):
    if kwargs['product_id']:
        value = redis_instance.get(kwargs['product_id'])
        response = {
            'key': kwargs['product_id'],
            'value': None,
            'msg': 'Not found'
        }
        if value:
            response['value'] = value
            response['msg']  = 'success'

            return Response(response, status=200)

        return Response(response, status=404)

@api_view(['GET'])
def products_sell_sellers(request, *args, **kwargs):
    if kwargs['seller_id']:
        value = redis_instance.get(kwargs['seller_id'])
        response = {
            'key': kwargs['seller_id'],
            'value': None,
            'msg': 'Not found'
        }
        if value:
            response['value'] = value
            response['msg']  = 'success'

            return Response(response, status=200)

        return Response(response, status=404)

@api_view(['GET'])
def products_from_category(request, *args, **kwargs):
    if kwargs['product_category_name']:
        value = redis_instance.get(kwargs['product_category_name'])
        response = {
            'key': kwargs['product_category_name'],
            'value': None,
            'msg': 'Not found'
        }
        if value:
            response['value'] = value
            response['msg']  = 'success'

            return Response(response, status=200)

        return Response(response, status=404)