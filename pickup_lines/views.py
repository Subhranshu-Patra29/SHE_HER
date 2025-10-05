from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from .models import PickupLine

def home(request):
    """Home page with two buttons"""
    return render(request, 'pickup_lines/home.html')

@csrf_exempt
def get_romantic_pickup_line(request):
    """API endpoint to get a random romantic pickup line"""
    romantic_lines = PickupLine.objects.filter(category='romantic')
    if romantic_lines.exists():
        random_line = random.choice(romantic_lines)
        return JsonResponse({
            'pickup_line': random_line.text,
            'category': random_line.category
        })
    else:
        return JsonResponse({
            'pickup_line': 'No romantic pickup lines available',
            'category': 'romantic'
        })

@csrf_exempt
def get_techy_pickup_line(request):
    """API endpoint to get a random techy pickup line"""
    techy_lines = PickupLine.objects.filter(category='techy')
    if techy_lines.exists():
        random_line = random.choice(techy_lines)
        return JsonResponse({
            'pickup_line': random_line.text,
            'category': random_line.category
        })
    else:
        return JsonResponse({
            'pickup_line': 'No techy pickup lines available',
            'category': 'techy'
        })