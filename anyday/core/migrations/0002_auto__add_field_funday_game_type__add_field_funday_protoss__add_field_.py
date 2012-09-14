# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Funday.game_type'
        db.add_column('core_funday', 'game_type',
                      self.gf('django.db.models.fields.CharField')(default='individual', max_length=20),
                      keep_default=False)

        # Adding field 'Funday.protoss'
        db.add_column('core_funday', 'protoss',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Funday.terran'
        db.add_column('core_funday', 'terran',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Funday.zerg'
        db.add_column('core_funday', 'zerg',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Funday.game_type'
        db.delete_column('core_funday', 'game_type')

        # Deleting field 'Funday.protoss'
        db.delete_column('core_funday', 'protoss')

        # Deleting field 'Funday.terran'
        db.delete_column('core_funday', 'terran')

        # Deleting field 'Funday.zerg'
        db.delete_column('core_funday', 'zerg')


    models = {
        'core.funday': {
            'Meta': {'object_name': 'Funday'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'game_type': ('django.db.models.fields.CharField', [], {'default': "'individual'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'protoss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'terran': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zerg': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['core']