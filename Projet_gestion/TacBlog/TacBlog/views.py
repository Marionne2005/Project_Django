from django.http import HttpResponse
from django.shortcuts import render





def index_1(request):
    if request.method== "POST":
        nom=request.POST.get("nom")
        email=request.POST.get("email")
        return HttpResponse
    return render(request, "templates_html.html")

def informations(request):
    if request.method== "POST":
        nom=request.POST.get("nom")
        email=request.POST.get("email")
        return render(request, "page_reponse.html", context={"nom": nom, "email": email,})

def page(request):
    if request.method=="POST":
        type_tache=request.POST.get("type_tache")
        if type_tache=="personnelles":
            return render(request, "Personal_tasks.html")
        elif type_tache=="professionnelles":
            return render(request, "Professional_tasks.html")
        elif type_tache=="menageres":
            return render(request, "housewives_tasks.html")


        