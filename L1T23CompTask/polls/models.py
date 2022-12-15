from django.db import models
# Create your models here.
class Question(models.Model):
    """
    Class model for poll questions 
    stored in db.sqlite3 relational 
    database.

    :param model modules, Model class: param called by function

    :rtype: string, poll question
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text