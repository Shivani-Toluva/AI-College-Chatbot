from django.db import models


class Intent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Response(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    answer = models.TextField()
    image = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.intent.name