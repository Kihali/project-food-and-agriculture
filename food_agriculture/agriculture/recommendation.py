from decimal import Decimal
from .models import Crop

def recommend_crop():
    """
    Recommend the best crop based on the highest sustainability score.
    """
    # Query the crop with the highest sustainability score
    recommended_crop = Crop.objects.order_by('-sustainability_score').first()

    if recommended_crop:
        recommended_loan_amount = calculate_loan_amount(recommended_crop)
        best_season = recommended_crop.season  # Using 'season' as the best season to plant

        return recommended_crop, recommended_loan_amount, best_season
    else:
        return None, 0, "Unknown"

def calculate_loan_amount(crop):
    """
    Calculate the recommended loan amount based on the crop's price.
    """
    base_amount = Decimal('1000')  # Base loan amount as Decimal
    return base_amount + (crop.price * Decimal('0.1'))  # Calculate loan amount using Decimal
