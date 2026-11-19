
from Job_Post.models import JobPost
from Users.models import employer
from datetime import date, timedelta

employers = list(employer.objects.all())

if not employers:
    print("No employer accounts found!")

else:
    roles = [
        ("Software Engineer", "IT"),
        ("Python Developer", "IT"),
        ("Django Developer", "IT"),
        ("Frontend Developer", "IT"),
        ("Backend Developer", "IT"),
        ("Full Stack Developer", "IT"),
        ("UI/UX Designer", "Design"),
        ("Graphic Designer", "Design"),
        ("Digital Marketing Executive", "Marketing"),
        ("Data Analyst", "IT")
    ]

    locations = [
        "Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Khulna",
        "Barishal", "Rangpur", "Mymensingh", "Cumilla", "Gazipur"
    ]

    job_posts = []

    for i in range(100):
        role, category = roles[i % 10]
        location = locations[i // 10]

        job_posts.append(JobPost(
            employer=employers[i % len(employers)],
            job_title=f"{role} - {location}",
            job_category=category,
            job_type=["FULL-TIME", "PART-TIME", "CONTRACT", "INTERNSHIP"][i % 4],
            job_location=location,
            workplace_type=["ON-SITE", "REMOTE", "HYBRID"][i % 3],
            job_description=f"We are looking for a talented {role} in {location}.",
            responsibilities=f"Develop, maintain and improve projects related to {role}.",
            requirements=f"Knowledge of {role}, problem-solving and communication skills.",
            qualifications="Bachelor's degree in Computer Science or related field.",
            benefits="Competitive salary, paid leave and professional development.",
            required_skills="Python, Django, JavaScript, HTML, CSS, SQL",
            salary_min=25000 + (i * 500),
            salary_max=45000 + (i * 700),
            salary_currency="BDT",
            vacancies=(i % 5) + 1,
            experience_required=["Freshers", "1 Year", "2 Years", "3 Years"][i % 4],
            application_deadline=date.today() + timedelta(days=30 + i),
            application_email=employers[i % len(employers)].email,
            job_status="OPEN TO APPLY"
        ))

    JobPost.objects.bulk_create(job_posts)

    print(f"Successfully created {len(job_posts)} job posts!")
