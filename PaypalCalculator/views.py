from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
PRICE_ADDON_CONSTANTS = {
    # no fees
    "friends_family": {"rate_percent": 0, "flat_fee": 0.0},
    # fees for private sellers
    "goods_services": {"rate_percent": 2.49, "flat_fee": 0.35},
    # fees for donations
    "donations": {"rate_percent": 1.00, "flat_fee": 0.35},
    # fees for micro payments (?)
    "micro_payment": {"rate_percent": 3.25, "flat_fee": 0.10},
    # fees for sellers/dealers between 0 - 2.000€
    "dealer_condition_1": {"rate_percent": 0.50, "flat_fee": 0.35},
    # fees for sellers/dealers between 2.000,01 - 5.000€
    "dealer_condition_2": {"rate_percent": 4.75, "flat_fee": 0.35},
    # fees for sellers/dealers between 5.000,01 - 25.000€
    "dealer_condition_3": {"rate_percent": 2.00, "flat_fee": 0.35},
    # fees for sellers/dealers between 25.000,01 - 100.000€
    "dealer_condition_4": {"rate_percent": 1.50, "flat_fee": 0.35},
    # fees for sellers/dealers above 100.000€
    "dealer_condition_5": {"rate_percent": 1.49, "flat_fee": 0.35},
}

goods_type_labels = {
    "friends_family": "Friends & Family",
    "goods_services": "Goods & Services",
    "donations": "Donations",
    "micro_payment": "Micro Payment",
    "dealer_condition_1": "Dealer Condition (between 0€ - 2.000€)",
    "dealer_condition_2": "Dealer Condition (between 2.000,01€ - 5.000€)",
    "dealer_condition_3": "Dealer Condition (between 5.000,01€ - 25.000€)",
    "dealer_condition_4": "Dealer Condition (between 25.000,01€ - 100.000€)",
    "dealer_condition_5": "Dealer Condition (above 100.000€)",
}
def calculate_fees(request):
    if request.method == 'GET':
        goods_type_items = [
            (key, goods_type_labels[key])
            for key in PRICE_ADDON_CONSTANTS.keys()
        ]
        context = {
            'goods_type_items': goods_type_items,
            'goods_type': PRICE_ADDON_CONSTANTS,
        }
        return render(request, 'PaypalCalculator/calculate.html', context)

    result = None
    if request.method == 'POST':
        goods_type = request.POST.get('goods_type', '')
        amount_str = request.POST.get('amount', '0')
        if not goods_type:
            return render(
                request,
                'PaypalCalculator/calculate.html',
                {'error': 'Please select a Goods type'}
            )
        try:
            amount = float(amount_str)
            fee_rate = _get_correct_goods_type(goods_type)
            if not fee_rate:
                return render(
                    request,
                    'PaypalCalculator/calculate.html',
                    {'error': 'Internal error. Please try again'}
                    )
            fixed_fee = fee_rate['rate_percent']
            fee_rate = fee_rate['flat_fee']
            result = amount - (amount * fee_rate + fixed_fee)
        except (ValueError, TypeError):
            result = None
    return render(request, 'PaypalCalculator/calculate.html', {'result': result})


def _get_correct_goods_type(goods_type):
    default = {}
    type_of_good = PRICE_ADDON_CONSTANTS.get(goods_type, default)

    if not type_of_good:
        return {}

    try:
        return {
            "rate_percent": float(type_of_good["rate_percent"]),
            "flat_fee": float(type_of_good["flat_fee"]),
        }
    except (KeyError, TypeError, ValueError):
        return {}