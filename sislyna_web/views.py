from django.shortcuts import render

# Create your views here.

def WelcomePageView(request):
    return render(request, 'sislyna_web/welcome_page.html')