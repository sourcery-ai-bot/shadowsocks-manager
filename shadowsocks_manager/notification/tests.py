# -*- coding: utf-8 -*-

# py2.7 and py3 compatibility imports
from __future__ import unicode_literals
from __future__ import absolute_import

from django.test import TestCase

from . import models


# Create your tests here.
class NotificationTestCase(TestCase):
    fixtures = ['template.json']

    def test_template(self):
        for obj in models.Template.objects.all():
            self.assertTrue(obj.template)

    def test_template_account_created(self):
        pass  # todo

    def test_notify(self):
        message='Subject: shadowsocks test email\r\nTo: nobody@localhost\r\ndelete me.'
        self.assertTrue(models.Notify.sendmail(message, 'No Reply', 'noreply@localost'))
