from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse

from .models import Task
from django.contrib import  messages



# Create your views here.
def info_personnel(request):
    print("Vue infor_personnel appelee!!")
    if request.method=="POST":
        option=request.POST.get("option_enre", None)
        task_user=request.POST.getlist("Tache[]")
        description=request.POST.getlist("description[]")
        priorities=request.POST.getlist("priorities[]")

        for task,descr,prio in zip(task_user,description,priorities):
             print("Tache:" ,task)
             if task and descr and prio:
                Task.objects.create(title=task, description=descr, priority=prio)
    donnees= Task.objects.all()
    return render(request, "Personal_tasks.html", context={"donnees":donnees})

def do_tache(request, id):
    tache=get_object_or_404(Task, id=id)
    tache.delete()
    return redirect("info_personnel")

def do_tache_all(request):
    if request.method=="POST":
      Task.objects.all().delete()
      return redirect('info_personnel')



def modifier_tache(request, id):
    tache=get_object_or_404(Task, id=id)

    if request.method=="POST":
        tache.titre=request.POST.get("title")
        tache.description=request.POST.get("description")
        tache.priorite=request.POST.get("priority")
        tache.save()
        return redirect('Personal_tasks')

    return render(request, "Personal_tasks.html", context={'task': tache})


