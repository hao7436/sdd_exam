from django.shortcuts import render
from .models import *
# Create your views here.
from newsapi import NewsApiClient
from .forms import *
from django.http import HttpResponseRedirect

                              

def index(request):

 return render(request, 'antiScam/index.html')

def scamType(request):
 
 return render(request, 'antiScam/ScamType.html')

def typeDetail1(request):
 
 return render(request, 'antiScam/typeDetail1-Impersonation.html')

def stories(request):
 stories = Stories.objects.all()
 return render(request, 'antiScam/stories.html',{'stories':stories})

def mediaNews(request):
 newsapi = NewsApiClient(api_key='f0517292ba784eb48dbbb16c1535b45b')
 top_headlines = newsapi.get_everything(q='scams')
 #sources = newsapi.get_sources()
 thisdict={"title":[],"url":[]}
 list_b = []
 list_c = []
 
 for item in top_headlines['articles']:
  list_b.append(item['title'])
  list_c.append(item['url'])
  thisdict["title"].append(item['title'])
  thisdict["url"].append(item['url'])  
 result = zip(list_b, list_c)
 context = {
    'mylist': result,
  }
 
 return render(request, 'antiScam/mediaNews.html',context)

def addStory(request):
 
 
 return render(request, 'antiScam/addStory.html')

def addStoryAction(request):

  if request.method == 'POST':
        form = storyForm(request.POST)
        if form.is_valid():
            stories = Stories()
            stories.authorFname = form.cleaned_data['authorFname']
            stories.authorLname = form.cleaned_data['authorLname']
            stories.authorEmail = form.cleaned_data['authorEmail']
            stories.authorNumber = form.cleaned_data['authorNumber']
            stories.scamTitle = form.cleaned_data['scamTitle']
            stories.scamType = form.cleaned_data['scamType']
            stories.nameOfScamer = form.cleaned_data['nameOfScamer']
            stories.contentOfScamer = form.cleaned_data['contentOfScamer']
            stories.emailOfScamer = form.cleaned_data['emailOfScamer']
            stories.scamDetail = form.cleaned_data['scamDetail']
            stories.save()
            return HttpResponseRedirect('/stories/')
  else:
        stories = Stories.objects.all()
        form = storyForm()
        return render(request, 'antiScam/stories.html',{'stories':stories})

def addCooperationAction(request):

  if request.method == 'POST':
        form = CooperationForm(request.POST)
        if form.is_valid():
            cooperations = Cooperation()
            cooperations.organisationName = form.cleaned_data['organisationName']
            cooperations.organisationEmail  = form.cleaned_data['organisationEmail']
            cooperations.personInContact  = form.cleaned_data['personInContact']
            cooperations.ContactNumber  = form.cleaned_data['ContactNumber']
            cooperations.cooperationDetail  = form.cleaned_data['cooperationDetail']
            cooperations.timestamp  = form.cleaned_data['timestamp']
            cooperations.save()
            return HttpResponseRedirect('/cooperation/')
  else:
        form = CooperationForm()
        return render(request, 'antiScam/cooperation.html')



def activities(request):
 
 return render(request, 'antiScam/Activities.html')

def activitiesDetail1(request):
 
 return render(request, 'antiScam/activites-detail1.html')

def cooperation(request):
 
 return render(request, 'antiScam/cooperation.html')