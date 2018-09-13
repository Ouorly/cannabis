from django import forms
from .models import TypeOfResearch, ArticleResearch

class SearchForm(forms.Form):
    """Форма поиска"""
    disease = forms.CharField()
    type_research = forms.ModelChoiceField(empty_label=None,
                                           required=False,
                                           error_messages={'required': ''},
                                           widget=forms.widgets.CheckboxSelectMultiple,
                                           queryset=TypeOfResearch.objects.all()
                                           )
    number_of_patients = forms.IntegerField(required=False, error_messages={'required': ''})

    # class Meta:
    #     model = ArticleResearch
    #     fields = ("fk_disease", "fk_type_of_research", "number_of_pations")
    #     widgets = {
    #         #"fk_disease": forms.CharField(),
    #         #"fk_type_of_research": forms.CheckboxSelectMultiple()
    #     }


class TypeResearchForm(forms.Form):
    """По типу"""
    type_research = forms.ModelChoiceField(empty_label=None,
                                           widget=forms.CheckboxSelectMultiple,
                                           queryset=TypeOfResearch.objects.all()
                                           )