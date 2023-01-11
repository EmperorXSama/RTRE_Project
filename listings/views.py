from django.shortcuts import render
from .models import listing


# Create your views here.

def index(request):
    listings = listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)


def listingById(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
