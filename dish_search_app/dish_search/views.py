from django.shortcuts import render
from .models import Restaurant

def search(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = Restaurant.objects.filter(name__icontains=query)

    context = {'results': results}
    return render(request, 'search.html', context)
