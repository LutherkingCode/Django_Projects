
# personne class
class Personne(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    enrollment_date = models.DateField()
    score = models.FloatField()
    is_succeed = models.BooleanField(default=False)

# Add a new personne to te data base
    person = models.Person.objects.create(
    first_name="luther",
    last_name="king",
    email="lutherkingsenat@yahoo.com",
    enrollment_date="2023-08-01",
    score=90,
    is_succeed=True
)

    

models.Personne.filter(models.Q(first_name__startswith='L') | models.Q(last_name__startswith='L'))

    
models.Personne.filter(score__gte=75).order_by('-score')


models.objects.filter(enrollment_date__lte='2020-12-12')


 person = models.Person.objects.create(
    first_name="luther",
    last_name="king",
    email="lutherkingsenat@yahoo.com",
    enrollment_date="2023-08-01",
    score=90,
    is_succeed=True)
    person.save()


