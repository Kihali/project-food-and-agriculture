from django.shortcuts import render
from .models import Crop, Farmer, Investment
from .recommendation import recommend_crop
from django.db.models import Sum, Avg

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
    # Aggregate data for the marketplace
    total_crops = Crop.objects.count()
    avg_market_value = Crop.objects.aggregate(Avg('market_value_per_ton'))['market_value_per_ton__avg'] or 0
    avg_sustainability_score = Crop.objects.aggregate(Avg('sustainability_score'))['sustainability_score__avg'] or 0
    
    # Get all crops
    crops = Crop.objects.all()

    context = {
        'crops': crops,
        'total_crops': total_crops,
        'avg_market_value': avg_market_value,
        'avg_sustainability_score': avg_sustainability_score,
    }
    return render(request, 'agriculture/marketplace.html', context)

def invest(request):
    farmers = Farmer.objects.all()
    context = {
        'farmers': farmers,
    }
    return render(request, 'agriculture/invest.html', context)

def crop_recommendation(request):
    recommended_crop, recommended_loan_amount, best_season = recommend_crop()

    context = {
        'crop_name': "No crop recommended",
        'loan_amount': 0,
        'season': "N/A",
        'profitability': "N/A",
        'sustainability_score': "N/A",
        'total_investment': 0,
        'avg_market_value': 0,
        'avg_sustainability_score': 0,
    }

    if recommended_crop:
        context['crop_name'] = recommended_crop.name
        context['loan_amount'] = recommended_loan_amount
        context['season'] = best_season
        context['profitability'] = recommended_crop.market_value_per_ton
        context['sustainability_score'] = recommended_crop.sustainability_score

        # Calculate total investment related to the recommended crop
        context['total_investment'] = Investment.objects.filter(crop=recommended_crop).aggregate(total_investment=Sum('amount'))['total_investment'] or 0

        # Calculate average market value and sustainability score for comparison
        context['avg_market_value'] = Crop.objects.aggregate(avg_market_value=Avg('market_value_per_ton'))['avg_market_value'] or 0
        context['avg_sustainability_score'] = Crop.objects.aggregate(avg_sustainability_score=Avg('sustainability_score'))['avg_sustainability_score'] or 0

    return render(request, 'agriculture/recommendation.html', context)