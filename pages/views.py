from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:4]
    context = {
        'listings': listings
    }
    return render(request,'pages/index.html',context)
def about(request):
    return render(request,'pages/about.html')
