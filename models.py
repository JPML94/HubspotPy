import uuid
import os
import datetime

from utility import none_to_string, string_to_none

class FileManager(object):

    def hubspot_to_json(self):
        pass

    def json_to_db(self):
        pass


class User(object):

    def __init__(self):
        self.flask_id = uuid.uuid4()
        self.hub_id = int
        self.email = str
        self.track = str
        self.cohort = str
        self.photo = str
        self.hub_properties = dict
        self.slack_interactions = dict or list

    def __repr__(self):
        return "User()"

    def __str__(self):
        return "instance of User"

    def create_contact(self, id):
        FileManager.json_to_db(self)

    def create_contacts(self, ids):
        FileManager.hubspot_to_json(self)

    def num_versions(self):
        pass


class Admin(object):

    def __init__(self):
        self.flask_id = uuid.uuid4()
        self.hub_id = int
        self.email = str


class Cohort(object):

    def __init__(self):
        members = list 
        start_date = datetime._date_class.isocalendar
        end_date = datetime._date_class


class Track(object):

    def __init__(self):
        members = list
        instructors = list


class FormResponse(object):

    def __init__(self):
        pass

class FeedbackResponse(FormResponse):

    def __init__(self):
        pass