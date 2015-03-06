# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.city'
        db.alter_column(u'users_userprofile', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'UserProfile.zipcode'
        db.alter_column(u'users_userprofile', 'zipcode', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'UserProfile.streetAddress'
        db.alter_column(u'users_userprofile', 'streetAddress', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'UserProfile.state'
        db.alter_column(u'users_userprofile', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'UserProfile.sSN'
        db.alter_column(u'users_userprofile', 'sSN', self.gf('django.db.models.fields.CharField')(max_length=11))

        # Changing field 'UserProfile.email'
        db.alter_column(u'users_userprofile', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75))
        # Adding field 'Doctor.office'
        db.add_column(u'users_doctor', 'office',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'UserProfile.city'
        db.alter_column(u'users_userprofile', 'city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'UserProfile.zipcode'
        db.alter_column(u'users_userprofile', 'zipcode', self.gf('django.db.models.fields.CharField')(max_length=5, null=True))

        # Changing field 'UserProfile.streetAddress'
        db.alter_column(u'users_userprofile', 'streetAddress', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'UserProfile.state'
        db.alter_column(u'users_userprofile', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'UserProfile.sSN'
        db.alter_column(u'users_userprofile', 'sSN', self.gf('django.db.models.fields.CharField')(max_length=11, null=True))

        # Changing field 'UserProfile.email'
        db.alter_column(u'users_userprofile', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))
        # Deleting field 'Doctor.office'
        db.delete_column(u'users_doctor', 'office')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.doctor': {
            'Meta': {'object_name': 'Doctor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.Employee']", 'unique': 'True'})
        },
        u'users.employee': {
            'Meta': {'object_name': 'Employee'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'users.nurse': {
            'Meta': {'object_name': 'Nurse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.Employee']", 'unique': 'True'})
        },
        u'users.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'dOB': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'default': "'xxx-xxx-xxxx'", 'max_length': '15', 'null': 'True'}),
            'sSN': ('django.db.models.fields.CharField', [], {'default': "'000-00-0000'", 'max_length': '11', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'streetAddress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': "'xxxxx'", 'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['users']