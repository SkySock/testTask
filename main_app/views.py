from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
import stripe

from main_app.models import Item


def get_session_id(request, pk: int):
    """
    Получить session_id для проведения оплаты
    :param request:
    :param pk:
    :return:
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods='GET')

    instance: Item = get_object_or_404(Item, pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': instance.name,
                    'description': instance.description,
                },
                'unit_amount': int(instance.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    return JsonResponse({'session_id': session.id})


def buy_item(request, pk):
    """
    Страница с описанием товара и кнопка для редиректа на сервис оплаты
    :param request:
    :param pk:
    :return:
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods='GET')

    item: Item = get_object_or_404(Item, pk=pk)

    return render(request, 'main_app/buy_item.html', context={'item': item})
