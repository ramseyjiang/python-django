from django.http import JsonResponse
from django.db import connection

def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")  # Simple query to check DB connectivity
        return JsonResponse({'status': 'healthy'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)