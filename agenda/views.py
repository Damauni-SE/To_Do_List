from django import forms
from django.shortcuts import render, redirect


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]
            tasks = request.session.get("tasks", [])
            tasks.append(new_task)
            request.session["tasks"] = tasks
            return redirect("tasks:index")
    else:
        form = NewTaskForm()

    tasks = request.session.get("tasks", [])

    return render(request, "agenda/index.html", {
        "form": form,
        "tasks": tasks
    })
