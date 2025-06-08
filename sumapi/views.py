from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def sum_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            x = int(data.get('x', 0))
            y = int(data.get('y', 0))
            return JsonResponse({'sum': x + y})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST only'}, status=405)
