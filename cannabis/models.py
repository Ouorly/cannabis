from django.db import models

class ActiveSubstance(models.Model):
    name = models.CharField(max_length=150)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class AnimalType(models.Model):
    name = models.CharField(max_length=150)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    # class Meta:
    #     managed = False


class Disease(models.Model):
    icd10_field = models.IntegerField(default=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=150)

    # class Meta:
    #     managed = False

    def __str__(self):
        return self.name

class DiseaseSynonyms(models.Model):
    name = models.TextField()
    fk_disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.TextField()
    drug_bank = models.TextField(blank=True, null=True)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class DrugActive(models.Model):
    fk_drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    fk_active_substance = models.ForeignKey(ActiveSubstance, on_delete=models.CASCADE)

    class Meta:
        # managed = False
        unique_together = (('fk_drug', 'fk_active_substance'),)


class DrugSynonyms(models.Model):
    name_synonyms = models.TextField()
    fk_drug = models.ForeignKey(Drug, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name_synonyms

class Effect(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class Formation(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class Journal(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class PatientGroup(models.Model):
    fk_gender_id = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.CASCADE)
    number_of_patient = models.IntegerField(default=0, blank=True, null=True)
    combination = models.TextField(blank=True, null=True)
    second_condition = models.ForeignKey(Disease,blank=True, null=True, on_delete=models.CASCADE)
    years_min = models.CharField(blank=True, null=True, max_length=150)
    years_max = models.CharField(blank=True, null=True, max_length=150)

    # class Meta:
    #     managed = False


class Race(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class SideEffect(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class DiseaseSymptoms(models.Model):
    fk_disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    fk_symptoms = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.fk_disease

class TestType(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class TypeArticle(models.Model):
    name = models.TextField()

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.name

class TypeOfResearch(models.Model):
    name = models.TextField()

    def __str__(self):
        return  self.name
    # class Meta:
    #     managed = False


class AnimalTypePatient(models.Model):
    fk_animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    fk_patient_group = models.ForeignKey(PatientGroup, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    def __str__(self):
        return  self.fk_animal_type

class ArticleResearch(models.Model):
    fk_effect = models.ForeignKey(Effect, blank=True, null=True, on_delete=models.CASCADE)
    fk_drug = models.ForeignKey(Drug, blank=True, null=True, on_delete=models.CASCADE)
    fk_disease = models.ForeignKey(Disease, blank=True, null=True, on_delete=models.CASCADE) # Болезнь
    dosage = models.TextField( blank=True, null=True) #режим (2столбец)
    fk_formation = models.ForeignKey(Formation, blank=True, null=True, on_delete=models.CASCADE)
    fk_type_of_research = models.ForeignKey(TypeOfResearch, blank=True, null=True, on_delete=models.CASCADE) # Фильтр тип иследуемого
    regimen = models.TextField( blank=True, null=True)
    cell_type = models.TextField( blank=True, null=True)
    fk_animal_type = models.ForeignKey(AnimalType, blank=True, null=True, on_delete=models.CASCADE)
    fk_patient_group = models.ForeignKey(PatientGroup, blank=True, null=True, on_delete=models.CASCADE) #пациенты
    fk_side_effect = models.ForeignKey(SideEffect, blank=True, null=True, on_delete=models.CASCADE)#побочки (3 столбец)
    side_effect = models.TextField(blank=True, null=True)
    fk_gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.CASCADE)
    combination = models.TextField(blank=True, null=True)
    fk_second_condition = models.ForeignKey(Disease, blank=True, null=True, on_delete=models.CASCADE, related_name='second_condition')
    human_study_parameters = models.TextField(blank=True, null=True)
    years_min = models.TextField(blank=True, null=True)
    years_max = models.TextField(blank=True, null=True)
    number_of_pations = models.IntegerField(blank=True, null=True) # Число иследуемых

    # class Meta:
    #     managed = False

    def __str__(self):
        return "{}".format(self.fk_disease)


class Article(models.Model):
    name = models.CharField(max_length=300)
    pubmed = models.BigIntegerField(default=0, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    fk_journal = models.ForeignKey(Journal, blank=True, null=True, on_delete=models.CASCADE)
    keywords = models.TextField(blank=True, null=True)
    fk_article_research = models.ManyToManyField(ArticleResearch,blank=True, null=True)
    fk_author = models.ManyToManyField(Author,blank=True, null=True)

    # class Meta:
    #     managed = False
    def __str__(self):
        return "{}".format(self.name)

# class ArticleArticleResearch(models.Model):
#     fk_article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     fk_article_research = models.ForeignKey(ArticleResearch, on_delete=models.CASCADE)
#
#     #class Meta:
#         #db_table = 'article_article_research'
#
#     def __str__(self):
#         return self.fk_article

class ClinicalTrial(models.Model):
    dosage = models.TextField()
    fk_disease_id = models.ForeignKey(Disease, on_delete=models.CASCADE)
    fk_effect_id = models.ForeignKey(Effect, on_delete=models.CASCADE)
    fk_side_effect_id = models.ForeignKey(SideEffect, on_delete=models.CASCADE)
    fk_pation_group = models.ForeignKey(PatientGroup, on_delete=models.CASCADE)
    fk_drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    fk_formation_id = models.ForeignKey(Formation, on_delete=models.CASCADE)
    clin_study_type = models.TextField(blank=True, null=True)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.fk_disease_id

class DrugFormation(models.Model):
    fk_drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    fk_formation = models.ForeignKey(Formation, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    def __str__(self):
        return self.fk_drug