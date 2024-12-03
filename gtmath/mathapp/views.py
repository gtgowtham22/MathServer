from django.shortcuts import render
from django.http import JsonResponse

def lamp_power_calculator(request):
    """Renders the Lamp Power Calculator page."""
    return render(request, 'lamp_power_calculator.html')

def calculate_power(request):
    """Handles the power calculation request."""
    if request.method == 'GET':
        intensity = float(request.GET.get('intensity', 0))
        resistance = float(request.GET.get('resistance', 0))
        power = intensity**2 * resistance
        return JsonResponse({'power': round(power, 2)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
