from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'monitor',
        'price': '1000000',
        'description': 'gg gimang',
        'quantity': '1',
    }

    return render(request, "main.html", context)