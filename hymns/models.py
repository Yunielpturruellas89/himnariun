from django.db import models

# Create your models here.
class Hymn(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(unique=True) # Assuming hymn numbers are unique
    author = models.CharField(max_length=255, blank=True, null=True)  # Allow null for unknown authors
    year = models.IntegerField(blank=True, null=True)  # Allow null for unknown years
    favorite = models.BooleanField(default=False)
    biblical_quote = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Verse(models.Model):
    hymn = models.ForeignKey(Hymn, on_delete=models.CASCADE, related_name='verses')
    type = models.CharField(max_length=50, choices=[('verse', 'Verse'), ('chorus', 'Chorus'), ('bridge', 'Bridge')], default='verse') # Add other verse types as needed

    def __str__(self):
        return f"Verse {self.pk} of {self.hymn.name}"


class Line(models.Model):
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name='lines')
    text = models.TextField()

    def __str__(self):
        return self.text[:50] # Show only the first 50 characters for brevity
