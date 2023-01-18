from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404 ,render
from .models import listing
from listings.choices import price_choices,bedroom_choices,state_choices

# Create your views here.

def index(request):
    listings = listing.objects.order_by('-list_date').filter(is_published=True)
    # implementing pagination
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listingById(request, listing_id):
    listing_detail = get_object_or_404(listing, pk=listing_id)

    context = {
        'listing' : listing_detail
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'listings/search.html' , context)
