from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView

from manage_todo.models import Todo

class Home(LoginRequiredMixin, View):

    login_url = "register"
    redirect_field_name = "redirect_to"
    
    def get(self, request, *args, **kwargs):
        context = Todo.objects.filter(user = self.request.user).order_by('-pk')
        today = datetime.today().date()
        return render(request, 'manage_todo/index.html', context={'todos' : context, 'today' : today})
    
class CreateTodo(LoginRequiredMixin, View):
    login_url = "register"
    redirect_field_name = "redirect_to"

    def post(self, request):
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date_expire = request.POST.get('date_expire')
        priority = request.POST.get('priority')
        Todo.objects.create(title=title, desc=desc, date_expire=date_expire, priority=priority, user=self.request.user)
        return redirect('home')
    
class UpdateTodo(LoginRequiredMixin, View):
    login_url = "register"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        context = Todo.objects.filter(user = self.request.user).order_by('-pk')
        edit = get_object_or_404(Todo, pk=self.kwargs.get('pk'), user=self.request.user)
        today = datetime.today().date()
        return render(request, 'manage_todo/index.html', context={
            "todos" : context,
            'edit' : edit,
            'today' : today,
        })
    
    def post(self, request, **kwargs):
        pk = kwargs.get('pk')
        todo = get_object_or_404(Todo, pk=pk)
        todo.title = request.POST.get('title')
        todo.desc = request.POST.get('desc')
        todo.date_expire = request.POST.get('date_expire')
        todo.priority = request.POST.get('priority')
        todo.save()
        return redirect('home')
    
class DeleteTodo(LoginRequiredMixin, View):
    login_url = "register"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        get_object_or_404(Todo, pk=pk, user=self.request.user).delete()
        return redirect('home')
    
class CompleteToggle(LoginRequiredMixin, View):
    login_url = "register"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        todo = get_object_or_404(Todo, pk=pk, user=self.request.user)
        todo.is_completed = not todo.is_completed
        todo.save()
        return redirect('home')

