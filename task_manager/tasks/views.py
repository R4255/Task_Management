from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Task
from django.contrib import messages
from django.contrib.auth.views import LoginView

from django.contrib.auth import logout
# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-priority', 'title']  # Order by priority descending, then by title

    def get_queryset(self):
    # Filter tasks by the logged-in user
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Separate tasks into high priority and normal priority
        context['high_priority_tasks'] = context['tasks'].filter(priority=2)
        context['normal_priority_tasks'] = context['tasks'].filter(priority=1)
        return context
    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model=Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'priority', 'deadline']  # Include 'deadline'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'priority', 'deadline']  # Include 'deadline'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    success_url=reverse_lazy('task_list')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=UserCreationForm()
    return render(request,'tasks/register.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('task_list')
class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')  # Replace 'home' with your desired redirect URL na
    def form_invalid(self, form):
        # Add an error message to be displayed on the login page
        messages.error(self.request, "Invalid username or password. Please try again.")
        return self.render_to_response(self.get_context_data(form=form))