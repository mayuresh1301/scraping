from django.shortcuts import render
from .models import Job
from bs4 import BeautifulSoup
import requests


# Create your views here.
def find_jobs(request):
    unfamiliar_skills_input = request.GET.get('skills', '')
    unfamiliar_skills = [skill.strip() for skill in unfamiliar_skills_input.split(',')]
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        posted_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in posted_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            link = job.find('header', class_ = 'clearfix').h2.a['href']
            if not any (unfamiliar_skill in skills for unfamiliar_skill in unfamiliar_skills):
                Job.objects.create(company_name=company_name.strip(), skills=skills.strip(), more_info=link)

    return render(request, 'scraper/job_list.html', {'jobs': Job.objects.all()})

def skills_form(request):
    return render(request, 'scraper/job_list.html')