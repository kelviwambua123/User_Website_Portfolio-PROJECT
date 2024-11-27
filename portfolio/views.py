from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Feedback
from .forms import ProjectForm, FeedbackForm
from django.contrib.auth.decorators import login_required

@login_required  # Ensures the user is logged in
def project_list(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'portfolio/project_list.html', {'projects': projects})

@login_required  # Ensures the user is logged in
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)  # Ensure user owns the project
    feedbacks = project.feedbacks.all()  # Get all feedback related to the project

    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.project = project
            feedback.user = request.user if request.user.is_authenticated else None  # Set user if logged in
            feedback.save()
            return redirect('portfolio:project_detail', pk=project.pk)
    else:
        feedback_form = FeedbackForm()

    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'feedbacks': feedbacks,
        'feedback_form': feedback_form,
    })

@login_required  # Ensures the user is logged in
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('portfolio:project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form})

@login_required  # Ensures the user is logged in
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form})

@login_required  # Ensures the user is logged in
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == "POST":
        project.delete()
        return redirect('portfolio:project_list')
    return render(request, 'portfolio/project_confirm_delete.html', {'project': project})