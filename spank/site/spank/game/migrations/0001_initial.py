# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'game_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('distinctive_signs', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'game', ['User'])

        # Adding model 'Poll'
        db.create_table(u'game_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('template', self.gf('django.db.models.fields.TextField')()),
            ('sequence', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('next', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Poll'], null=True, blank=True)),
        ))
        db.send_create_signal(u'game', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'game_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'game', ['Choice'])

        # Adding M2M table for field polls on 'Choice'
        m2m_table_name = db.shorten_name(u'game_choice_polls')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('choice', models.ForeignKey(orm[u'game.choice'], null=False)),
            ('poll', models.ForeignKey(orm[u'game.poll'], null=False))
        ))
        db.create_unique(m2m_table_name, ['choice_id', 'poll_id'])

        # Adding model 'Answer'
        db.create_table(u'game_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.User'])),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Poll'])),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Choice'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'game', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'game_user')

        # Deleting model 'Poll'
        db.delete_table(u'game_poll')

        # Deleting model 'Choice'
        db.delete_table(u'game_choice')

        # Removing M2M table for field polls on 'Choice'
        db.delete_table(db.shorten_name(u'game_choice_polls'))

        # Deleting model 'Answer'
        db.delete_table(u'game_answer')


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
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game']