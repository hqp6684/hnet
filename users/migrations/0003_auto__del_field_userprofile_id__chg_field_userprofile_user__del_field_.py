# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.id'
        db.delete_column(u'users_userprofile', u'id')


        # Changing field 'UserProfile.user'
        db.alter_column(u'users_userprofile', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True))
        # Deleting field 'Employee.id'
        db.delete_column(u'users_employee', u'id')


        # Changing field 'Employee.user'
        db.alter_column(u'users_employee', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True))
        # Deleting field 'Doctor.id'
        db.delete_column(u'users_doctor', u'id')


        # Changing field 'Doctor.user'
        db.alter_column(u'users_doctor', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.Employee'], unique=True, primary_key=True))
        # Deleting field 'Patient.id'
        db.delete_column(u'users_patient', u'id')


        # Changing field 'Patient.user'
        db.alter_column(u'users_patient', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True))
        # Deleting field 'Nurse.id'
        db.delete_column(u'users_nurse', u'id')


        # Changing field 'Nurse.user'
        db.alter_column(u'users_nurse', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.Employee'], unique=True, primary_key=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'UserProfile.id'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'UserProfile.id'
        db.add_column(u'users_userprofile', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'UserProfile.user'
        db.alter_column(u'users_userprofile', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # User chose to not deal with backwards NULL issues for 'Employee.id'
        raise RuntimeError("Cannot reverse this migration. 'Employee.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Employee.id'
        db.add_column(u'users_employee', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'Employee.user'
        db.alter_column(u'users_employee', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # User chose to not deal with backwards NULL issues for 'Doctor.id'
        raise RuntimeError("Cannot reverse this migration. 'Doctor.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Doctor.id'
        db.add_column(u'users_doctor', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'Doctor.user'
        db.alter_column(u'users_doctor', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.Employee'], unique=True))

        # User chose to not deal with backwards NULL issues for 'Patient.id'
        raise RuntimeError("Cannot reverse this migration. 'Patient.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Patient.id'
        db.add_column(u'users_patient', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'Patient.user'
        db.alter_column(u'users_patient', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # User chose to not deal with backwards NULL issues for 'Nurse.id'
        raise RuntimeError("Cannot reverse this migration. 'Nurse.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Nurse.id'
        db.add_column(u'users_nurse', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'Nurse.user'
        db.alter_column(u'users_nurse', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.Employee'], unique=True))

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
            'office': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.Employee']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.employee': {
            'Meta': {'object_name': 'Employee'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.nurse': {
            'Meta': {'object_name': 'Nurse'},
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.Employee']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.patient': {
            'Meta': {'object_name': 'Patient'},
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'dOB': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'default': "'xxx-xxx-xxxx'", 'max_length': '15', 'null': 'True'}),
            'sSN': ('django.db.models.fields.CharField', [], {'default': "'000-00-0000'", 'max_length': '11', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'streetAddress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': "'xxxxx'", 'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['users']