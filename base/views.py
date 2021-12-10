from django.shortcuts import render

from base.models import Product

# Create your views here.


def home(request):

    data = Product.objects.all()
    context = {
        'data': data
    }

    return render(request, 'home.html', context)
