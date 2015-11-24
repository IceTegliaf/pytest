# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table('pingator_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('when', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pingator.Site'])),
            ('is_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('http_status', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('error_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pingator', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table('pingator_log')


    models = {
        'pingator.log': {
            'Meta': {'object_name': 'Log'},
            'error_text': ('django.db.models.fields.TextField', [], {}),
            'http_status': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pingator.Site']"}),
            'when': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'pingator.site': {
            'Meta': {'object_name': 'Site'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pingator']