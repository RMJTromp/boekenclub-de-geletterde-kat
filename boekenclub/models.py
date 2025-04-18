from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='approved_books'
    )

    def __str__(self):
        return f"{self.title} door {self.author}"

    def average_score(self):
        reads = self.read_set.all()
        if reads.exists():
            return round(sum(r.score for r in reads) / reads.count(), 2)
        return None

    def read_count(self):
        return self.read_set.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio_text = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profiel van {self.user.username}"


class Read(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    SCORE_CHOICES = [(i, str(i)) for i in range(1, 6)]
    score = models.IntegerField(choices=SCORE_CHOICES)

    class Meta:
        unique_together = ('book', 'user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} las {self.book.title} op {self.date} (score: {self.score})"
