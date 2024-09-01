from decimal import Decimal
from .models import Crop

def recommend_crop():
    """
    Recommend the best crop based on the highest sustainability score.
    """
    # Query the crop with the highest sustainability score
    recommended_crop = Crop.objects.order_by('-sustainability_score').first()

    # Debugging output
    if recommended_crop:
        print(f"Recommended Crop: {recommended_crop.name}")
        print(f"Sustainability Score: {recommended_crop.sustainability_score}")
        print(f"Market Value per Ton: {recommended_crop.market_value_per_ton}")
        print(f"Optimal Growing Season: {recommended_crop.optimal_growing_season}")

        recommended_loan_amount = calculate_loan_amount(recommended_crop)
        best_season = recommended_crop.optimal_growing_season

        return recommended_crop, recommended_loan_amount, best_season
    else:
        return None, 0, "Unknown"

def calculate_loan_amount(crop):
    """
    Calculate the recommended loan amount based on the crop's market value.
    """
    base_amount = Decimal('1000')  # Base loan amount as Decimal
    if hasattr(crop, 'market_value_per_ton') and crop.market_value_per_ton is not None:
        market_value = Decimal(crop.market_value_per_ton)
        loan_amount = base_amount + (market_value * Decimal('0.1'))  # Calculate loan amount using Decimal
        print(f"Calculated Loan Amount: {loan_amount}")
        return loan_amount
    else:
        print(f"Market value not available for crop: {crop.name}")
        return base_amount  # Default loan amount if market value is not available
