from django.http import HttpResponse
from django.shortcuts import render
from .models import UserTask 
from django.shortcuts import redirect, get_object_or_404

def home(request):
    return render(request, 'app/home.html')

def task_detail(request):
    if request.method == 'POST':
        task_text = request.POST.get('tasks') 
        new_task = UserTask.objects.create(kia=task_text)
        return redirect('task_detail')
        # queries=UserTask.objects.all()
        # return render(request,'app/list.html', {'kata':queries})
    
    else:
        tasks = UserTask.objects.all()  # Retrieve all tasks
        return render(request, 'app/list.html', {'kata': tasks})

def delete_task(request, pk):
    task = get_object_or_404(UserTask, pk=pk)
    task.delete()
    return redirect('task_detail') 
    
def edit_task(request, pk):
    task = get_object_or_404(UserTask, pk=pk)
    if request.method == "POST":
        task_text = request.POST.get('editask')
        task.kia = task_text  # Update task content
        task.save()  # Save the changes
        return redirect('task_detail')
    else:
        return render(request, 'app/edit.html', {'task': task})


    
        
        
    
    
    






