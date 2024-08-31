from django.shortcuts import render
from .models import Crop
from .recommendation import recommend_crop
from django.db.models import Sum, Avg
from .models import Crop, Farmer, Investment

def index(request):
    crops = Crop.objects.all()
    farmers = Farmer.objects.all()
    context = {
        'crops': crops,
        'farmers': farmers,
    }
    return render(request, 'agriculture/index.html', context)

def impact_dashboard(request):
    total_earnings = Farmer.objects.aggregate(Sum('earnings'))['earnings__sum'] or 0
    total_investments = Investment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    sustainability_score = Crop.objects.aggregate(Avg('sustainability_score'))['sustainability_score__avg'] or 0

    context = {
        'total_earnings': total_earnings,
        'total_investments': total_investments,
        'sustainability_score': sustainability_score,
    }
    return render(request, 'agriculture/dashboard.html', context)

def marketplace(request):
    crops = Crop.objects.all()
    context = {
        'crops': crops,
    }
    return render(request, 'agriculture/marketplace.html', context)

def invest(request):
    farmers = Farmer.objects.all()
    context = {
        'farmers': farmers,
    }
    return render(request, 'agriculture/invest.html', context)

def crop_recommendation(request):
    # Get the best crop recommendation based on the database query
    recommended_crop, recommended_loan_amount, best_season = recommend_crop()
    
    # Check if a crop was recommended
    if not recommended_crop:
        return render(request, 'agriculture/recommendation.html', {'error': 'No suitable crop found.'})

    context = {
        'recommended_crop': recommended_crop.name,
        'suitability': recommended_crop.sustainability_score,
        'market_demand': "N/A",  # Since market_demand is not available, set to "N/A"
        'profitability': recommended_crop.price,  # Using price as a proxy for profitability
        'climate_adaptability': "N/A",  # Set to "N/A" if not available
        'recommended_loan_amount': recommended_loan_amount,
        'best_season': best_season
    }
    return render(request, 'agriculture/recommendation.html', context)