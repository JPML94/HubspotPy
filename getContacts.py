import json
import os

from hubspot3.contacts import ContactsClient
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUBSPOT_API_KEY")

client = ContactsClient(api_key=API_KEY)
contacts_data = client.get_all()

ids = []

for contact in contacts_data:
    ids.append(contact['id'])


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


contacts = []

for i in ids:
    contact_by_id = client.get_contact_by_id(i)
    try:
        email = contact_by_id['properties']['email']['value']
    except KeyError:
        email = ''
    try:
        emailHistory = contact_by_id['properties']['email']['versions']
    except KeyError:
        emailHistory = ''
    try:
        firstname = contact_by_id['properties']['firstname']['value']
    except KeyError:
        firstname = ''
    try:
        firstnameHistory = contact_by_id['properties']['firstname']['versions']
    except KeyError:
        firstnameHistory = ''
    try:
        lastname = contact_by_id['properties']['lastname']['value']
    except KeyError:
        lastname = ''
    try:
        lastnameHistory = contact_by_id['properties']['lastname']['versions']
    except KeyError:
        lastnameHistory = ''
    try:
        lifecyclestage = contact_by_id['properties']['lifecyclestage']['value']
    except KeyError:
        lifecyclestage = ''
    try:
        lifecyclestageHistory = contact_by_id['properties']['lifecyclestage']['versions']
    except KeyError:
        lifecyclestageHistory = ''
    try:
        website = contact_by_id['properties']['website']['value']
    except KeyError:
        website = ''
    try:
        websiteHistory = contact_by_id['properties']['website']['versions']
    except KeyError:
        websiteHistory = ''
    try:
        lead_source = contact_by_id['properties']['lead_source']['value']
    except KeyError:
        lead_source = ''
    try:
        lead_sourceHistory = contact_by_id['properties']['lead_source']['versions']
    except KeyError:
        lead_sourceHistory = ''
    try:
        jobtitle = contact_by_id['properties']['jobtitle']['value']
    except KeyError:
        jobtitle = ''
    try:
        jobtitleHistory = contact_by_id['properties']['jobtitle']['versions']
    except KeyError:
        jobtitleHistory = ''
    try:
        company = contact_by_id['properties']['company']['value']
    except KeyError:
        company = ''
    try:
        companyHistory = contact_by_id['properties']['company']['versions']
    except KeyError:
        companyHistory = ''
    try:
        notes_last_updated = contact_by_id['properties']['notes_last_updated']['value']
    except KeyError:
        notes_last_updated = ''
    try:
        notes_last_updatedHistory = contact_by_id['properties']['notes_last_updated']['versions']
    except KeyError:
        notes_last_updatedHistory = ''
    try:
        createdate = contact_by_id['properties']['createdate']['value']
    except KeyError:
        createdate = ''
    try:
        createdateHistory = contact_by_id['properties']['createdate']['versions']
    except KeyError:
        createdateHistory = ''
    try:
        slack_handle = contact_by_id['properties']['slack_handle']['value']
    except KeyError:
        slack_handle = ''
    try:
        slack_handleHistory = contact_by_id['properties']['slack_handle']['versions']
    except KeyError:
        slack_handleHistory = ''
    try:
        github = contact_by_id['properties']['github']['value']
    except KeyError:
        github = ''
    try:
        githubHistory = contact_by_id['properties']['github']['versions']
    except KeyError:
        githubHistory = ''
    try:
        medium = contact_by_id['properties']['medium']['value']
    except KeyError:
        medium = ''
    try:
        mediumHistory = contact_by_id['properties']['medium']['versions']
    except KeyError:
        mediumHistory = ''
    try:
        twitterhandle = contact_by_id['properties']['twitterhandle']['value']
    except KeyError:
        twitterhandle = ''
    try:
        twitterhandleHistory = contact_by_id['properties']['twitterhandle']['versions']
    except KeyError:
        twitterhandleHistory = ''
    try:
        linkedin = contact_by_id['properties']['linkedin']['value']
    except KeyError:
        linkedin = ''
    try:
        linkedinHistory = contact_by_id['properties']['linkedin']['versions']
    except KeyError:
        linkedinHistory = ''
    try:
        hs_analytics_last_url = contact_by_id['properties']['hs_analytics_last_url']['value']
    except KeyError:
        hs_analytics_last_url = ''
    try:
        hs_analytics_last_urlHistory = contact_by_id['properties']['hs_analytics_last_url']['versions']
    except KeyError:
        hs_analytics_last_urlHistory = ''
    try:
        num_conversion_events = contact_by_id['properties']['num_conversion_events']['value']
    except KeyError:
        num_conversion_events = ''
    try:
        num_conversion_eventsHistory = contact_by_id['properties']['num_conversion_events']['versions']
    except KeyError:
        num_conversion_eventsHistory = ''
    try:
        num_unique_conversion_events = contact_by_id['properties']['num_unique_conversion_events']['value']
    except KeyError:
        num_unique_conversion_events = ''
    try:
        num_unique_conversion_eventsHistory = contact_by_id[
            'properties']['num_unique_conversion_events']['versions']
    except KeyError:
        num_unique_conversion_eventsHistory = ''
    try:
        curriculum_grade = contact_by_id['properties']['curriculum_grade']['value']
    except KeyError:
        curriculum_grade = ''
    try:
        curriculum_gradeHistory = contact_by_id['properties']['curriculum_grade']['versions']
    except KeyError:
        curriculum_gradeHistory = ''
    try:
        curriculum_detailed_feedback = contact_by_id['properties']['curriculum_detailed_feedback']['value']
    except:
        curriculum_detailed_feedback = ''
    try:
        curriculum_detailed_feedbackHistory = contact_by_id[
            'properties']['curriculum_detailed_feedback']['versions']
    except KeyError:
        curriculum_detailed_feedbackHistory = ''
    try:
        project_grade = contact_by_id['properties']['project_grade']['value']
    except KeyError:
        project_grade = ''
    try:
        project_gradeHistory = contact_by_id['properties']['project_grade']['versions']
    except KeyError:
        project_gradeHistory = ''
    try:
        project_detailed_feedback = contact_by_id['properties']['project_detailed_feedback']['value']
    except:
        project_detailed_feedback = ''
    try:
        project_detailed_feedbackHistory = contact_by_id[
            'properties']['project_detailed_feedback']['versions']
    except KeyError:
        project_detailed_feedbackHistory = ''
    try:
        career_development_grade = contact_by_id['properties']['career_development_grade']['value']
    except KeyError:
        career_development_grade = ''
    try:
        career_development_gradeHistory = contact_by_id[
            'properties']['career_development_grade']['versions']
    except KeyError:
        career_development_gradeHistory = ''
    try:
        career_development_detailed_feedback = contact_by_id[
            'properties']['career_development_detailed_feedback']['value']
    except KeyError:
        career_development_detailed_feedback = ''
    try:
        career_development_detailed_feedbackHistory = contact_by_id[
            'properties']['career_development_detailed_feedback']['versions']
    except KeyError:
        career_development_detailed_feedbackHistory = ''
    try:
        overall_grade = contact_by_id['properties']['overall_grade']['value']
    except KeyError:
        overall_grade = ''
    try:
        overall_gradeHistory = contact_by_id['properties']['overall_grade']['versions']
    except KeyError:
        overall_gradeHistory = ''
    try:
        general_detailed_feedback = contact_by_id['properties']['general_detailed_feedback']['value']
    except KeyError:
        general_detailed_feedback = ''
    try:
        general_detailed_feedbackHistory = contact_by_id[
            'properties']['general_detailed_feedback']['versions']
    except KeyError:
        general_detailed_feedbackHistory = ''
    try:
        good_standing = contact_by_id['properties']['good_standing']['value']
    except KeyError:
        good_standing = ''
    try:
        good_standingHistory = contact_by_id['properties']['good_standing']['value']
    except KeyError:
        good_standingHistory = ''
    try:
        tc_cohort = contact_by_id['properties']['tc_cohort']['value']
    except KeyError:
        tc_cohort = ''
    try:
        tc_cohortHistory = contact_by_id['properties']['tc_cohort']['versions']
    except KeyError:
        tc_cohortHistory = ''
    try:
        tc_email = contact_by_id['properties']['tc_email']['value']
    except KeyError:
        tc_email = ''
    try:
        tc_emailHistory = contact_by_id['properties']['tc_email']['versions']
    except KeyError:
        tc_emailHistory = ''
    try:
        tc_grad_date = contact_by_id['properties']['tc_grad_date']['value']
    except KeyError:
        tc_grad_date = ''
    try:
        tc_grad_dateHistory = contact_by_id['properties']['tc_grad_date']['versions']
    except KeyError:
        tc_grad_dateHistory = ''
    try:
        tc_projects = contact_by_id['properties']['tc_projects']['value']
    except KeyError:
        tc_projects = ''
    try:
        tc_projectsHistory = contact_by_id['properties']['tc_projects']['versions']
    except KeyError:
        tc_projectsHistory = ''
    try:
        tc_start_date = contact_by_id['properties']['tc_start_date']['value']
    except KeyError:
        tc_start_date = ''
    try:
        tc_start_dateHistory = contact_by_id['properties']['tc_start_date']['versions']
    except KeyError:
        tc_start_dateHistory = ''
    try:
        tc_track = contact_by_id['properties']['tc_track']['value']
    except KeyError:
        tc_track = ''
    try:
        tc_trackHistory = contact_by_id['properties']['tc_track']['versions']
    except KeyError:
        tc_trackHistory = ''
    try:
        n140_character_bio = contact_by_id['properties']['n140_character_bio']['value']
    except KeyError:
        n140_character_bio = ''
    try:
        n140_character_bioHistory = contact_by_id['properties']['n140_character_bio']['versions']
    except KeyError:
        n140_character_bioHistory = ''
    try:
        mbti_types = contact_by_id['properties']['mbti_types']['value']
    except KeyError:
        mbti_types = ''
    try:
        mbti_typesHistory = contact_by_id['properties']['mbti_types']['versions']
    except KeyError:
        mbti_typesHistory = ''
    try:
        hs_eventbrite_lastregisteredevent = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredevent']['value']
    except KeyError:
        hs_eventbrite_lastregisteredevent = ''
    try:
        hs_eventbrite_lastregisteredeventHistory = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredevent']['versions']
    except KeyError:
        hs_eventbrite_lastregisteredeventHistory = ''
    try:
        hs_eventbrite_lastregisteredeventdate = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredeventdate']['value']
    except:
        hs_eventbrite_lastregisteredeventdate = ''
    try:
        hs_eventbrite_lastregisteredeventdateHistory = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredeventdate']['versions']
    except KeyError:
        hs_eventbrite_lastregisteredeventdateHistory = ''
    try:
        are_you_open_to_new_roles_ = contact_by_id['properties']['are_you_open_to_new_roles_']['value']
    except KeyError:
        are_you_open_to_new_roles_ = ''
    try:
        are_you_open_to_new_roles_History = contact_by_id[
            'properties']['are_you_open_to_new_roles_']['versions']
    except KeyError:
        are_you_open_to_new_roles_History = ''
    try:
        new_companies_reached_out = contact_by_id['properties']['new_companies_reached_out']['value']
    except KeyError:
        new_companies_reached_out = ''
    try:
        new_companies_reached_outHistory = contact_by_id[
            'properties']['new_companies_reached_out']['versions']
    except KeyError:
        new_companies_reached_outHistory = ''

    with open('data/{}.json'.format(i), 'w') as f:
        data = {
            "email": {"value": email, "history": emailHistory},
            "firstname": {"value": firstname, "history": firstnameHistory},
            "lastname": {"value": lastname, "history": lastnameHistory},
            "lifecycle-stage": {"value": lifecyclestage, "history": lifecyclestageHistory},
            "website": {"value": website, "history": websiteHistory},
            "lead-source": {"value": lead_source, "history": lead_sourceHistory},
            "job-title": {"value": jobtitle, "history": jobtitleHistory},
            "company_name": {"value": company, "history": companyHistory},
            "last-activity-date": {"value": notes_last_updated, "history": notes_last_updatedHistory},
            "created-date": {"value": createdate, "history": createdateHistory},
            "slack": {"value": slack_handle, "history": slack_handleHistory},
            "github": {"value": github, "history": githubHistory},
            "medium": {"value": medium, "history": mediumHistory},
            "twitter": {"value": twitterhandle, "history": twitterhandleHistory},
            "linkedin": {"value": linkedin, "history": linkedinHistory},
            "last-page-seen": {"value": hs_analytics_last_url, "history": hs_analytics_last_urlHistory},
            "num-forms-submitted": {"value": num_conversion_events, "history": num_conversion_eventsHistory},
            "num-unique-forms-submitted": {"value": num_unique_conversion_events, "history": num_unique_conversion_eventsHistory},
            "curriculum-grade": {"value": curriculum_grade, "history": curriculum_gradeHistory},
            "curriculum-detailed": {"value": curriculum_detailed_feedback, "history": curriculum_detailed_feedbackHistory},
            "project-grade": {"value": project_grade, "history": project_gradeHistory},
            'project-detailed': {"value": project_detailed_feedback, "history": project_detailed_feedbackHistory},
            "cardev-grade": {"value": career_development_grade, "history": career_development_gradeHistory},
            "cardev-detailed": {"value": career_development_detailed_feedback, "history": career_development_detailed_feedbackHistory},
            "general-grade": {"value": overall_grade, "history": overall_gradeHistory},
            "general-detailed": {"value": general_detailed_feedback, "history": general_detailed_feedbackHistory},
            "good-standing": {"value": good_standing, "history": good_standingHistory},
            "cohort": {"value": tc_cohort, "history": tc_cohortHistory},
            "tc-email": {"value": tc_email, "history": tc_emailHistory},
            "tc-grad-date": {"value": tc_grad_date, "history": tc_grad_dateHistory},
            "tc-projects": {"value": tc_projects, "history": tc_projectsHistory},
            "tc-start-date": {"value": tc_start_date, "history": tc_start_dateHistory},
            "track": {"value": tc_track, "history": tc_trackHistory},
            "bio": {"value": n140_character_bio, "history": n140_character_bioHistory},
            "mbti-type": {"value": mbti_types, "history": mbti_typesHistory},
            "last-registered-event": {"value": hs_eventbrite_lastregisteredevent, "history": hs_eventbrite_lastregisteredeventHistory},
            "last-registered-event-date": {"value": hs_eventbrite_lastregisteredeventdate, "history": hs_eventbrite_lastregisteredeventdateHistory},
            "job-search-mentality": {"value": are_you_open_to_new_roles_, "history": are_you_open_to_new_roles_History},
            "companies-reached": {"value": new_companies_reached_out, "history": new_companies_reached_outHistory}
        }
        json_data = json.dumps(data, default=set_default)
        print('data on file for {}'.format(i))
        f.write(json_data)
        f.close()
    contacts.append(contact_by_id)
