from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Listing
from .model_choices import price_choices, state_choices, bedroom_choices
# from .models import * # Bad Practise
# listings app view


def listings_index(request):
    listing_list = Listing.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(listing_list, 2)

    try:
        listing_list = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        listing_list = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        listing_list = paginator.page(paginator.num_pages)

    context = {
        'listing_list': listing_list,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # get single listing object
    listing_ = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing.html', {'listing': listing_})


def search(request):
    # city_ = request.GET.get('city')  # Do Not Do This or u will be slapped
    get_method = request.GET.copy()
    # keywords = get_method.get('keywords')
    # city = get_method.get('city')
    print(get_method)
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'get_method': get_method,
    }
    return render(request, 'listings/search.html', context)
