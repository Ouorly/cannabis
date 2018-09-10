from django.contrib import admin
from .models import (ActiveSubstance, AnimalType, AnimalTypePatient, Article, ArticleResearch, ArticleArticleResearch,
                     Author, ClinicalTrial, Disease, DiseaseSymptoms, DiseaseSynonyms, Drug, DrugActive, DrugFormation,
                     DrugSynonyms, Effect, Formation, Gender, Journal, PatientGroup, Race, SideEffect, Symptom, TestType,
                     TypeArticle, TypeOfResearch)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "date")

admin.site.register(ActiveSubstance)
admin.site.register(AnimalType)
admin.site.register(AnimalTypePatient)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleResearch)
admin.site.register(ArticleArticleResearch)
admin.site.register(Author)
admin.site.register(ClinicalTrial)
admin.site.register(Disease)
admin.site.register(DiseaseSymptoms)
admin.site.register(DiseaseSynonyms)
admin.site.register(Drug)
admin.site.register(DrugActive)
admin.site.register(DrugFormation)
admin.site.register(DrugSynonyms)
admin.site.register(Effect)
admin.site.register(Formation)
admin.site.register(Gender)
admin.site.register(Journal)
admin.site.register(PatientGroup)
admin.site.register(Race)
admin.site.register(SideEffect)
admin.site.register(Symptom)
admin.site.register(TestType)
admin.site.register(TypeArticle)
admin.site.register(TypeOfResearch)

