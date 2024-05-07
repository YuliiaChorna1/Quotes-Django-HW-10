from datetime import datetime
from dataclasses import dataclass
from django.db import models
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateField, EmbeddedDocumentField, ListField, StringField, ReferenceField


class Tag(EmbeddedDocument):
    name = StringField()


class Authors(Document):
    fullname = StringField()
    born_date = DateField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Authors, reverse_delete_rule=2)
    quote = StringField()


class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.DateTimeField(null=False)
    born_location = models.CharField(null=False)
    description = models.CharField(null=False)

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    tags = models.CharField(null=False)
    author = models.CharField(null=False)
    quote = models.CharField(null=False)

    def __str__(self):
        return f"{self.name}"


@dataclass
class TagView:
    name: str
    quotes: list[Quotes]