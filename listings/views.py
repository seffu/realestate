from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .models import Listing

# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }
    print(context)
    return render(request,'listings/listings.html',context)
def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query_listing = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listing = query_listing.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listing = query_listing.filter(city__iexact=city)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_listing = query_listing.filter(bedrooms__lte=bedrooms)
    context = {
        'listing':query_listing,
        'values':request.GET,
    }
    return render(request,'listings/search.html',context=context)
