from django.shortcuts import render


# Create your views here.
def pay(request):
    return render(request, 'pay.html')


def recharge(request):
    return render(request, 'recharge.html')


def rechargeok(request):
    return render(request, 'rechargeok.html')