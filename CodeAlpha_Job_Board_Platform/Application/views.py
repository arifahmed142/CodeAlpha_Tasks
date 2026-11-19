from django.shortcuts import render, get_object_or_404, redirect
from Job_Post.models import JobPost
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application

@login_required
def application(request, id):

    job = get_object_or_404(JobPost, id=id)

    # Check whether the logged-in user is a candidate
    if not hasattr(request.user, 'candidate'):
        messages.error(request, 'Only candidates can apply for jobs.')
        return redirect('Details')
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

        if Application.objects.filter(job=job, candidate=candidate).exists():
            messages.warning(request, 'You have already applied for this job.')
            return redirect('Home')

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            resume = request.FILES.get('resume')
            cover_letter = request.POST.get('cover_letter')
            experience = request.POST.get('experience') or 0
            expected_salary = request.POST.get('expected_salary') or None

            if not resume:
                messages.error(request, 'Please upload your resume.')
                return render(request, 'apply_job.html', {'job': job,'user': candidate})

            Application.objects.create(
                job=job,
                candidate=candidate,
                name=name,
                email=email,
                phone=phone,
                address=address,
                resume=resume,
                cover_letter=cover_letter,
                experience=experience,
                expected_salary=expected_salary
            )

            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('Home')

    return render(request, 'application.html', {'job': job,'user': candidate})


@login_required
def applied(request):
    if not hasattr(request.user, 'candidate'):
        messages.error(request, 'Only candidates can view their applications.')
        return redirect('Home')
    candidate = request.user.candidate
    applications = Application.objects.filter(candidate=candidate).select_related('job','job__employer').order_by('-applied_at')
    context = {'applications': applications,'pending_count': applications.filter(application_status='PENDING').count(),'accepted_count': applications.filter(application_status='ACCEPTED').count(),}
    return render(request,'applied.html',context)



@login_required
def ApplicationDetails(request, id):

    if not hasattr(request.user, 'employer'):
        messages.error(request, 'Only employers can view applicant details.')
        return redirect('Home')

    employer = request.user.employer

    application = get_object_or_404(
        Application,
        id=id,
        job__employer=employer
    )

    if request.method == 'POST':

        status = request.POST.get('application_status')

        allowed_statuses = [
            'REVIEWED',
            'SHORTLISTED',
            'ACCEPTED',
            'REJECTED'
        ]

        if status in allowed_statuses:
            application.application_status = status
            application.save(update_fields=['application_status', 'updated_at'])
            messages.success(request, 'Application status updated successfully.')
        else:
            messages.error(request, 'Invalid application status.')

        return redirect('Applicant', id=application.job.id)

    return render(request, 'application-view.html', {'application': application})