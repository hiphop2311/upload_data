# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
class Data(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    # data_file_name = models.CharField(max_length=255, )
    # metadata_file_name = models.CharField(max_length=255, )
    # province = models.CharField(max_length=100)  # จังหวัด
    # department = models.CharField(max_length=100)  # หน่วยงานให้ข้อมูล
    # uploader_name = models.CharField(max_length=100)  # ชื่อ-สกุล ผู้อัพโหลดข้อมูล
    # email = models.EmailField()  # อีเมล
    # uploaded_at = models.DateTimeField(auto_now_add=True)  # วันอัพโหลดข้อมูล
    # data_type = models.CharField(max_length=100)  # ประเภทข้อมูล
    # data_char = models.CharField(max_length=100)  # ลักษณะข้อมูล
    # age_range = models.CharField(max_length=100)  # ช่วงอายุ
    # description = models.CharField(max_length=255, blank=True)
    # upload_date = models.DateField('%d/%m/%Y')
    # created_at = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    # updated_at = models.DateTimeField('%d/%m/%Y %H:%M:%S')
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)
