# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.firstname'
        db.alter_column(u'game_user', 'firstname', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'User.lastname'
        db.alter_column(u'game_user', 'lastname', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'User.email'
        db.alter_column(u'game_user', 'email', self.gf('django.db.models.fields.CharField')(default='', max_length=100))
        # Adding field 'Choice.number'
        db.add_column(u'game_choice', 'number',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Choice.choice_text'
        db.alter_column(u'game_choice', 'choice_text', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'User.firstname'
        db.alter_column(u'game_user', 'firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'User.lastname'
        db.alter_column(u'game_user', 'lastname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'User.email'
        db.alter_column(u'game_user', 'email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Deleting field 'Choice.number'
        db.delete_column(u'game_choice', 'number')


        # Changing field 'Choice.choice_text'
        db.alter_column(u'game_choice', 'choice_text', self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 10, 16, 0, 0), max_length=200))

    models = {
        u'game.answer': {
            'Meta': {'object_name': 'Answer'},
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.Choice']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.Poll']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.User']"})
        },
        u'game.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'polls': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['game.Poll']", 'symmetrical': 'False'})
        },
        u'game.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.Poll']", 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'sequence': ('django.db.models.fields.SmallIntegerField', [], {}),
            'template': ('django.db.models.fields.TextField', [], {})
        },
        u'game.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'distinctive_signs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game']