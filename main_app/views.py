from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
import stripe

from main_app.models import Item, Order


def get_session_id_for_item(request, pk: int):
    """
    Получить session_id для проведения оплаты товара
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


def get_session_id_for_order(request, pk: int):
    """
    Получить session_id для проведения оплаты заказа
    :param request:
    :param pk:
    :return:
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods='GET')

    instance: Order = get_object_or_404(Order, pk=pk)

    line_items = [
        {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        } for item in instance.items.all()
    ]

    session = stripe.checkout.Session.create(
        line_items=line_items,
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


def buy_order(request, pk):
    """
    Страница с описанием товаров в заказе и кнопка для редиректа на сервис оплаты
    :param request:
    :param pk:
    :return:
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods='GET')

    order: Order = get_object_or_404(Order, pk=pk)

    return render(request, 'main_app/buy_order.html', context={'order': order, 'items': order.items.all()})
