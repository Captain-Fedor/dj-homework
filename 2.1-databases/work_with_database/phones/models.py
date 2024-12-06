from django.db import models

# В файле models.py нашего приложения создаём модель
# Phone с полями id, name, price, image, release_date, lte_exists и slug. Поле id — должно быть основным ключом модели.

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('name', max_length=50)
    image = models.URLField()
    # image = models.ImageField('image', upload_to='images/')
    price = models.IntegerField('price')
    release_date = models.DateField('release_date', auto_now=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField('slug', max_length=100, unique=True)


