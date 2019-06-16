# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core_user.models import User

class Note(models.Model):
	note_id = models.IntegerField(default=0)
	owner = models.CharField(max_length=30, default='undefined')
	name = models.CharField(max_length=200, null=True)
	tags = models.CharField(max_length=100, null=True)
	text = models.CharField(max_length=5000, null=True)
	author = models.CharField(max_length=50, default='undefined')
	created_date = models.DateTimeField(null=True)
	updated_timestamp = models.DateTimeField(null=True)
	status = models.BooleanField()

class Meta:
	db_table = u'Note'
	unique_together = (('note_id', 'owner'),)
