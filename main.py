import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Thesis(ndb.Model):
    thesis_title = ndb.StringProperty(indexed=False)
    thesis_desc = ndb.StringProperty(indexed=False)
    thesis_date = ndb.StringProperty(indexed=False)
    thesis_status = ndb.StringProperty(indexed=False)

class ThesisSuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('thesis_success.html')
        self.response.write(template.render(template_values))

class ThesisEsuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('thesis_esuccess.html')
        self.response.write(template.render(template_values))

class ThesisListHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        thesiss = Thesis.query().fetch()
        template_values = {
            "all_thesis": thesiss,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('thesis_list.html')
        self.response.write(template.render(template_values))

class ThesisNewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('thesis_new.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self):
        thesis = Thesis()
        thesis.thesis_title = self.request.get('thesis_title')
        thesis.thesis_desc = self.request.get('thesis_desc')
        thesis.thesis_date = self.request.get('thesis_date')
        thesis.thesis_status = self.request.get('thesis_status')
        thesis.put()
        self.redirect('/thesis/success')

class ThesisViewHandler(webapp2.RequestHandler):
    def get(self, tid):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        thesi = Thesis.query().fetch()
        template_values = {
            "urlid": tid,
            "all_thesi": thesi,
            "url":url,
            "urlname":urlname,
            "name":name
        }
        template = JINJA_ENVIRONMENT.get_template('thesis_view.html')
        self.response.write(template.render(template_values))

class ThesisEditHandler(webapp2.RequestHandler):
    def get(self, tid):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
            thesis = Thesis.query().fetch()
            template_values = {
            "urlid": tid,
            "all_thesis": thesis,
            "url":url,
            "urlname":urlname,
            "name":name
            }
            template = JINJA_ENVIRONMENT.get_template('thesis_edit.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self, tid):
        thesis = Thesis()
        thesis = Thesis.get_by_id(long(tid))
        thesis.thesis_title = self.request.get('thesis_title')
        thesis.thesis_desc = self.request.get('thesis_desc')
        thesis.thesis_date = self.request.get('thesis_date')
        thesis.thesis_status = self.request.get('thesis_status')
        thesis.put()
        self.redirect('/thesis/esuccess')



class Student(ndb.Model):
    student_fname = ndb.StringProperty(indexed=False)
    student_lname = ndb.StringProperty(indexed=False)
    student_email = ndb.StringProperty(indexed=False)
    student_number = ndb.StringProperty(indexed=False)

class StudentSuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('student_success.html')
        self.response.write(template.render(template_values))

class StudentEsuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('student_esuccess.html')
        self.response.write(template.render(template_values))

class StudentListHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        student = Student.query().fetch()
        template_values = {
            "all_student": student,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('student_list.html')
        self.response.write(template.render(template_values))

class StudentNewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('student_new.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self):
        student = Student()
        student.student_fname = self.request.get('student_fname')
        student.student_lname = self.request.get('student_lname')
        student.student_email = self.request.get('student_email')
        student.student_number = self.request.get('student_number')
        student.put()
        self.redirect('/student/success')

class StudentViewHandler(webapp2.RequestHandler):
    def get(self, tid):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        student = Student.query().fetch()
        template_values = {
            "urlid": tid,
            "all_student": student,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('student_view.html')
        self.response.write(template.render(template_values))

class StudentEditHandler(webapp2.RequestHandler):
    def get(self, tid):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
            student = Student.query().fetch()
            template_values = {
            "urlid": tid,
            "all_student": student,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('student_edit.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self, tid):
        student = Student()
        student = Student.get_by_id(long(tid))
        student.student_fname = self.request.get('student_fname')
        student.student_lname = self.request.get('student_lname')
        student.student_email = self.request.get('student_email')
        student.student_number = self.request.get('student_number')
        student.put()
        self.redirect('/student/esuccess')

class Adviser(ndb.Model):
    adviser_title = ndb.StringProperty(indexed=False)
    adviser_fname = ndb.StringProperty(indexed=False)
    adviser_lname = ndb.StringProperty(indexed=False)
    adviser_email = ndb.StringProperty(indexed=False)
    adviser_number = ndb.StringProperty(indexed=False)
    adviser_dept = ndb.StringProperty(indexed=False)

class AdviserSuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('adviser_success.html')
        self.response.write(template.render(template_values))

class AdviserEsuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('adviser_esuccess.html')
        self.response.write(template.render(template_values))

class AdviserListHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        adviser = Adviser.query().fetch()
        template_values = {
            "all_adviser": adviser,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('adviser_list.html')
        self.response.write(template.render(template_values))

class AdviserNewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('adviser_new.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))
    def post(self):
        adviser = Adviser()
        adviser.adviser_title = self.request.get('adviser_title')
        adviser.adviser_fname = self.request.get('adviser_fname')
        adviser.adviser_lname = self.request.get('adviser_lname')
        adviser.adviser_email = self.request.get('adviser_email')
        adviser.adviser_number = self.request.get('adviser_number')
        adviser.adviser_dept = self.request.get('adviser_dept')
        adviser.put()
        self.redirect('/adviser/success')

class AdviserViewHandler(webapp2.RequestHandler):
    def get(self, tid):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        adviser = Adviser.query().fetch()
        template_values = {
            "urlid": tid,
            "all_adviser": adviser,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('adviser_view.html')
        self.response.write(template.render(template_values))

class AdviserEditHandler(webapp2.RequestHandler):
    def get(self, tid):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Logged in as '+user.nickname()
            adviser = Adviser.query().fetch()
            template_values = {
            "urlid": tid,
            "all_adviser": adviser,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('adviser_edit.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self, tid):
        adviser = Adviser()
        adviser = Adviser.get_by_id(long(tid))
        adviser.adviser_title = self.request.get('adviser_title')
        adviser.adviser_fname = self.request.get('adviser_fname')
        adviser.adviser_lname = self.request.get('adviser_lname')
        adviser.adviser_email = self.request.get('adviser_email')
        adviser.adviser_number = self.request.get('adviser_number')
        adviser.adviser_dept = self.request.get('adviser_dept')
        adviser.put()
        self.redirect('/adviser/esuccess')

application = webapp2.WSGIApplication([
    ('/thesis/new', ThesisNewHandler),
    ('/thesis/list', ThesisListHandler),
    ('/thesis/success', ThesisSuccessPageHandler),
    ('/thesis/view/([^/]+)', ThesisViewHandler),
    ('/thesis/edit/([^/]+)', ThesisEditHandler),
    ('/thesis/esuccess', ThesisEsuccessPageHandler),
    ('/student/new', StudentNewHandler),
    ('/student/list', StudentListHandler),
    ('/student/success', StudentSuccessPageHandler),
    ('/student/view/([^/]+)', StudentViewHandler),
    ('/student/edit/([^/]+)', StudentEditHandler),
    ('/student/esuccess', StudentEsuccessPageHandler),
    ('/adviser/new', AdviserNewHandler),
    ('/adviser/list', AdviserListHandler),
    ('/adviser/success', AdviserSuccessPageHandler),
    ('/adviser/view/([^/]+)', AdviserViewHandler),
    ('/adviser/edit/([^/]+)', AdviserEditHandler),
    ('/adviser/esuccess', AdviserEsuccessPageHandler)
], debug=True)









