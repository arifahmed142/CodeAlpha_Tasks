from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobPost
from django.contrib import messages
from Application.models import Application
from Users.models import candidate, employer

# Create your views here.
def JobPosts(request):
    jobs = JobPost.objects.all()
    return render(request, 'homepage.html', {'jobs':jobs})

def onsite(request):
    jobs = JobPost.objects.filter(workplace_type = 'ON-SITE')
    return render(request, 'homepage.html', {'jobs':jobs})

def intern(request):
    jobs = JobPost.objects.filter(job_type = 'INTERNSHIP')
    return render(request, 'homepage.html', {'jobs':jobs})

def remote(request):
    jobs = JobPost.objects.filter(workplace_type = 'REMOTE')
    return render(request, 'homepage.html', {'jobs':jobs})



def JobDetails(request, id):
    job = get_object_or_404(JobPost, id=id)
    if hasattr(request.user, 'employer'):
        user = request.user.employer
    elif hasattr(request.user, 'candidate'):
        user = request.user.candidate
    else:
        user = None
    if request.method == 'POST':
        if hasattr(request.user, 'employer') and job.employer == request.user.employer:
            job.delete()
            messages.success(request, 'Job post deleted successfully!')
            return redirect('Home')
        messages.error(request, 'You are not authorized to delete this job.')
    return render(request, 'job_details.html', {'job': job,'user': user})


@login_required
def MyPostedJobs(request):

    if not hasattr(request.user, 'employer'):
        messages.error(request, 'Only employers can view their posted jobs.')
        return redirect('Home')
    employer = request.user.employer
    jobs = JobPost.objects.filter(employer=employer).prefetch_related('applications').order_by('-posted_at')
    total_applications = Application.objects.filter(job__employer=employer).count()
    context = {'jobs': jobs,'total_applications': total_applications,}

    return render(request, 'Post.html', context)


@login_required
def PostJob(request):

    if not hasattr(request.user, 'employer'):
        messages.error(request, 'Only employers can post jobs.')
        return redirect('Home')

    if request.method == 'POST':

        job_title = request.POST.get('job_title')
        job_category = request.POST.get('job_category')
        job_type = request.POST.get('job_type')
        job_location = request.POST.get('job_location')
        workplace_type = request.POST.get('workplace_type')

        job_description = request.POST.get('job_description')
        responsibilities = request.POST.get('responsibilities')
        requirements = request.POST.get('requirements')

        qualifications = request.POST.get('qualifications')
        benefits = request.POST.get('benefits')
        required_skills = request.POST.get('required_skills')
        experience_required = request.POST.get('experience_required')

        salary_min = request.POST.get('salary_min') or None
        salary_max = request.POST.get('salary_max') or None
        salary_currency = request.POST.get('salary_currency')
        vacancies = request.POST.get('vacancies')
        application_deadline = request.POST.get('application_deadline')
        application_email = request.POST.get('application_email') or None

        JobPost.objects.create(
            employer=request.user.employer,
            job_title=job_title,
            job_category=job_category,
            job_type=job_type,
            job_location=job_location,
            workplace_type=workplace_type,
            job_description=job_description,
            responsibilities=responsibilities,
            requirements=requirements,
            qualifications=qualifications or None,
            benefits=benefits or None,
            required_skills=required_skills or None,
            experience_required=experience_required or None,
            salary_min=salary_min,
            salary_max=salary_max,
            salary_currency=salary_currency,
            vacancies=vacancies,
            application_deadline=application_deadline,
            application_email=application_email
        )

        messages.success(request, 'Job posted successfully!')
        return redirect('Job_List')

    return render(request, 'postjob.html')


@login_required
def Applicants(request, id):

    if not hasattr(request.user, 'employer'):
        messages.error(request, 'Only employers can view applicants.')
        return redirect('Home')

    employer = request.user.employer
    job = get_object_or_404(JobPost,id=id,employer=employer)
    applications = Application.objects.filter(job=job).select_related('candidate').order_by('-applied_at')
    context = {'job': job,'applications': applications,'pending_count': applications.filter(application_status='PENDING').count(),'shortlisted_count': applications.filter(application_status='SHORTLISTED').count(),}

    return render(request, 'applicant_list.html', context)