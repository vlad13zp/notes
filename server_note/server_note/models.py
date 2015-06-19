from django.db import models

"""
Model Tag
Have fields of name and access to user
"""


class Tag(models.Model):
    tag_name = models.CharField(max_length=32)
    access = models.IntegerField()

    def __unicode__(self):
        return '{0} ({1})'.format(self.tag_name, self.access)
"""
Model Color
Have two same fields and one to idenify color
"""


class Color(models.Model):
    color_name = models.CharField(max_length=32)
    hex_stat = models.CharField(max_length=32)
    access = models.IntegerField()

    def __unicode__(self):
        return '{0} (panel-{1})'.format(self.color_name, self.hex_stat)
"""
Model Category
Same fields
"""


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    access = models.IntegerField()

    def __unicode__(self):
        return '{0} ({1})'.format(self.category_name, self.access)
"""
Model User
Own model of user
"""


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    id_tag = models.ManyToManyField(Tag)
    id_color = models.ManyToManyField(Color)
    id_category = models.ManyToManyField(Category)

    def __unicode__(self):
        return 'User - {0}'.format(self.email)
"""
Model Note
Main model for our notes
"""


class Note(models.Model):
    id_user = models.ForeignKey(User)
    subject = models.CharField(max_length=32)
    message = models.CharField(max_length=100)
    date_create = models.DateTimeField(null=True)
    id_tag = models.ManyToManyField(Tag)
    id_color = models.ForeignKey(Color)
    id_category = models.ForeignKey(Category)
    files = models.FileField(upload_to='files/', null=True)

    def __unicode__(self):
        return '{0} / {1}'.format(self.id_user, self.subject)
