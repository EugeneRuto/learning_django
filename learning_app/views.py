from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, "index.html",context)

def our_story(request):
    context={}
    return render(request, "our_story.html",context)

def our_team_members(request):
    context={}
    return render(request, "our_team_members.html",context)

def contact_us(request):
    context={}
    return render(request, "contact_us.html",context)