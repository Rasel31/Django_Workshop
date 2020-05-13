from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.model_choices import state_choices, bedroom_choices, price_choices
# pages app views


def index(request):
    latest = Listing.objects.order_by('-list_date')[:3]    # 0, 1, 2 object
    #   Listing.objects.order_by('-list_date')  ==> select * from Listing order by list_date Desc

    context = {
        'latest': latest,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,

    }
    return render(request,'pages/index.html', context)


def about(request):
    team = Realtor.objects.order_by('-contact_date')[:3]
    seller_of_month = Realtor.objects.filter(is_mvp=True).first()
    #   Realtor.objects.filter(is_mvp=True)  ==> select * from Realtor where is_mvp = True

    context = {
        'team': team,
        'seller_of_month': seller_of_month
    }
    return render(request,'pages/about.html', context)
