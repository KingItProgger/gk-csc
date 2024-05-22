from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView
from django.shortcuts import render,redirect
from .models import Flat,House,News,Recall,Review,Room
from .forms import RecallForm,ReviewForm


class FlatsList(ListView):
    model = Flat
    template_name = 'main.html'
    context_object_name = 'flats'
    ordering = 'rooms'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FlatsList, self).get_context_data()
        context['news']=News.objects.all()
        context['rooms']=Room.objects.all()
        return context













#class FlatsList(ListView):
    #model = Flat
    #template_name = 'main.html'
    #context_object_name = 'flats'

    #def get_context_data(self,**kwargs):
        #form = RecallForm()
        #context=super().get_context_data(**kwargs)
        #context['form']=self.form
        #return context


class Flats_1_List(ListView):
    model = Flat
    template_name = 'main1.html'
    context_object_name = 'flats'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['news']=News.objects.all()
        context['rooms']=Room.objects.all()
        return context



class Flats_2_List(ListView):
    model = Flat
    template_name = 'main2.html'
    context_object_name = 'flats'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['news']=News.objects.all()
        context['rooms']=Room.objects.all()
        return context


class Flats_3_List(ListView):
    model = Flat
    template_name = 'main3.html'
    context_object_name = 'flats'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['news']=News.objects.all()
        context['rooms']=Room.objects.all()
        return context




class FlatDetail(DetailView):
    model = Flat
    template_name = 'flat.html'
    context_object_name = 'flat'

class NewsList(ListView):
    model = News
    ordering = 'datetime'
    template_name = 'news.html'
    context_object_name = 'news'
    ordering='-datetime'

class NewsDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'


class RecallView(CreateView):
    model = Recall
    form_class = RecallForm
    template_name = 'recall.html'
    context_object_name = 'recall'



class ReviewCreate(CreateView):
    form_class = ReviewForm
    model = Review
    template_name = 'responses.html'



def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contacts.html')

def sales(request):
    return render(request,'sales.html')

def building_plan(request):
    return render(request,'building_plan.html')

def credit_0(request):
    return render(request,'credit_0.html')

def price_list(request):
    return render(request,'price_list.html')



def faq(request):
    return render(request,'faq.html')

def credit_issues(request):
    return render(request,'credit_issues.html')

def pay_ways(request):
    return render(request,'pay_ways.html')

def reverse_call(request):
    return render(request,'reverse_call.html')

def law_inform(request):
    return render(request,'law_inform.html')

def docs(request):
    return render(request,'docs.html')

