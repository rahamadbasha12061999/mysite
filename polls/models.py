from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.question_text}.{self.choice_text}"


class Email(models.Model):
    from_email = models.EmailField(help_text="From Email")
    to_email = models.EmailField(help_text="To Email")
    subject = models.CharField(max_length=500)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
