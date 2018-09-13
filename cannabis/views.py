from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.views.generic import View
from django.db.models import Q
from .forms import SearchForm
from .models import Article, ArticleResearch


class CannabisView(View):

    def get(self, request):
        form = SearchForm()
        #forms_type = TypeResearchForm()
        return render(request, 'cannabis/cannabis.html', {"form": form})

    def post(self, request):
        form = SearchForm(request.POST)
        #forms_type = TypeResearchForm(request.POST)
        #if forms_type.is_valid():

        #if form.is_valid():
        number = request.POST.get("number") #form.cleaned_data["number"]
        type_research = request.POST.getlist("type_research", None) #form.cleaned_data["type_research"]
        disease = request.POST.get("disease") #form.cleaned_data["disease"]
        #print(type_research)
        filt = []

        if number:
            num = Q()
            num &= Q(fk_article_research__number_of_pations__gte=number)
            filt.append(num)
        if type_research:
            type_r = Q()
            type_r &= Q(fk_article_research__fk_type_of_research__id__in=type_research)
            filt.append(type_r)
        posts = Article.objects.filter(Q(fk_article_research__fk_disease__name__istartswith=disease)).filter(*filt)
        print(posts)
        return render(request, 'cannabis/cannabis.html', {"form": form, "posts": posts})
        #else:
            #return HttpResponse("Error")

class PostViews(View):
    """Вывод статьи"""
    def get(self, request, pk):
        post = get_object_or_404(Article, id=pk)
        return render(request, 'cannabis/post-single.html', {"post": post})



def search_form(request):
    return render_to_response(request, 'cannabis/search-form.html')


