# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.auth_accepted'
        db.add_column(u'game_user', 'auth_accepted',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.modified_at'
        db.add_column(u'game_user', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 10, 23, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'User.badge_modified'
        db.add_column(u'game_user', 'badge_modified',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'User.firstname'
        db.alter_column(u'game_user', 'firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'User.lastname'
        db.alter_column(u'game_user', 'lastname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'User.email'
        db.alter_column(u'game_user', 'email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'User.auth_accepted'
        db.delete_column(u'game_user', 'auth_accepted')

        # Deleting field 'User.modified_at'
        db.delete_column(u'game_user', 'modified_at')

        # Deleting field 'User.badge_modified'
        db.delete_column(u'game_user', 'badge_modified')


        # Changing field 'User.firstname'
        db.alter_column(u'game_user', 'firstname', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'User.lastname'
        db.alter_column(u'game_user', 'lastname', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'User.email'
        db.alter_column(u'game_user', 'email', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

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
            'auth_accepted': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'badge_modified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'distinctive_signs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '1'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game']