"""Views for the tracker app."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudySession
from .forms import SubjectForm

def home(request):
    """Render the home page."""
    return render(request, 'tracker/home.html')

@login_required
def add_subject(request):
    """Handle creation of a new Subject via SubjectForm."""
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        subject = form.save(commit=False)
        subject.user = request.user
        subject.save()
        return redirect('dashboard')
    return render(request, 'tracker/add_subject.html', {'form': form})

@login_required
def dashboard(request):
    """Show user study sessions dashboard."""
    session = StudySession.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'session': session})
