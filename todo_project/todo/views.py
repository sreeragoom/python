from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    tasks = Todo.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        Todo.objects.create(title=title)
        return redirect("/")
    return render(request, "index.html", {"tasks": tasks})

def delete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect("/")

def update_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.completed = "completed" in request.POST
        task.save()
        return redirect("/")
    return render(request, "update_task.html", {"task": task})
