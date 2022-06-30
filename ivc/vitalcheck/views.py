from django.shortcuts import render

# Create your views here.

def getLandingView(request):
    template_name = 'landing.html'
    return render(request,template_name)



def getStatsView(request):
    template_name = "stats.html"
    print("hello world")
    return render(request,template_name)    