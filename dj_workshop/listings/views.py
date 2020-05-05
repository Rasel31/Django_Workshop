from django.shortcuts import render
from .models import Listing
# from .models import * # Bad Practise
# listings app view


def listings_index(request):
    listing_list = Listing.objects.all()

    context = {
        'listing_list': listing_list,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_ = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing.html', {'listing': listing_})


def search(request):
    return render(request, 'listings/search.html')
