from django.db import models

# As classes definem as tabelas e as variaveis as colunas da tabela

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('data published')


class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

# Create your models here.
