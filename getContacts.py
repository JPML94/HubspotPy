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
        annualRevenue = contact_by_id['properties']['annualrevenue']['value']
    except KeyError:
        annualRevenue = None
    try:
        annualRevenueHistory = contact_by_id['properties']['annualrevenue']['versions']
    except KeyError:
        annualRevenueHistory = None
    try:
        associatedDeals = contact_by_id['properties']['num_associated_deals']['value']
    except KeyError:
        associatedDeals = None
    try:
        associatedDealsHistory = contact_by_id['properties']['num_associated_deals']['versions']
    except KeyError:
        associatedDealsHistory = None
    try:
        bayAreaAddress = contact_by_id['properties']['bay_area_address']['value']
    except KeyError:
        bayAreaAddress = None
    try:
        bayAreaAddressHistory = contact_by_id['properties']['bay_area_address']['versions']
    except KeyError:
        bayAreaAddressHistory = None
    try:
        becameCustomer = contact_by_id['properties']['hs_lifecyclestage_customer_date']['value']
    except KeyError:
        becameCustomer = None
    try:
        becameCustomerHistory = contact_by_id['properties']['hs_lifecyclestage_customer_date']['versions']
    except KeyError:
        becameCustomerHistory = None
    try:
        becameLead = contact_by_id['properties']['hs_lifecyclestage_lead_date']['value']
    except KeyError:
        becameLead = None
    try:
        becameLeadHistory = contact_by_id['properties']['hs_lifecyclestage_lead_date']['versions']
    except KeyError:
        becameLeadHistory = None
    try:
        becameMarketingQualifiedLead = contact_by_id['properties']['hs_lifecyclestage_marketingqualifiedlead_date']['value']
    except KeyError:
        becameMarketingQualifiedLead = None
    try:
        becameMarketingQualifiedLeadHistory = contact_by_id['properties']['hs_lifecyclestage_marketingqualifiedlead_date']['versions']
    except KeyError:
        becameMarketingQualifiedLeadHistory = None
    try:
        becameSalesQualifiedLead = contact_by_id['properties']['hs_lifecyclestage_salesqualifiedlead_date']['value']
    except KeyError:
        becameSalesQualifiedLead = None
    try:
        becameSalesQualifiedLeadHistory = contact_by_id['properties']['hs_lifecyclestage_salesqualifiedlead_date']['versions']
    except KeyError:
        becameSalesQualifiedLeadHistory = None
    try:
        becameSubscriber = contact_by_id['properties']['hs_lifecyclestage_subscriber_date']['value']
    except KeyError:
        becameSubscriber = None
    try:
        becameSubscriberHistory = contact_by_id['properties']['hs_lifecyclestage_subscriber_date']['versions']
    except KeyError:
        becameSubscriberHistory = None
    try:
        becameEvangelist = contact_by_id['properties']['hs_lifecyclestage_evangelist_date']['value']
    except KeyError:
        becameEvangelist = None
    try:
        becameEvangelistHistory = contact_by_id['properties']['hs_lifecyclestage_evangelist_date']['versions']
    except KeyError:
        becameEvangelistHistory = None
    try:
        becameOportunity = contact_by_id['properties']['hs_lifecyclestage_opportunity_date']['value']
    except KeyError:
        becameOportunity = None
    try:
        becameOportunityHistory = contact_by_id['properties']['hs_lifecyclestage_opportunity_date']['versions']
    except KeyError:
        becameOportunityHistory = None
    try:
        becameOther = contact_by_id['properties']['hs_lifecyclestage_other_date']['value']
    except KeyError:
        becameOther = None
    try:
        becameOtherHistory = contact_by_id['properties']['hs_lifecyclestage_other_date']['versions']
    except KeyError:
        becameOtherHistory = None
    try:
        city = contact_by_id['properties']['city']['value']
    except KeyError:
        city = None
    try:
        cityHistory = contact_by_id['properties']['city']['versions']
    except KeyError:
        cityHistory = None
    try:
        closeDate = contact_by_id['properties']['closedate']['value']
    except KeyError:
        closeDate = None
    try:
        closeDateHistory = contact_by_id['properties']['closedate']['versions']
    except KeyError:
        closeDateHistory = None
    try:
        closestFriend = contact_by_id['properties']['closest_friend_name']['value']
    except KeyError:
        closestFriend = None
    try:
        closestFriendHistory = contact_by_id['properties']['closest_friend_name']['versions']
    except KeyError:
        closestFriendHistory = None
    try:
        closestFriendNumber = contact_by_id['properties']['closest_friend_number']['value']
    except KeyError:
        closestFriendNumber = None
    try:
        closestFriendNumberHistory = contact_by_id['properties']['closest_friend_number']['versions']
    except KeyError:
        closestFriendNumberHistory = None
    try:
        contactOwnerID = contact_by_id['properties']['hubspot_owner_id']['value']
    except KeyError:
        contactOwnerID = None
    try:
        contactOwnerIDHistory = contact_by_id['properties']['hubspot_owner_id']['versions']
    except KeyError:
        contactOwnerIDHistory = None
    try:
        contactPriority = contact_by_id['properties']['hs_predictivescoringtier']['value']
    except KeyError:
        contactPriority = None
    try:
        contactPriorityHistory = contact_by_id['properties']['hs_predictivescoringtier']['versions']
    except KeyError:
        contactPriorityHistory = None
    try:
        contactType = contact_by_id['properties']['contact_type']['value']
    except KeyError:
        contactType = None
    try:
        contactTypeHistory = contact_by_id['properties']['contact_type']['versions']
    except KeyError:
        contactTypeHistory = None
    try:
        country = contact_by_id['properties']['country']['value']
    except KeyError:
        country = None
    try:
        countryHistory = contact_by_id['properties']['country']['versions']
    except KeyError:
        countryHistory = None
    try:
        currentLocation = contact_by_id['properties']['current_location']['value']
    except KeyError:
        currentLocation = None
    try:
        currentLocationHistory = contact_by_id['properties']['current_location']['versions']
    except KeyError:
        currentLocationHistory = None
    try:
        currentWorkEmail = contact_by_id['properties']['current_work_email']['value']
    except KeyError:
        currentWorkEmail = None
    try:
        currentWorkEmailHistory = contact_by_id['properties']['current_work_email']['versions']
    except KeyError:
        currentWorkEmailHistory = None
    try:
        currentlyInSequence = contact_by_id['properties']['hs_sequences_is_enrolled']['value']
    except KeyError:
        currentlyInSequence = None
    try:
        currentlyInSequenceHistory = contact_by_id['properties']['hs_sequences_is_enrolled']['versions']
    except KeyError:
        currentlyInSequenceHistory = None
    try:
        daysToClose = contact_by_id['properties']['days_to_close']['value']
    except KeyError:
        daysToClose = None
    try:
        daysToCloseHistory = contact_by_id['properties']['days_to_close']['versions']
    except KeyError:
        daysToCloseHistory = None
    try:
        emergencyContactEmail = contact_by_id['properties']['emergency_contact_email']['value']
    except KeyError:
        emergencyContactEmail = None
    try:
        emergencyContactEmailHistory = contact_by_id['properties']['emergency_contact_email']['versions']
    except KeyError:
        emergencyContactEmailHistory = None
    try:
        emergencyContactLocation = contact_by_id['properties']['emergency_contact_location']['value']
    except KeyError:
        emergencyContactLocation = None
    try:
        emergencyContactLocationHistory = contact_by_id['properties']['emergency_contact_location']['versions']
    except KeyError:
        emergencyContactLocationHistory = None
    try:
        emergencyContactName = contact_by_id['properties']['emergency_contact_name']['value']
    except KeyError:
        emergencyContactName = None
    try:
        emergencyContactNameHistory = contact_by_id['properties']['emergency_contact_name']['versions']
    except KeyError:
        emergencyContactNameHistory = None
    try:
        emergencyContactNumber = contact_by_id['properties']['emergency_contact_number']['value']
    except KeyError:
        emergencyContactNumber = None
    try:
        emergencyContactNumberHistory = contact_by_id['properties']['emergency_contact_number']['versions']
    except KeyError:
        emergencyContactNumberHistory = None
    try:
        fax = contact_by_id['properties']['fax']['value']
    except KeyError:
        fax = None
    try:
        faxHistory = contact_by_id['properties']['fax']['versions']
    except KeyError:
        faxHistory = None
    try:
        firstDealDate = contact_by_id['properties']['first_deal_created_date']['value']
    except KeyError:
        firstDealDate = None
    try:
        firstDealDateHistory = contact_by_id['properties']['first_deal_created_date']['versions']
    except KeyError:
        firstDealDateHistory = None
    try:
        hubspotScore = contact_by_id['properties']['hubspotscore']['value']
    except KeyError:
        hubspotScore = None
    try:
        hubspotScoreHistory = contact_by_id['properties']['hubspotscore']['versions']
    except KeyError:
        hubspotScoreHistory = None
    try:
        hubspotTeam = contact_by_id['properties']['hubspot_team_id']['value']
    except KeyError:
        hubspotTeam = None
    try:
        hubspotTeamHistory = contact_by_id['properties']['hubspot_team_id']['versions']
    except KeyError:
        hubspotTeamHistory = None
    try:
        industry = contact_by_id['properties']['industry']['value']
    except KeyError:
        industry = None
    try:
        industryHistory = contact_by_id['properties']['industry']['versions']
    except KeyError:
        industryHistory = None
    try:
        ipAddress = contact_by_id['properties']['ipaddress']['value']
    except KeyError:
        ipAddress = None
    try:
        ipAddressHistory = contact_by_id['properties']['ipaddress']['versions']
    except KeyError:
        ipAddressHistory = None
    try:
        lastContacted = contact_by_id['properties']['notes_last_contacted']['value']
    except KeyError:
        lastContacted = None
    try:
        lastContactedHistory = contact_by_id['properties']['notes_last_contacted']['versions']
    except KeyError:
        lastContactedHistory = None
    try:
        lastMeetingBooked = contact_by_id['properties']['engagements_last_meeting_booked']['value']
    except KeyError:
        lastMeetingBooked = None
    try:
        lastMeetingBookedHistory = contact_by_id['properties']['engagements_last_meeting_booked']['versions']
    except KeyError:
        lastMeetingBookedHistory = None
    try:
        lastMeetingBookedCampaign = contact_by_id['properties']['engagements_last_meeting_booked_campaign']['value']
    except KeyError:
        lastMeetingBookedCampaign = None
    try:
        lastMeetingBookedCampaignHistory = contact_by_id['properties']['engagements_last_meeting_booked_campaign']['versions']
    except KeyError:
        lastMeetingBookedCampaignHistory = None
    try:
        lastMeetingBookedMedium = contact_by_id['properties']['engagements_last_meeting_booked_medium']['value']
    except KeyError:
        lastMeetingBookedMedium = None
    try:
        lastMeetingBookedMediumHistory = contact_by_id['properties']['engagements_last_meeting_booked_medium']['versions']
    except KeyError:
        lastMeetingBookedMediumHistory = None
    try:
        lastMeetingBookedSource = contact_by_id['properties']['engagements_last_meeting_booked_source']['value']
    except KeyError:
        lastMeetingBookedSource = None
    try:
        lastMeetingBookedSourceHistory = contact_by_id['properties']['engagements_last_meeting_booked_source']['versions']
    except KeyError:
        lastMeetingBookedSourceHistory = None
    try:
        lastModifiedDate = contact_by_id['properties']['lastmodifieddate']['value']
    except KeyError:
        lastModifiedDate = None
    try:
        lastModifiedDateHistory = contact_by_id['properties']['lastmodifieddate']['versions']
    except KeyError:
        lastModifiedDateHistory = None
    try:
        leadStatus = contact_by_id['properties']['hs_lead_status']['value']
    except KeyError:
        leadStatus = None
    try:
        leadStatusHistory = contact_by_id['properties']['hs_lead_status']['versions']
    except KeyError:
        leadStatusHistory = None
    try:
        legalBasis = contact_by_id['properties']['hs_legal_basis']['value']
    except KeyError:
        legalBasis = None
    try:
        legalBasisHistory = contact_by_id['properties']['hs_legal_basis']['versions']
    except KeyError:
        legalBasisHistory = None
    try:
        legalName = contact_by_id['properties']['legal_name']['value']
    except KeyError:
        legalName = None
    try:
        legalNameHistory = contact_by_id['properties']['legal_name']['versions']
    except KeyError:
        legalNameHistory = None
    try:
        closingLikelihood = contact_by_id['properties']['hs_predictivecontactscore_v2']['value']
    except KeyError:
        closingLikelihood = None
    try:
        closingLikelihoodHistory = contact_by_id['properties']['hs_predictivecontactscore_v2']['versions']
    except KeyError:
        closingLikelihoodHistory = None
    try:
        message = contact_by_id['properties']['message']['value']
    except KeyError:
        message = None
    try:
        messageHistory = contact_by_id['properties']['message']['versions']
    except KeyError:
        messageHistory = None
    try:
        mobilePhone = contact_by_id['properties']['mobilephone']['value']
    except KeyError:
        mobilePhone = None
    try:
        mobilePhoneHistory = contact_by_id['properties']['mobilephone']['versions']
    except KeyError:
        mobilePhoneHistory = None
    try:
        nextActivityDate = contact_by_id['properties']['notes_next_activity_date']['value']
    except KeyError:
        nextActivityDate = None
    try:
        nextActivityDateHistory = contact_by_id['properties']['notes_next_activity_date']['versions']
    except KeyError:
        nextActivityDateHistory = None
    try:
        numOfEmployees = contact_by_id['properties']['numemployees']['value']
    except KeyError:
        numOfEmployees = None
    try:
        numOfEmployeesHistory = contact_by_id['properties']['numemployees']['versions']
    except KeyError:
        numOfEmployeesHistory = None
    try:
        numSalesActivities = contact_by_id['properties']['num_notes']['value']
    except KeyError:
        numSalesActivities = None
    try:
        numSalesActivitiesHistory = contact_by_id['properties']['num_notes']['versions']
    except KeyError:
        numSalesActivitiesHistory = None
    try:
        numTimesContacted = contact_by_id['properties']['num_contacted_notes']['value']
    except KeyError:
        numTimesContacted = None
    try:
        numTimesContactedHistory = contact_by_id['properties']['num_contacted_notes']['versions']
    except KeyError:
        numTimesContactedHistory = None
    try:
        compensationOptions = contact_by_id['properties']['offer_letter_compensation_options']['value']
    except KeyError:
        compensationOptions = None
    try:
        compensationOptionsHistory = contact_by_id['properties']['offer_letter_compensation_options']['versions']
    except KeyError:
        compensationOptionsHistory = None
    try:
        managerTimeAtCompany = contact_by_id['properties']['offer_letter_manager_time_at_company']['value']
    except KeyError:
        managerTimeAtCompany = None
    try:
        managerTimeAtCompanyHistory = contact_by_id['properties']['offer_letter_manager_time_at_company']['versions']
    except KeyError:
        managerTimeAtCompanyHistory = None
    try:
        nameOfManager = contact_by_id['properties']['offer_letter_name_of_manager']['value']
    except KeyError:
        nameOfManager = None
    try:
        nameOfManagerHistory = contact_by_id['properties']['offer_letter_name_of_manager']['versions']
    except KeyError:
        nameOfManagerHistory = None
    try:
        numOfDirectReports = contact_by_id['properties']['offer_letter_number_of_direct_reports']['value']
    except KeyError:
        numOfDirectReports = None
    try:
        numOfDirectReportsHistory = contact_by_id['properties']['offer_letter_number_of_direct_reports']['versions']
    except KeyError:
        numOfDirectReportsHistory = None
    try:
        numOfEmployeesOfferLetter = contact_by_id['properties']['offer_letter_number_of_employees']['value']
    except KeyError:
        numOfEmployeesOfferLetter = None
    try:
        numOfEmployeesOfferLetterHistory = contact_by_id['properties']['offer_letter_number_of_employees']['versions']
    except KeyError:
        numOfEmployeesOfferLetterHistory = None
    try:
        paymentTiming3 = contact_by_id['properties']['offer_letter_payment_timing_3']['value']
    except KeyError:
        paymentTiming3 = None
    try:
        paymentTiming3History = contact_by_id['properties']['offer_letter_payment_timing_3']['versions']
    except KeyError:
        paymentTiming3History = None
    try:
        positionTitle = contact_by_id['properties']['offer_letter_position_title']['value']
    except KeyError:
        positionTitle = None
    try:
        positionTitleHistory = contact_by_id['properties']['offer_letter_position_title']['versions']
    except KeyError:
        positionTitleHistory = None
    try:
        ownerAssignedDate = contact_by_id['properties']['hubspot_owner_assigneddate']['value']
    except KeyError:
        ownerAssignedDate = None
    try:
        ownerAssignedDateHistory = contact_by_id['properties']['hubspot_owner_assigneddate']['versions']
    except KeyError:
        ownerAssignedDateHistory = None
    try:
        permanentAddress = contact_by_id['properties']['permanent_address']['value']
    except KeyError:
        permanentAddress = None
    try:
        permanentAddressHistory = contact_by_id['properties']['permanent_address']['versions']
    except KeyError:
        permanentAddressHistory = None
    try:
        persona = contact_by_id['properties']['hs_persona']['value']
    except KeyError:
        persona = None
    try:
        persona = contact_by_id['properties']['hs_persona']['versions']
    except KeyError:
        persona = None
    try:
        phone = contact_by_id['properties']['phone']['value']
    except KeyError:
        phone = None
    try:
        phoneHistory = contact_by_id['properties']['phone']['versions']
    except KeyError:
        phoneHistory = None
    try:
        postalCode = contact_by_id['properties']['zip']['value']
    except KeyError:
        postalCode = None
    try:
        postalCodeHistory = contact_by_id['properties']['zip']['versions']
    except KeyError:
        postalCodeHistory = None
    try:
        recentDealAmount = contact_by_id['properties']['recent_deal_amount']['value']
    except KeyError:
        recentDealAmount = None
    try:
        recentDealAmountHistory = contact_by_id['properties']['recent_deal_amount']['versions']
    except KeyError:
        recentDealAmountHistory = None
    try:
        recentDealCloseDate = contact_by_id['properties']['recent_deal_close_date']['value']
    except KeyError:
        recentDealCloseDate = None
    try:
        recentDealCloseDateHistory = contact_by_id['properties']['recent_deal_close_date']['versions']
    except KeyError:
        recentDealCloseDateHistory = None
    try:
        emailLastOpened = contact_by_id['properties']['hs_sales_email_last_opened']['value']
    except KeyError:
        emailLastOpened = None
    try:
        emailLastOpenedHistory = contact_by_id['properties']['hs_sales_email_last_opened']['versions']
    except KeyError:
        emailLastOpenedHistory = None
    try:
        emailLastReply = contact_by_id['properties']['hs_sales_email_last_replied']['value']
    except KeyError:
        emailLastReply = None
    try:
        emailLastReplyHistory = contact_by_id['properties']['hs_sales_email_last_replied']['versions']
    except KeyError:
        emailLastReplyHistory = None
    try:
        emailLastClick = contact_by_id['properties']['hs_sales_email_last_clicked']['value']
    except KeyError:
        emailLastClick = None
    try:
        emailLastClickHistory = contact_by_id['properties']['hs_sales_email_last_clicked']['versions']
    except KeyError:
        emailLastClickHistory = None
    try:
        salutation = contact_by_id['properties']['salutation']['value']
    except KeyError:
        salutation = None
    try:
        salutationHistory = contact_by_id['properties']['salutation']['versions']
    except KeyError:
        salutationHistory = None
    try:
        state = contact_by_id['properties']['state']['value']
    except KeyError:
        state = None
    try:
        stateHistory = contact_by_id['properties']['state']['versions']
    except KeyError:
        stateHistory = None
    try:
        address = contact_by_id['properties']['address']['value']
    except KeyError:
        address = None
    try:
        addressHistory = contact_by_id['properties']['address']['versions']
    except KeyError:
        addressHistory = None
    try:
        totalRevenue = contact_by_id['properties']['total_revenue']['value']
    except KeyError:
        totalRevenue = None
    try:
        totalRevenueHistory = contact_by_id['properties']['total_revenue']['versions']
    except KeyError:
        totalRevenueHistory = None
    try:
        broadcastLinks = contact_by_id['properties']['hs_social_num_broadcast_clicks']['value']
    except KeyError:
        broadcastLinks = None
    try:
        broadcastLinksHistory = contact_by_id['properties']['hs_social_num_broadcast_clicks']['versions']
    except KeyError:
        broadcastLinksHistory = None
    try:
        facebookClicks = contact_by_id['properties']['hs_social_facebook_clicks']['value']
    except KeyError:
        facebookClicks = None
    try:
        facebookClicksHistory = contact_by_id['properties']['hs_social_facebook_clicks']['versions']
    except KeyError:
        facebookClicksHistory = None
    try:
        followerCount = contact_by_id['properties']['followercount']['value']
    except KeyError:
        followerCount = None
    try:
        followerCountHistory = contact_by_id['properties']['followercount']['versions']
    except KeyError:
        followerCountHistory = None
    try:
        googlePlusClicks = contact_by_id['properties']['hs_social_google_plus_clicks']['value']
    except KeyError:
        googlePlusClicks = None
    try:
        googlePlusClicksHistory = contact_by_id['properties']['hs_social_google_plus_clicks']['versions']
    except KeyError:
        googlePlusClicksHistory = None
    try:
        kloutScore = contact_by_id['properties']['kloutscoregeneral']['value']
    except KeyError:
        kloutScore = None
    try:
        kloutScoreHistory = contact_by_id['properties']['kloutscoregeneral']['versions']
    except KeyError:
        kloutScoreHistory = None
    try:
        linkedInBio = contact_by_id['properties']['linkedinbio']['value']
    except KeyError:
        linkedInBio = None
    try:
        linkedInBioHistory = contact_by_id['properties']['linkedinbio']['versions']
    except KeyError:
        linkedInBioHistory = None
    try:
        linkedInClicks = contact_by_id['properties']['hs_social_linkedin_clicks']['value']
    except KeyError:
        linkedInClicks = None
    try:
        linkedInClicksHistory = contact_by_id['properties']['hs_social_linkedin_clicks']['versions']
    except KeyError:
        linkedInClicksHistory = None
    try:
        linkedInConnections = contact_by_id['properties']['linkedinconnections']['value']
    except KeyError:
        linkedInConnections = None
    try:
        linkedInConnectionsHistory = contact_by_id['properties']['linkedinconnections']['versions']
    except KeyError:
        linkedInConnectionsHistory = None
    try:
        mostRecentSocialClick = contact_by_id['properties']['hs_social_last_engagement']['value']
    except KeyError:
        mostRecentSocialClick = None
    try:
        mostRecentSocialClickHistory = contact_by_id['properties']['hs_social_last_engagement']['versions']
    except KeyError:
        mostRecentSocialClickHistory = None
    try:
        twitterBio = contact_by_id['properties']['twitterbio']['value']
    except KeyError:
        twitterBio = None
    try:
        twitterBioHistory = contact_by_id['properties']['twitterbio']['versions']
    except KeyError:
        twitterBioHistory = None
    try:
        twitterClicks = contact_by_id['properties']['hs_social_twitter_clicks']['value']
    except KeyError:
        twitterClicks = None
    try:
        twitterClicksHistory = contact_by_id['properties']['hs_social_twitter_clicks']['versions']
    except KeyError:
        twitterClicksHistory = None
    try:
        twitterProfilePic = contact_by_id['properties']['twitterprofilephoto']['value']
    except KeyError:
        twitterProfilePic = None
    try:
        twitterProfilePicHistory = contact_by_id['properties']['twitterprofilephoto']['versions']
    except KeyError:
        twitterProfilePicHistory = None
    try:
        toolExpertise = contact_by_id['properties']['tool_expertise']['value']
    except KeyError:
        toolExpertise = None
    try:
        toolExpertiseHistory = contact_by_id['properties']['tool_expertise']['versions']
    except KeyError:
        toolExpertiseHistory = None
    try:
        sectorExperience = contact_by_id['properties']['sector_experience']['value']
    except KeyError:
        sectorExperience = None
    try:
        sectorExperienceHistory = contact_by_id['properties']['sector_experience']['versions']
    except KeyError:
        sectorExperienceHistory = None
    try:
        pastProfession = contact_by_id['properties']['past_profession']['value']
    except KeyError:
        pastProfession = None
    try:
        pastProfessionHistory = contact_by_id['properties']['past_profession']['versions']
    except KeyError:
        pastProfessionHistory = None
    try:
        recruiterName = contact_by_id['properties']['who_was_the_recruiter_']['value']
    except KeyError:
        recruiterName = None
    try:
        recruiterNameHistory = contact_by_id['properties']['who_was_the_recruiter_']['versions']
    except KeyError:
        recruiterNameHistory = None
    try:
        recruiterCompany = contact_by_id['properties']['recruiter_company']['value']
    except KeyError:
        recruiterCompany = None
    try:
        recruiterCompanyHistory = contact_by_id['properties']['recruiter_company']['versions']
    except KeyError:
        recruiterCompanyHistory = None
    try:
        totalSharesIssued = contact_by_id['properties']['offer_letter_total_shares_issued']['value']
    except KeyError:
        totalSharesIssued = None
    try:
        totalSharesIssuedHistory = contact_by_id['properties']['offer_letter_total_shares_issued']['versions']
    except KeyError:
        totalSharesIssuedHistory = None
    try:
        priorityGoals = contact_by_id['properties']['priority_goals_for_next_week']['value']
    except KeyError:
        priorityGoals = None
    try:
        priorityGoalsHistory = contact_by_id['properties']['priority_goals_for_next_week']['versions']
    except KeyError:
        priorityGoalsHistory = None
    try:
        postMoneyValuation = contact_by_id['properties']['offer_letter_most_recent_post_money_valuation']['value']
    except KeyError:
        postMoneyValuation = None
    try:
        postMoneyValuationHistory = contact_by_id['properties']['offer_letter_most_recent_post_money_valuation']['versions']
    except KeyError:
        postMoneyValuationHistory = None
    try:
        managersDirectReports = contact_by_id['properties']['offer_letter_managers_direct_reports']['value']
    except KeyError:
        managersDirectReports = None
    try:
        managersDirectReportsHistory = contact_by_id['properties']['offer_letter_managers_direct_reports']['versions']
    except KeyError:
        managersDirectReportsHistory = None
    try:
        annualizedSalary = contact_by_id['properties']['offer_letter_annualized_salary']['value']
    except KeyError:
        annualizedSalary = None
    try:
        annualizedSalaryHistory = contact_by_id['properties']['offer_letter_annualized_salary']['versions']
    except KeyError:
        annualizedSalaryHistory = None
    try:
        amountRaisedLastRound = contact_by_id['properties']['offer_letter_amount_raised_in_most_recent_round']['value']
    except KeyError:
        amountRaisedLastRound = None
    try:
        amountRaisedLastRoundHistory = contact_by_id['properties']['offer_letter_amount_raised_in_most_recent_round']['versions']
    except KeyError:
        amountRaisedLastRoundHistory = None
    try:
        roundType = contact_by_id['properties']['offer_letter_type_of_round']['value']
    except KeyError:
        roundType = None
    try:
        roundTypeHistory = contact_by_id['properties']['offer_letter_type_of_round']['versions']
    except KeyError:
        roundTypeHistory = None
    try:
        bonuses = contact_by_id['properties']['offer_letter_bonuses']['value']
    except KeyError:
        bonuses = None
    try:
        bonusesHistory = contact_by_id['properties']['offer_letter_bonuses']['versions']
    except KeyError:
        bonusesHistory = None
    try:
        offerLetterUpload = contact_by_id['properties']['offer_letter_upload']['value']
    except KeyError:
        offerLetterUpload = None
    try:
        offerLetterUploadHistory = contact_by_id['properties']['offer_letter_upload']['versions']
    except KeyError:
        offerLetterUploadHistory = None
    try:
        whenFullyVested = contact_by_id['properties']['offer_letter_when_fully_vested']['value']
    except KeyError:
        whenFullyVested = None
    try:
        whenFullyVestedHistory = contact_by_id['properties']['offer_letter_when_fully_vested']['versions']
    except KeyError:
        whenFullyVestedHistory = None
    try:
        vestingStartDate = contact_by_id['properties']['offer_letter_vesting_start_date']['value']
    except KeyError:
        vestingStartDate = None
    try:
        vestingStartDateHistory = contact_by_id['properties']['offer_letter_vesting_start_date']['versions']
    except KeyError:
        vestingStartDateHistory = None
    try:
        typeOfEngagement = contact_by_id['properties']['offer_letter_type_of_engagement']['value']
    except KeyError:
        typeOfEngagement = None
    try:
        typeOfEngagementHistory = contact_by_id['properties']['offer_letter_type_of_engagement']['versions']
    except KeyError:
        typeOfEngagementHistory = None
    try:
        totalAmountRaised = contact_by_id['properties']['offer_letter_total_amount_raised']['value']
    except KeyError:
        totalAmountRaised = None
    try:
        totalAmountRaisedHistory = contact_by_id['properties']['offer_letter_total_amount_raised']['versions']
    except KeyError:
        totalAmountRaisedHistory = None
    try:
        sharesOfStock = contact_by_id['properties']['offer_letter_shares_of_stock']['value']
    except KeyError:
        sharesOfStock = None
    try:
        sharesOfStockHistory = contact_by_id['properties']['offer_letter_shares_of_stock']['versions']
    except KeyError:
        sharesOfStockHistory = None
    try:
        sharesOfStock2 = contact_by_id['properties']['offer_letter_shares_of_stock_2']['value']
    except KeyError:
        sharesOfStock2 = None
    try:
        sharesOfStock2History = contact_by_id['properties']['offer_letter_shares_of_stock_2']['versions']
    except KeyError:
        sharesOfStock2History = None
    try:
        sharesOfStock3 = contact_by_id['properties']['offer_letter_shares_of_stock_3']['value']
    except KeyError:
        sharesOfStock3 = None
    try:
        sharesOfStock3History = contact_by_id['properties']['offer_letter_shares_of_stock_3']['versions']
    except KeyError:
        sharesOfStock3History = None
    try:
        proposedStartDate = contact_by_id['properties']['offer_letter_proposed_start_date']['value']
    except KeyError:
        proposedStartDate = None
    try:
        proposedStartDateHistory = contact_by_id['properties']['offer_letter_proposed_start_date']['versions']
    except KeyError:
        proposedStartDateHistory = None
    try:
        proposedSalaryOption3 = contact_by_id['properties']['offer_letter_proposed_salary_option_3']['value']
    except KeyError:
        proposedSalaryOption3 = None
    try:
        proposedSalaryOption3History = contact_by_id['properties']['offer_letter_proposed_salary_option_3']['versions']
    except KeyError:
        proposedSalaryOption3History = None
    try:
        paymentTiming = contact_by_id['properties']['offer_letter_payment_timing']['value']
    except KeyError:
        paymentTiming = None
    try:
        paymentTimingHistory = contact_by_id['properties']['offer_letter_payment_timing']['versions']
    except KeyError:
        paymentTimingHistory = None
    try:
        parentCompanyName = contact_by_id['properties']['offer_letter_parent_company_name']['value']
    except KeyError:
        parentCompanyName = None
    try:
        parentCompanyNameHistory = contact_by_id['properties']['offer_letter_parent_company_name']['versions']
    except KeyError:
        parentCompanyNameHistory = None
    try:
        paidTimeOff = contact_by_id['properties']['offer_letter_paid_time_off']['value']
    except KeyError:
        paidTimeOff = None
    try:
        paidTimeOffHistory = contact_by_id['properties']['offer_letter_paid_time_off']['versions']
    except KeyError:
        paidTimeOffHistory = None
    try:
        otherBenefits = contact_by_id['properties']['offer_letter_other_benefits']['value']
    except KeyError:
        otherBenefits = None
    try:
        otherBenefitsHistory = contact_by_id['properties']['offer_letter_other_benefits']['versions']
    except KeyError:
        otherBenefitsHistory = None
    try:
        officeAddress = contact_by_id['properties']['offer_letter_office_address']['value']
    except KeyError:
        officeAddress = None
    try:
        officeAddressHistory = contact_by_id['properties']['offer_letter_office_address']['versions']
    except KeyError:
        officeAddressHistory = None
    try:
        offerLetterExpirationDate = contact_by_id['properties']['offer_letter_offer_letter_expire_date']['value']
    except KeyError:
        offerLetterExpirationDate = None
    try:
        offerLetterExpirationDateHistory = contact_by_id['properties']['offer_letter_offer_letter_expire_date']['versions']
    except KeyError:
        offerLetterExpirationDateHistory = None
    try:
        managerTitle = contact_by_id['properties']['offer_letter_manager_s_title']['value']
    except KeyError:
        managerTitle = None
    try:
        managerTitleHistory = contact_by_id['properties']['offer_letter_manager_s_title']['versions']
    except KeyError:
        managerTitleHistory = None
    try:
        managerTimeInRole = contact_by_id['properties']['offer_letter_manager_time_in_role']['value']
    except KeyError:
        managerTimeInRole = None
    try:
        managerTimeInRoleHistory = contact_by_id['properties']['offer_letter_manager_time_in_role']['versions']
    except KeyError:
        managerTimeInRoleHistory = None
    try:
        lastFundingRoundDate = contact_by_id['properties']['offer_letter_date_of_last_funding_round']['value']
    except KeyError:
        lastFundingRoundDate = None
    try:
        lastFundingRoundDateHistory = contact_by_id['properties']['offer_letter_date_of_last_funding_round']['versions']
    except KeyError:
        lastFundingRoundDateHistory = None
    try:
        offerGivenDate = contact_by_id['properties']['offer_letter_date_given_offer']['value']
    except KeyError:
        offerGivenDate = None
    try:
        offerGivenDateHistory = contact_by_id['properties']['offer_letter_date_given_offer']['versions']
    except KeyError:
        offerGivenDateHistory = None
    try:
        bonuses3 = contact_by_id['properties']['offer_letter_bonuses_3']['value']
    except KeyError:
        bonuses3 = None
    try:
        bonuses3History = contact_by_id['properties']['offer_letter_bonuses_3']['versions']
    except KeyError:
        bonuses3History = None
    try:
        bonuses2 = contact_by_id['properties']['offer_letter_bonuses_2']['value']
    except KeyError:
        bonuses2 = None
    try:
        bonuses2History = contact_by_id['properties']['offer_letter_bonuses_2']['versions']
    except KeyError:
        bonuses2History = None
    try:
        benefits = contact_by_id['properties']['offer_letter_benefits']['value']
    except KeyError:
        benefits = None
    try:
        benefitsHistory = contact_by_id['properties']['offer_letter_benefits']['versions']
    except KeyError:
        benefitsHistory = None
    try:
        proposedSalaryOption2 = contact_by_id['properties']['offer_letter_proposed_salary_option_2']['value']
    except KeyError:
        proposedSalaryOption2 = None
    try:
        proposedSalaryOption2History = contact_by_id['properties']['offer_letter_proposed_salary_option_2']['versions']
    except KeyError:
        proposedSalaryOption2History = None
    try:
        paymentSchedule2 = contact_by_id['properties']['offer_letter_payment_schedule_2']['value']
    except KeyError:
        paymentSchedule2 = None
    try:
        paymentSchedule2History = contact_by_id['properties']['offer_letter_payment_schedule_2']['versions']
    except KeyError:
        paymentSchedule2History = None
    try:
        offerLetterCompanyName = contact_by_id['properties']['offer_letter_company_name']['value']
    except KeyError:
        offerLetterCompanyName = None
    try:
        offerLetterCompanyNameHistory = contact_by_id['properties']['offer_letter_company_name']['versions']
    except KeyError:
        offerLetterCompanyNameHistory = None
    try:
        numCompaniesReachedOut = contact_by_id['properties']['num_companies_you_reached_out']['value']
    except KeyError:
        numCompaniesReachedOut = None
    try:
        numCompaniesReachedOutHistory = contact_by_id['properties']['num_companies_you_reached_out']['versions']
    except KeyError:
        numCompaniesReachedOutHistory = None
    try:
        namesCompaniesReachedOut = contact_by_id['properties']['new_companies_reached_out']['value']
    except KeyError:
        namesCompaniesReachedOut = None
    try:
        namesCompaniesReachedOutHistory = contact_by_id['properties']['new_companies_reached_out']['versions']
    except KeyError:
        namesCompaniesReachedOutHistory = None
    try:
        jobSearchStage = contact_by_id['properties']['job_search_stage']['value']
    except KeyError:
        jobSearchStage = None
    try:
        jobSearchStageHistory = contact_by_id['properties']['job_search_stage']['versions']
    except KeyError:
        jobSearchStageHistory = None
    try:
        feelLastWeek = contact_by_id['properties']['feel_about_the_last_week']['value']
    except KeyError:
        feelLastWeek = None
    try:
        feelLastWeekHistory = contact_by_id['properties']['feel_about_the_last_week']['versions']
    except KeyError:
        feelLastWeekHistory = None
    try:
        supportThisWeek = contact_by_id['properties']['support_for_this_week']['value']
    except KeyError:
        supportThisWeek = None
    try:
        supportThisWeekHistory = contact_by_id['properties']['support_for_this_week']['versions']
    except KeyError:
        supportThisWeekHistory = None
    try:
        greatResume = contact_by_id['properties']['great_resume']['value']
    except KeyError:
        greatResume = None
    try:
        greatResumeHistory = contact_by_id['properties']['great_resume']['versions']
    except KeyError:
        greatResumeHistory = None
    try:
        greatPortfolioDeck = contact_by_id['properties']['great_portfolio_deck']['value']
    except KeyError:
        greatPortfolioDeck = None
    try:
        greatPortfolioDeckHistory = contact_by_id['properties']['great_portfolio_deck']['versions']
    except KeyError:
        greatPortfolioDeckHistory = None
    try:
        greatLinkedInDescription = contact_by_id['properties']['great_linkedin_description']['value']
    except KeyError:
        greatLinkedInDescription = None
    try:
        greatLinkedInDescriptionHistory = contact_by_id['properties']['great_linkedin_description']['value']
    except KeyError:
        greatLinkedInDescriptionHistory = None
    try:
        workWithRecruiter = contact_by_id['properties']['did_you_work_with_a_recruiter_to_get_placed_']['value']
    except KeyError:
        workWithRecruiter = None
    try:
        workWithRecruiterHistory = contact_by_id['properties']['did_you_work_with_a_recruiter_to_get_placed_']['versions']
    except KeyError:
        workWithRecruiterHistory = None
    try:
        currentlyInterviewing = contact_by_id['properties']['currently_interviewing_with_companies']['value']
    except KeyError:
        currentlyInterviewing = None
    try:
        currentlyInterviewingHistory = contact_by_id['properties']['currently_interviewing_with_companies']['versions']
    except KeyError:
        currentlyInterviewingHistory = None
    try:
        extraInfo = contact_by_id['properties']['extra_info_to_add']['value']
    except KeyError:
        extraInfo = None
    try:
        extraInfoHistory = contact_by_id['properties']['extra_info_to_add']['versions']
    except KeyError:
        extraInfoHistory = None
    try:
        growUpLocation = contact_by_id['properties']['where_did_you_grow_up_']['value']
    except KeyError:
        growUpLocation = None
    try:
        growUpLocationHistory = contact_by_id['properties']['where_did_you_grow_up_']['versions']
    except KeyError:
        growUpLocationHistory = None
    try:
        weight = contact_by_id['properties']['weight']['value']
    except KeyError:
        weight = None
    try:
        weightHistory = contact_by_id['properties']['weight']['versions']
    except KeyError:
        weightHistory = None
    try:
        significantOtherLinkedIn = contact_by_id['properties']['significant_other_linkedin']['value']
    except KeyError:
        significantOtherLinkedIn = None
    try:
        significantOtherLinkedInHistory = contact_by_id['properties']['significant_other_linkedin']['versions']
    except KeyError:
        significantOtherLinkedInHistory = None
    try:
        siblings = contact_by_id['properties']['siblings']['value']
    except KeyError:
        siblings = None
    try:
        siblingsHistory = contact_by_id['properties']['siblings']['versions']
    except KeyError:
        siblingsHistory = None
    try:
        sectorsOfInterest = contact_by_id['properties']['sectors_of_interest']['value']
    except KeyError:
        sectorsOfInterest = None
    try:
        sectorsOfInterestHistory = contact_by_id['properties']['sectors_of_interest']['versions']
    except KeyError:
        sectorsOfInterestHistory = None
    try:
        religiousAffiliations = contact_by_id['properties']['religious_affiliations']['value']
    except KeyError:
        religiousAffiliations = None
    try:
        religiousAffiliationsHistory = contact_by_id['properties']['religious_affiliations']['versions']
    except KeyError:
        religiousAffiliationsHistory = None
    try:
        preferredName = contact_by_id['properties']['preferred_name']['value']
    except KeyError:
        preferredName = None
    try:
        preferredNameHistory = contact_by_id['properties']['preferred_name']['versions']
    except KeyError:
        preferredNameHistory = None
    try:
        siblingNotes = contact_by_id['properties']['notes_on_sibling_s_']['value']
    except KeyError:
        siblingNotes = None
    try:
        siblingNotesHistory = contact_by_id['properties']['notes_on_sibling_s_']['versions']
    except KeyError:
        siblingNotesHistory = None
    try:
        childrenNotes = contact_by_id['properties']['notes_on_children']['value']
    except KeyError:
        childrenNotes = None
    try:
        childrenNotesHistory = contact_by_id['properties']['notes_on_children']['versions']
    except KeyError:
        childrenNotesHistory = None
    try:
        significantOtherName = contact_by_id['properties']['name_of_significant_other']['value']
    except KeyError:
        significantOtherName = None
    try:
        significantOtherNameHistory = contact_by_id['properties']['name_of_significant_other']['versions']
    except KeyError:
        significantOtherNameHistory = None
    try:
        maritalStatus = contact_by_id['properties']['marital_status']['value']
    except KeyError:
        maritalStatus = None
    try:
        maritalStatusHistory = contact_by_id['properties']['marital_status']['versions']
    except KeyError:
        maritalStatusHistory = None
    try:
        laptopType = contact_by_id['properties']['laptop_type']['value']
    except KeyError:
        laptopType = None
    try:
        laptopTypeHistory = contact_by_id['properties']['laptop_type']['versions']
    except KeyError:
        laptopTypeHistory = None
    try:
        immigrationStatus = contact_by_id['properties']['immigration_status']['value']
    except KeyError:
        immigrationStatus = None
    try:
        immigrationStatusHistory = contact_by_id['properties']['immigration_status']['versions']
    except KeyError:
        immigrationStatusHistory = None
    try:
        hobbies = contact_by_id['properties']['hobbies']['value']
    except KeyError:
        hobbies = None
    try:
        hobbiesHistory = contact_by_id['properties']['hobbies']['versions']
    except KeyError:
        hobbiesHistory = None
    try:
        height = contact_by_id['properties']['height']['value']
    except KeyError:
        height = None
    try:
        heightHistory = contact_by_id['properties']['height']['versions']
    except KeyError:
        heightHistory = None
    try:
        gradSchoolProgramType = contact_by_id['properties']['grad_school_program_type']['value']
    except KeyError:
        gradSchoolProgramType = None
    try:
        gradSchoolProgramTypeHistory = contact_by_id['properties']['grad_school_program_type']['versions']
    except KeyError:
        gradSchoolProgramTypeHistory = None
    try:
        gradSchoolProgram = contact_by_id['properties']['grad_school_program']['value']
    except KeyError:
        gradSchoolProgram = None
    try:
        gradSchoolProgramHistory = contact_by_id['properties']['grad_school_program']['versions']
    except KeyError:
        gradSchoolProgramHistory = None
    try:
        glasses = contact_by_id['properties']['glasses']['value']
    except KeyError:
        glasses = None
    try:
        glassesHistory = contact_by_id['properties']['glasses']['versions']
    except KeyError:
        glassesHistory = None
    try:
        gender = contact_by_id['properties']['gender']['value']
    except KeyError:
        gender = None
    try:
        genderHistory = contact_by_id['properties']['gender']['versions']
    except KeyError:
        genderHistory = None
    try:
        gearSize = contact_by_id['properties']['gear_size']['value']
    except KeyError:
        gearSize = None
    try:
        gearSizeHistory = contact_by_id['properties']['gear_size']['versions']
    except KeyError:
        gearSizeHistory = None
    try:
        familyLocation = contact_by_id['properties']['family_location']['value']
    except KeyError:
        familyLocation = None
    try:
        familyLocationHistory = contact_by_id['properties']['family_location']['versions']
    except KeyError:
        familyLocationHistory = None
    try:
        familyInBayArea = contact_by_id['properties']['family_in_bay_area']['value']
    except KeyError:
        familyInBayArea = None
    try:
        familyInBayAreaHistory = contact_by_id['properties']['family_in_bay_area']['versions']
    except KeyError:
        familyInBayAreaHistory = None
    try:
        ethnicity = contact_by_id['properties']['ethnicity']['value']
    except KeyError:
        ethnicity = None
    try:
        ethnicityHistory = contact_by_id['properties']['ethnicity']['versions']
    except KeyError:
        ethnicityHistory = None
    try:
        collegeOrUniversity = contact_by_id['properties']['college_university']['value']
    except KeyError:
        collegeOrUniversity = None
    try:
        collegeOrUniversityHistory = contact_by_id['properties']['college_university']['versions']
    except KeyError:
        collegeOrUniversityHistory = None
    try:
        citizenship = contact_by_id['properties']['citizenship']['value']
    except KeyError:
        citizenship = None
    try:
        citizenshipHistory = contact_by_id['properties']['citizenship']['versions']
    except KeyError:
        citizenshipHistory = None
    try:
        children = contact_by_id['properties']['children']['value']
    except KeyError:
        children = None
    try:
        childrenHistory = contact_by_id['properties']['children']['versions']
    except KeyError:
        childrenHistory = None
    try:
        birthplace = contact_by_id['properties']['birthplace']['value']
    except KeyError:
        birthplace = None
    try:
        birthplaceHistory = contact_by_id['properties']['birthplace']['versions']
    except KeyError:
        birthplaceHistory = None
    try:
        birthday = contact_by_id['properties']['birthday']['value']
    except KeyError:
        birthday = None
    try:
        birthdayHistory = contact_by_id['properties']['birthday']['versions']
    except KeyError:
        birthdayHistory = None
    try:
        languagesSpoken = contact_by_id['properties']['additional_languages_spoken']['value']
    except KeyError:
        languagesSpoken = None
    try:
        languagesSpokenHistory = contact_by_id['properties']['additional_languages_spoken']['versions']
    except KeyError:
        languagesSpokenHistory = None
    try:
        currentlyInWorkflow = contact_by_id['properties']['currentlyinworkflow']['value']
    except KeyError:
        currentlyInWorkflow = None
    try:
        currentlyInWorkflowHistory = contact_by_id['properties']['currentlyinworkflow']['versions']
    except KeyError:
        currentlyInWorkflowHistory = None
    try:
        emailAddressQuarantined = contact_by_id['properties']['hs_email_quarantined']['value']
    except KeyError:
        emailAddressQuarantined = None
    try:
        emailAddressQuarantinedHistory = contact_by_id['properties']['hs_email_quarantined']['versions']
    except KeyError:
        emailAddressQuarantinedHistory = None
    try:
        firstMarketingEmailClickDate = contact_by_id['properties']['hs_email_first_click_date']['value']
    except KeyError:
        firstMarketingEmailClickDate = None
    try:
        firstMarketingEmailClickDateHistory = contact_by_id['properties']['hs_email_first_click_date']['versions']
    except KeyError:
        firstMarketingEmailClickDateHistory = None
    try:
        firstMarketingEmailOpenDate = contact_by_id['properties']['hs_email_first_open_date']['value']
    except KeyError:
        firstMarketingEmailOpenDate = None
    try:
        firstMarketingEmailOpenDateHistory = contact_by_id['properties']['hs_email_first_open_date']['versions']
    except KeyError:
        firstMarketingEmailOpenDateHistory = None
    try:
        firstMarketingEmailSendDate = contact_by_id['properties']['hs_email_first_send_date']['value']
    except KeyError:
        firstMarketingEmailSendDate = None
    try:
        firstMarketingEmailSendDateHistory = contact_by_id['properties']['hs_email_first_send_date']['versions']
    except KeyError:
        firstMarketingEmailSendDateHistory = None
    try:
        lastMarketingEmailClickDate = contact_by_id['properties']['hs_email_last_click_date']['value']
    except KeyError:
        lastMarketingEmailClickDate = None
    try:
        lastMarketingEmailClickDateHistory = contact_by_id['properties']['hs_email_last_click_date']['versions']
    except KeyError:
        lastMarketingEmailClickDateHistory = None
    try:
        lastMarketingEmailName = contact_by_id['properties']['hs_email_last_email_name']['value']
    except KeyError:
        lastMarketingEmailName = None
    try:
        lastMarketingEmailNameHistory = contact_by_id['properties']['hs_email_last_email_name']['versions']
    except KeyError:
        lastMarketingEmailNameHistory = None
    try:
        lastMarketingEmailOpenDate = contact_by_id['properties']['hs_email_last_open_date']['value']
    except KeyError:
        lastMarketingEmailOpenDate = None
    try:
        lastMarketingEmailOpenDateHistory = contact_by_id['properties']['hs_email_last_open_date']['versions']
    except KeyError:
        lastMarketingEmailOpenDateHistory = None
    try:
        lastMarketingEmailSendDate = contact_by_id['properties']['hs_email_last_send_date']['value']
    except KeyError:
        lastMarketingEmailSendDate = None
    try:
        lastMarketingEmailSendDateHistory = contact_by_id['properties']['hs_email_last_send_date']['versions']
    except KeyError:
        lastMarketingEmailSendDateHistory = None
    try:
        marketingEmailConfirmationStatus = contact_by_id['properties']['hs_emailconfirmationstatus']['value']
    except KeyError:
        marketingEmailConfirmationStatus = None
    try:
        marketingEmailConfirmationStatusHistory = contact_by_id['properties']['hs_emailconfirmationstatus']['versions']
    except KeyError:
        marketingEmailConfirmationStatusHistory = None
    try:
        marketingEmailsBounced = contact_by_id['properties']['hs_email_bounce']['value']
    except KeyError:
        marketingEmailsBounced = None
    try:
        marketingEmailsBouncedHistory = contact_by_id['properties']['hs_email_bounce']['versions']
    except KeyError:
        marketingEmailsBouncedHistory = None
    try:
        marketingEmailsClicked = contact_by_id['properties']['hs_email_click']['value']
    except KeyError:
        marketingEmailsClicked = None
    try:
        marketingEmailsClickedHistory = contact_by_id['properties']['hs_email_click']['versions']
    except KeyError:
        marketingEmailsClickedHistory = None
    try:
        marketingEmailsDelivered = contact_by_id['properties']['hs_email_delivered']['value']
    except KeyError:
        marketingEmailsDelivered = None
    try:
        marketingEmailsDeliveredHistory = contact_by_id['properties']['hs_email_delivered']['versions']
    except KeyError:
        marketingEmailsDeliveredHistory = None
    try:
        marketingEmailsOpened = contact_by_id['properties']['hs_email_open']['value']
    except KeyError:
        marketingEmailsOpened = None
    try:
        marketingEmailsOpenedHistory = contact_by_id['properties']['hs_email_open']['versions']
    except KeyError:
        marketingEmailsOpenedHistory = None
    try:
        optedOutEmailMarketingInfo = contact_by_id['properties']['hs_email_optout_4686743']['value']
    except KeyError:
        optedOutEmailMarketingInfo = None
    try:
        optedOutEmailMarketingInfoHistory = contact_by_id['properties']['hs_email_optout_4686743']['versions']
    except KeyError:
        optedOutEmailMarketingInfoHistory = None
    try:
        optedOutBlogSubscription = contact_by_id['properties']['hs_email_optout_4686744']['value']
    except KeyError:
        optedOutBlogSubscription = None
    try:
        optedOutBlogSubscriptionHistory = contact_by_id['properties']['hs_email_optout_4686744']['versions']
    except KeyError:
        optedOutBlogSubscriptionHistory = None
    try:
        optedOutOneToOne = contact_by_id['properties']['hs_email_optout_2898892']['value']
    except KeyError:
        optedOutOneToOne = None
    try:
        optedOutOneToOneHistory = contact_by_id['properties']['hs_email_optout_2898892']['versions']
    except KeyError:
        optedOutOneToOneHistory = None
    try:
        optedOutTCSub = contact_by_id['properties']['hs_email_optout_4722455']['value']
    except KeyError:
        optedOutTCSub = None
    try:
        optedOutTCSubHistory = contact_by_id['properties']['hs_email_optout_4722455']['versions']
    except KeyError:
        optedOutTCSubHistory = None
    try:
        emailsSentSinceLastEngagement = contact_by_id['properties']['hs_email_sends_since_last_engagement']['value']
    except KeyError:
        emailsSentSinceLastEngagement = None
    try:
        emailsSentSinceLastEngagementHistory = contact_by_id['properties']['hs_email_sends_since_last_engagement']['versions']
    except KeyError:
        emailsSentSinceLastEngagementHistory = None
    try:
        optedOutAllEmail = contact_by_id['properties']['hs_email_optout']['value']
    except KeyError:
        optedOutAllEmail = None
    try:
        optedOutAllEmailHistory = contact_by_id['properties']['hs_email_optout']['versions']
    except KeyError:
        optedOutAllEmailHistory = None
    try:
        averagePageViews = contact_by_id['properties']['hs_analytics_average_page_views']['value']
    except KeyError:
        averagePageViews = None
    try:
        averagePageViewsHistory = contact_by_id['properties']['hs_analytics_average_page_views']['versions']
    except KeyError:
        averagePageViewsHistory = None
    try:
        eventRevenue = contact_by_id['properties']['hs_analytics_revenue']['value']
    except KeyError:
        eventRevenue = None
    try:
        eventRevenueHistory = contact_by_id['properties']['hs_analytics_revenue']['versions']
    except KeyError:
        eventRevenueHistory = None
    try:
        firstPageSeen = contact_by_id['properties']['hs_analytics_first_url']['value']
    except KeyError:
        firstPageSeen = None
    try:
        firstPageSeenHistory = contact_by_id['properties']['hs_analytics_first_url']['versions']
    except KeyError:
        firstPageSeenHistory = None
    try:
        firstReferringSite = contact_by_id['properties']['hs_analytics_first_referrer']['value']
    except KeyError:
        firstReferringSite = None
    try:
        firstReferringSiteHistory = contact_by_id['properties']['hs_analytics_first_referrer']['versions']
    except KeyError:
        firstReferringSiteHistory = None
    try:
        firstTouchConvertingCampaign = contact_by_id['properties']['hs_analytics_first_touch_converting_campaign']['value']
    except KeyError:
        firstTouchConvertingCampaign = None
    try:
        firstTouchConvertingCampaignHistory = contact_by_id['properties']['hs_analytics_first_touch_converting_campaign']['versions']
    except KeyError:
        firstTouchConvertingCampaignHistory = None
    try:
        lastReferringSite = contact_by_id['properties']['hs_analytics_last_referrer']['value']
    except KeyError:
        lastReferringSite = None
    try:
        lastReferringSiteHistory = contact_by_id['properties']['hs_analytics_last_referrer']['versions']
    except KeyError:
        lastReferringSiteHistory = None
    try:
        lastTouchConvertingCampaign = contact_by_id['properties']['hs_analytics_last_touch_converting_campaign']['value']
    except KeyError:
        lastTouchConvertingCampaign = None
    try:
        lastTouchConvertingCampaignHistory = contact_by_id['properties']['hs_analytics_last_touch_converting_campaign']['versions']
    except KeyError:
        lastTouchConvertingCampaignHistory = None
    try:
        numEventCompletions = contact_by_id['properties']['hs_analytics_num_event_completions']['value']
    except KeyError:
        numEventCompletions = None
    try:
        numEventCompletionsHistory = contact_by_id['properties']['hs_analytics_num_event_completions']['versions']
    except KeyError:
        numEventCompletionsHistory = None
    try:
        numPageViews = contact_by_id['properties']['hs_analytics_num_page_views']['value']
    except KeyError:
        numPageViews = None
    try:
        numPageViewsHistory = contact_by_id['properties']['hs_analytics_num_page_views']['versions']
    except KeyError:
        numPageViewsHistory = None
    try:
        numVisits = contact_by_id['properties']['hs_analytics_num_visits']['value']
    except KeyError:
        numVisits = None
    try:
        numVisitsHistory = contact_by_id['properties']['hs_analytics_num_visits']['versions']
    except KeyError:
        numVisitsHistory = None
    try:
        originalSource = contact_by_id['properties']['hs_analytics_source']['value']
    except KeyError:
        originalSource = None
    try:
        originalSourceHistory = contact_by_id['properties']['hs_analytics_source']['versions']
    except KeyError:
        originalSourceHistory = None
    try:
        originalSourceD1 = contact_by_id['properties']['hs_analytics_source_data_1']['value']
    except KeyError:
        originalSourceD1 = None
    try:
        originalSourceD1History = contact_by_id['properties']['hs_analytics_source_data_1']['versions']
    except KeyError:
        originalSourceD1History = None
    try:
        originalSourceD2 = contact_by_id['properties']['hs_analytics_source_data_2']['value']
    except KeyError:
        originalSourceD2 = None
    try:
        originalSourceD2History = contact_by_id['properties']['hs_analytics_source_data_2']['versions']
    except KeyError:
        originalSourceD2History = None
    try:
        timeFirstSeen = contact_by_id['properties']['hs_analytics_first_timestamp']['value']
    except KeyError:
        timeFirstSeen = None
    try:
        timeFirstSeenHistory = contact_by_id['properties']['hs_analytics_first_timestamp']['versions']
    except KeyError:
        timeFirstSeenHistory = None
    try:
        timeLastSeen = contact_by_id['properties']['hs_analytics_last_timestamp']['value']
    except KeyError:
        timeLastSeen = None
    try:
        timeLastSeenHistory = contact_by_id['properties']['hs_analytics_last_timestamp']['versions']
    except KeyError:
        timeLastSeenHistory = None
    try:
        timeFirstVisit = contact_by_id['properties']['hs_analytics_first_visit_timestamp']['value']
    except KeyError:
        timeFirstVisit = None
    try:
        timeFirstVisitHistory = contact_by_id['properties']['hs_analytics_first_visit_timestamp']['versions']
    except KeyError:
        timeFirstVisitHistory = None
    try:
        timeLastVisit = contact_by_id['properties']['hs_analytics_last_visit_timestamp']['value']
    except KeyError:
        timeLastVisit = None
    try:
        timeLastVisitHistory = contact_by_id['properties']['hs_analytics_last_visit_timestamp']['versions']
    except KeyError:
        timeLastVisitHistory = None
    try:
        firstConversion = contact_by_id['properties']['first_conversion_event_name']['value']
    except KeyError:
        firstConversion = None
    try:
        firstConversionHistory = contact_by_id['properties']['first_conversion_event_name']['versions']
    except KeyError:
        firstConversionHistory = None
    try:
        firstConversionDate = contact_by_id['properties']['first_conversion_date']['value']
    except KeyError:
        firstConversionDate = None
    try:
        firstConversionDateHistory = contact_by_id['properties']['first_conversion_date']['versions']
    except KeyError:
        firstConversionDateHistory = None
    try:
        IPCity = contact_by_id['properties']['ip_city']['value']
    except KeyError:
        IPCity = None
    try:
        IPCityHistory = contact_by_id['properties']['ip_city']['versions']
    except KeyError:
        IPCityHistory = None
    try:
        IPCountry = contact_by_id['properties']['ip_country']['value']
    except KeyError:
        IPCountry = None
    try:
        IPCountryHistory = contact_by_id['properties']['ip_country']['versions']
    except KeyError:
        IPCountryHistory = None
    try:
        IPCountryCode = contact_by_id['properties']['ip_country_code']['value']
    except KeyError:
        IPCountryCode = None
    try:
        IPCountryCodeHistory = contact_by_id['properties']['ip_country_code']['versions']
    except KeyError:
        IPCountryCodeHistory = None
    try:
        IPState = contact_by_id['properties']['ip_state']['value']
    except KeyError:
        IPState = None
    try:
        IPStateHistory = contact_by_id['properties']['ip_state']['versions']
    except KeyError:
        IPStateHistory = None
    try:
        IPStateCode = contact_by_id['properties']['ip_state_code']['value']
    except KeyError:
        IPStateCode = None
    try:
        IPStateCodeHistory = contact_by_id['properties']['ip_state_code']['versions']
    except KeyError:
        IPStateCodeHistory = None
    try:
        IPTimeZone = contact_by_id['properties']['hs_ip_timezone']['value']
    except KeyError:
        IPTimeZone = None
    try:
        IPTimeZoneHistory = contact_by_id['properties']['hs_ip_timezone']['versions']
    except KeyError:
        IPTimeZoneHistory = None
    try:
        recentConversion = contact_by_id['properties']['recent_conversion_event_name']['value']
    except KeyError:
        recentConversion = None
    try:
        recentConversionHistory = contact_by_id['properties']['recent_conversion_event_name']['versions']
    except KeyError:
        recentConversionHistory = None
    try:
        recentConversionDate = contact_by_id['properties']['recent_conversion_date']['value']
    except KeyError:
        recentConversionDate = None
    try:
        recentConversionDateHistory = contact_by_id['properties']['recent_conversion_date']['versions']
    except KeyError:
        recentConversionDateHistory = None
    try:
        carDevWeeklyUpdateAssets = contact_by_id['properties']['cardev_weekly_update_assets']['value']
    except KeyError:
        carDevWeeklyUpdateAssets = None,
    try:
        carDevWeeklyUpdateAssetsHistory = contact_by_id['properties']['cardev_weekly_update_assets']['versions']
    except KeyError:
        carDevWeeklyUpdateAssetsHistory = None
    try:
        connectionsToTC = contact_by_id['properties']['connections_to_tradecraft']['value']
    except KeyError:
        connectionsToTC = None
    try:
        connectionsToTCHistory = contact_by_id['properties']['connections_to_tradecraft']['versions']
    except KeyError:
        connectionsToTCHistory = None
    try:
        contactWithTCCommunity = contact_by_id['properties']['contact_with_tc_community']['value']
    except KeyError:
        contactWithTCCommunity = None
    try:
        contactWithTCCommunityHistory = contact_by_id['properties']['contact_with_tc_community']['versions']
    except KeyError:
        contactWithTCCommunityHistory = None
    try:
        inProjects = contact_by_id['properties']['in_projects']['value']
    except KeyError:
        inProjects = None
    try:
        inProjectsHistory = contact_by_id['properties']['in_projects']['versions']
    except KeyError:
        inProjectsHistory = None
    try:
        newsletterRoleApproval = contact_by_id['properties']['newsletter_alumni_permission']['value']
    except KeyError:
        newsletterRoleApproval = None
    try:
        newsletterRoleApprovalHistory = contact_by_id['properties']['newsletter_alumni_permission']['versions']
    except KeyError:
        newsletterRoleApprovalHistory = None
    try:
        valueForMentor = contact_by_id['properties']['value_for_mentor']['value']
    except KeyError:
        valueForMentor = None
    try:
        valueForMentorHistory = contact_by_id['properties']['value_for_mentor']['versions']
    except KeyError:
        valueForMentorHistory = None
    try:
        mentorNoExaplanation = contact_by_id['properties']['explanation_for_bringing_mentor']['value']
    except KeyError:
        mentorNoExaplanation = None
    try:
        mentorNoExaplanationHistory = contact_by_id['properties']['explanation_for_bringing_mentor']['versions']
    except KeyError:
        mentorNoExaplanationHistory = None
    try:
        pathToReachMentor = contact_by_id['properties']['path_to_reach_mentor_role']['value']
    except KeyError:
        pathToReachMentor = None
    try:
        pathToReachMentorHistory = contact_by_id['properties']['path_to_reach_mentor_role']['versions']
    except KeyError:
        pathToReachMentorHistory = None
    try:
        immersiveParticipant = contact_by_id['properties']['immersive_participant']['value']
    except KeyError:
        immersiveParticipant = None
    try:
        immersiveParticipantHistory = contact_by_id['properties']['immersive_participant']['versions']
    except KeyError:
        immersiveParticipantHistory = None
    try:
        keyIssueDate = contact_by_id['properties']['key_issue_date']['value']
    except KeyError:
        keyIssueDate = None
    try:
        keyIssueDateHistory = contact_by_id['properties']['key_issue_date']['versions']
    except KeyError:
        keyIssueDateHistory = None
    try:
        keyReturnDate = contact_by_id['properties']['key_return_date']['value']
    except KeyError:
        keyReturnDate = None
    try:
        keyReturnDateHistory = contact_by_id['properties']['key_return_date']['versions']
    except KeyError:
        keyReturnDateHistory = None
    try:
        lastTCEmailUseDate = contact_by_id['properties']['last_tc_email_use_date']['value']
    except KeyError:
        lastTCEmailUseDate = None
    try:
        lastTCEmailUseDateHistory = contact_by_id['properties']['last_tc_email_use_date']['versions']
    except KeyError:
        lastTCEmailUseDateHistory = None
    try:
        linkGoalTracker = contact_by_id['properties']['link_to_goal_tracker']['value']
    except KeyError:
        linkGoalTracker = None
    try:
        linkGoalTrackerHistory = contact_by_id['properties']['link_to_goal_tracker']['versions']
    except KeyError:
        linkGoalTrackerHistory = None
    try:
        linkJobTracker = contact_by_id['properties']['link_to_job_tracker']['value']
    except KeyError:
        linkJobTracker = None
    try:
        linkJobTrackerHistory = contact_by_id['properties']['link_to_job_tracker']['versions']
    except KeyError:
        linkJobTrackerHistory = None
    try:
        madeTCReferral = contact_by_id['properties']['made_tc_referral']['value']
    except KeyError:
        madeTCReferral = None
    try:
        madeTCReferralHistory = contact_by_id['properties']['made_tc_referral']['versions']
    except KeyError:
        madeTCReferralHistory = None
    try:
        lastMentorBroughtName = contact_by_id['properties']['last_mentor_brought_name']['value']
    except KeyError:
        lastMentorBroughtName = None
    try:
        lastMentorBroughtNameHistory = contact_by_id['properties']['last_mentor_brought_name']['versions']
    except KeyError:
        lastMentorBroughtNameHistory = None
    try:
        lastMentorBroughtLinkedIn = contact_by_id['properties']['last_mentor_brought_linkedin']['value']
    except KeyError:
        lastMentorBroughtLinkedIn = None
    try:
        lastMentorBroughtLinkedInHistory = contact_by_id['properties']['last_mentor_brought_linkedin']['versions']
    except KeyError:
        lastMentorBroughtLinkedInHistory = None
    try:
        mentoredAtTC = contact_by_id['properties']['mentored_at_tc']['value']
    except KeyError:
        mentoredAtTC = None
    try:
        mentoredAtTCHistory = contact_by_id['properties']['mentored_at_tc']['versions']
    except KeyError:
        mentoredAtTCHistory = None
    try:
        mentorsBroughtIn = contact_by_id['properties']['mentors_brought_in']['value']
    except KeyError:
        mentorsBroughtIn = None
    try:
        mentorsBroughtInHistory = contact_by_id['properties']['mentors_brought_in']['versions']
    except KeyError:
        mentorsBroughtInHistory = None
    try:
        promoHelp = contact_by_id['properties']['wom_help']['value']
    except KeyError:
        promoHelp = None
    try:
        promoHelpHistory = contact_by_id['properties']['wom_help']['versions']
    except KeyError:
        promoHelpHistory = None
    try:
        promoNotes = contact_by_id['properties']['wom_notes']['value']
    except KeyError:
        promoNotes = None
    try:
        promoNotesHistory = contact_by_id['properties']['wom_notes']['versions']
    except KeyError:
        promoNotesHistory = None
    try:
        secondEmail = contact_by_id['properties']['second_email']['value']
    except KeyError:
        secondEmail = None
    try:
        secondEmailHistory = contact_by_id['properties']['second_email']['versions']
    except KeyError:
        secondEmailHistory = None
    try:
        sheetsTransferNotes = contact_by_id['properties']['sheets_transfer_notes']['value']
    except KeyError:
        sheetsTransferNotes = None
    try:
        sheetsTransferNotesHistory = contact_by_id['properties']['sheets_transfer_notes']['versions']
    except KeyError:
        sheetsTransferNotesHistory = None
    try:
        storyVideoLink = contact_by_id['properties']['story_video_link']['value']
    except KeyError:
        storyVideoLink = None
    try:
        storyVideoLinkHistory = contact_by_id['properties']['story_video_link']['versions']
    except KeyError:
        storyVideoLinkHistory = None
    try:
        membersReferred = contact_by_id['properties']['tc_members_referred']['value']
    except KeyError:
        membersReferred = None
    try:
        membersReferredHistory = contact_by_id['properties']['tc_members_referred']['versions']
    except KeyError:
        membersReferredHistory = None
    try:
        bankingInfo = contact_by_id['properties']['banking_information']['value']
    except KeyError:
        bankingInfo = None
    try:
        bankingInfoHistory = contact_by_id['properties']['banking_information']['versions']
    except KeyError:
        bankingInfoHistory = None
    try:
        burnRate = contact_by_id['properties']['burn_rate']['value']
    except KeyError:
        burnRate = None
    try:
        burnRateHistory = contact_by_id['properties']['burn_rate']['versions']
    except KeyError:
        burnRateHistory = None
    try:
        depositCollected = contact_by_id['properties']['deposit_collected']['value']
    except KeyError:
        depositCollected = None
    try:
        depositCollectedHistory = contact_by_id['properties']['deposit_collected']['versions']
    except KeyError:
        depositCollectedHistory = None
    try:
        depositUncollected = contact_by_id['properties']['deposit_uncollected']['value']
    except KeyError:
        depositUncollected = None
    try:
        depositUncollectedHistory = contact_by_id['properties']['deposit_uncollected']['versions']
    except KeyError:
        depositUncollectedHistory = None
    try:
        financialSituation = contact_by_id['properties']['financial_situation']['value']
    except KeyError:
        financialSituation = None
    try:
        financialSituationHistory = contact_by_id['properties']['financial_situation']['versions']
    except KeyError:
        financialSituationHistory = None
    try:
        financing = contact_by_id['properties']['financing']['value']
    except KeyError:
        financing = None
    try:
        financingHistory = contact_by_id['properties']['financing']['versions']
    except KeyError:
        financingHistory = None
    try:
        financingType = contact_by_id['properties']['financing_type']['value']
    except KeyError:
        financingType = None
    try:
        financingTypeHistory = contact_by_id['properties']['financing_type']['versions']
    except KeyError:
        financingTypeHistory = None
    try:
        holdBackAmount = contact_by_id['properties']['holdback_amount']['value']
    except KeyError:
        holdBackAmount = None
    try:
        holdBackAmountHistory = contact_by_id['properties']['holdback_amount']['versions']
    except KeyError:
        holdBackAmountHistory = None
    try:
        holdBackRepaymentDate = contact_by_id['properties']['holdback_repayment_date']['value']
    except KeyError:
        holdBackRepaymentDate = None
    try:
        holdBackRepaymentDateHistory = contact_by_id['properties']['holdback_repayment_date']['versions']
    except KeyError:
        holdBackRepaymentDateHistory = None
    try:
        paymentNotes = contact_by_id['properties']['payment_notes']['value']
    except KeyError:
        paymentNotes = None
    try:
        paymentNotesHistory = contact_by_id['properties']['payment_notes']['versions']
    except KeyError:
        paymentNotesHistory = None
    try:
        tuitionCollected = contact_by_id['properties']['tuition_collected']['value']
    except KeyError:
        tuitionCollected = None
    try:
        tuitionCollectedHistory = contact_by_id['properties']['tuition_collected']['versions']
    except KeyError:
        tuitionCollectedHistory = None
    try:
        tuitionUncollected = contact_by_id['properties']['tuition_uncollected']['value']
    except KeyError:
        tuitionUncollected = None
    try:
        tuitionUncollectedHistory = contact_by_id['properties']['tuition_uncollected']['versions']
    except KeyError:
        tuitionUncollectedHistory = None
    try:
        venmoInfo = contact_by_id['properties']['venmo_account_info']['value']
    except KeyError:
        venmoInfo = None
    try:
        venmoInfoHistory = contact_by_id['properties']['venmo_account_info']['versions']
    except KeyError:
        venmoInfoHistory = None
    try:
        writeOffAmount = contact_by_id['properties']['write_off_amount']['value']
    except KeyError:
        writeOffAmount = None
    try:
        writeOffAmountHistory = contact_by_id['properties']['write_off_amount']['versions']
    except KeyError:
        writeOffAmountHistory = None
    try:
        alcoholDrinkFrequency = contact_by_id['properties']['alcoholic_drink_frequency']['value']
    except KeyError:
        alcoholDrinkFrequency = None
    try:
        alcoholDrinkFrequencyHistory = contact_by_id['properties']['alcoholic_drink_frequency']['versions']
    except KeyError:
        alcoholDrinkFrequencyHistory = None
    try:
        alcoholDrinkPreference = contact_by_id['properties']['alcoholic_drink_preferences']['value']
    except KeyError:
        alcoholDrinkPreference = None
    try:
        alcoholDrinkPreferenceHistory = contact_by_id['properties']['alcoholic_drink_preferences']['versions']
    except KeyError:
        alcoholDrinkPreferenceHistory = None
    try:
        allergies = contact_by_id['properties']['allergies']['value']
    except KeyError:
        allergies = None
    try:
        allergiesHistory = contact_by_id['properties']['allergies']['versions']
    except KeyError:
        allergiesHistory = None
    try:
        dietaryRestrictions = contact_by_id['properties']['dietary_restrictions']['value']
    except KeyError:
        dietaryRestrictions = None
    try:
        dietaryRestrictionsHistory = contact_by_id['properties']['dietary_restrictions']['versions']
    except KeyError:
        dietaryRestrictionsHistory = None
    try:
        fears = contact_by_id['properties']['fears']['value']
    except KeyError:
        fears = None
    try:
        fearsHistory = contact_by_id['properties']['fears']['versions']
    except KeyError:
        fearsHistory = None
    try:
        insuranceCompany = contact_by_id['properties']['insurance_company']['value']
    except KeyError:
        insuranceCompany = None
    try:
        insuranceCompanyHistory = contact_by_id['properties']['insurance_company']['versions']
    except KeyError:
        insuranceCompanyHistory = None
    try:
        chronicConditions = contact_by_id['properties']['chronic_conditions']['value']
    except KeyError:
        chronicConditions = None
    try:
        chronicConditionsHistory = contact_by_id['properties']['chronic_conditions']['versions']
    except KeyError:
        chronicConditionsHistory = None
    try:
        medications = contact_by_id['properties']['medications']['value']
    except KeyError:
        medications = None
    try:
        medicationsHistory = contact_by_id['properties']['medications']['versions']
    except KeyError:
        medicationsHistory = None
    try:
        recentInjuries = contact_by_id['properties']['recent_injuries']['value']
    except KeyError:
        recentInjuries = None
    try:
        recentInjuriesHistory = contact_by_id['properties']['recent_injuries']['versions']
    except KeyError:
        recentInjuriesHistory = None
    try:
        stressFactors = contact_by_id['properties']['stress_factors']['value']
    except KeyError:
        stressFactors = None
    try:
        stressFactorsHistory = contact_by_id['properties']['stress_factors']['versions']
    except KeyError:
        stressFactorsHistory = None
    try:
        currentlyOnContracts = contact_by_id['properties']['currently_on_contract']['value']
    except KeyError:
        currentlyOnContracts = None
    try:
        currentlyOnContractsHistory = contact_by_id['properties']['currently_on_contract']['versions']
    except KeyError:
        currentlyOnContractsHistory = None
    try:
        currentContractCompany = contact_by_id['properties']['current_contract_company']['value']
    except KeyError:
        currentContractCompany = None
    try:
        currentContractCompanyHistory = contact_by_id['properties']['current_contract_company']['versions']
    except KeyError:
        currentContractCompanyHistory = None
    try:
        currentManager = contact_by_id['properties']['current_manager']['value']
    except KeyError:
        currentManager = None
    try:
        currentManagerHistory = contact_by_id['properties']['current_manager']['versions']
    except KeyError:
        currentManagerHistory = None
    try:
        employmentStatus = contact_by_id['properties']['employment_status']['value']
    except KeyError:
        employmentStatus = None
    try:
        employmentStatusHistory = contact_by_id['properties']['employment_status']['versions']
    except KeyError:
        employmentStatusHistory = None
    try:
        functionalSpecialties = contact_by_id['properties']['functional_specialties']['value']
    except KeyError:
        functionalSpecialties = None
    try:
        functionalSpecialtiesHistory = contact_by_id['properties']['functional_specialties']['versions']
    except KeyError:
        functionalSpecialtiesHistory = None
    try:
        industryFocus = contact_by_id['properties']['industry_focus']['value']
    except KeyError:
        industryFocus = None
    try:
        industryFocusHistory = contact_by_id['properties']['industry_focus']['versions']
    except KeyError:
        industryFocusHistory = None
    try:
        nextPerformanceReview = contact_by_id['properties']['next_performance_review']['value']
    except KeyError:
        nextPerformanceReview = None
    try:
        nextPerformanceReviewHistory = contact_by_id['properties']['next_performance_review']['versions']
    except KeyError:
        nextPerformanceReviewHistory = None
    try:
        notablePreTCCompanies = contact_by_id['properties']['notable_pre_tc_companies']['value']
    except KeyError:
        notablePreTCCompanies = None
    try:
        notablePreTCCompaniesHistory = contact_by_id['properties']['notable_pre_tc_companies']['versions']
    except KeyError:
        notablePreTCCompaniesHistory = None



    # OG PROPERTIES

    try:
        email = contact_by_id['properties']['email']['value']
    except KeyError:
        email = None
    try:
        emailHistory = contact_by_id['properties']['email']['versions']
    except KeyError:
        emailHistory = None
    try:
        firstname = contact_by_id['properties']['firstname']['value']
    except KeyError:
        firstname = None
    try:
        firstnameHistory = contact_by_id['properties']['firstname']['versions']
    except KeyError:
        firstnameHistory = None
    try:
        lastname = contact_by_id['properties']['lastname']['value']
    except KeyError:
        lastname = None
    try:
        lastnameHistory = contact_by_id['properties']['lastname']['versions']
    except KeyError:
        lastnameHistory = None
    try:
        lifecyclestage = contact_by_id['properties']['lifecyclestage']['value']
    except KeyError:
        lifecyclestage = None
    try:
        lifecyclestageHistory = contact_by_id['properties']['lifecyclestage']['versions']
    except KeyError:
        lifecyclestageHistory = None
    try:
        website = contact_by_id['properties']['website']['value']
    except KeyError:
        website = None
    try:
        websiteHistory = contact_by_id['properties']['website']['versions']
    except KeyError:
        websiteHistory = None
    try:
        lead_source = contact_by_id['properties']['lead_source']['value']
    except KeyError:
        lead_source = None
    try:
        lead_sourceHistory = contact_by_id['properties']['lead_source']['versions']
    except KeyError:
        lead_sourceHistory = None
    try:
        jobtitle = contact_by_id['properties']['jobtitle']['value']
    except KeyError:
        jobtitle = None
    try:
        jobtitleHistory = contact_by_id['properties']['jobtitle']['versions']
    except KeyError:
        jobtitleHistory = None
    try:
        company = contact_by_id['properties']['company']['value']
    except KeyError:
        company = None
    try:
        companyHistory = contact_by_id['properties']['company']['versions']
    except KeyError:
        companyHistory = None
    try:
        notes_last_updated = contact_by_id['properties']['notes_last_updated']['value']
    except KeyError:
        notes_last_updated = None
    try:
        notes_last_updatedHistory = contact_by_id['properties']['notes_last_updated']['versions']
    except KeyError:
        notes_last_updatedHistory = None
    try:
        createdate = contact_by_id['properties']['createdate']['value']
    except KeyError:
        createdate = None
    try:
        createdateHistory = contact_by_id['properties']['createdate']['versions']
    except KeyError:
        createdateHistory = None
    try:
        slack_handle = contact_by_id['properties']['slack_handle']['value']
    except KeyError:
        slack_handle = None
    try:
        slack_handleHistory = contact_by_id['properties']['slack_handle']['versions']
    except KeyError:
        slack_handleHistory = None
    try:
        github = contact_by_id['properties']['github']['value']
    except KeyError:
        github = None
    try:
        githubHistory = contact_by_id['properties']['github']['versions']
    except KeyError:
        githubHistory = None
    try:
        medium = contact_by_id['properties']['medium']['value']
    except KeyError:
        medium = None
    try:
        mediumHistory = contact_by_id['properties']['medium']['versions']
    except KeyError:
        mediumHistory = None
    try:
        twitterhandle = contact_by_id['properties']['twitterhandle']['value']
    except KeyError:
        twitterhandle = None
    try:
        twitterhandleHistory = contact_by_id['properties']['twitterhandle']['versions']
    except KeyError:
        twitterhandleHistory = None
    try:
        linkedin = contact_by_id['properties']['linkedin']['value']
    except KeyError:
        linkedin = None
    try:
        linkedinHistory = contact_by_id['properties']['linkedin']['versions']
    except KeyError:
        linkedinHistory = None
    try:
        hs_analytics_last_url = contact_by_id['properties']['hs_analytics_last_url']['value']
    except KeyError:
        hs_analytics_last_url = None
    try:
        hs_analytics_last_urlHistory = contact_by_id['properties']['hs_analytics_last_url']['versions']
    except KeyError:
        hs_analytics_last_urlHistory = None
    try:
        num_conversion_events = contact_by_id['properties']['num_conversion_events']['value']
    except KeyError:
        num_conversion_events = None
    try:
        num_conversion_eventsHistory = contact_by_id['properties']['num_conversion_events']['versions']
    except KeyError:
        num_conversion_eventsHistory = None
    try:
        num_unique_conversion_events = contact_by_id['properties']['num_unique_conversion_events']['value']
    except KeyError:
        num_unique_conversion_events = None
    try:
        num_unique_conversion_eventsHistory = contact_by_id[
            'properties']['num_unique_conversion_events']['versions']
    except KeyError:
        num_unique_conversion_eventsHistory = None
    try:
        curriculum_grade = contact_by_id['properties']['curriculum_grade']['value']
    except KeyError:
        curriculum_grade = None
    try:
        curriculum_gradeHistory = contact_by_id['properties']['curriculum_grade']['versions']
    except KeyError:
        curriculum_gradeHistory = None
    try:
        curriculum_detailed_feedback = contact_by_id['properties']['curriculum_detailed_feedback']['value']
    except:
        curriculum_detailed_feedback = None
    try:
        curriculum_detailed_feedbackHistory = contact_by_id[
            'properties']['curriculum_detailed_feedback']['versions']
    except KeyError:
        curriculum_detailed_feedbackHistory = None
    try:
        project_grade = contact_by_id['properties']['project_grade']['value']
    except KeyError:
        project_grade = None
    try:
        project_gradeHistory = contact_by_id['properties']['project_grade']['versions']
    except KeyError:
        project_gradeHistory = None
    try:
        project_detailed_feedback = contact_by_id['properties']['project_detailed_feedback']['value']
    except:
        project_detailed_feedback = None
    try:
        project_detailed_feedbackHistory = contact_by_id[
            'properties']['project_detailed_feedback']['versions']
    except KeyError:
        project_detailed_feedbackHistory = None
    try:
        career_development_grade = contact_by_id['properties']['career_development_grade']['value']
    except KeyError:
        career_development_grade = None
    try:
        career_development_gradeHistory = contact_by_id[
            'properties']['career_development_grade']['versions']
    except KeyError:
        career_development_gradeHistory = None
    try:
        career_development_detailed_feedback = contact_by_id[
            'properties']['career_development_detailed_feedback']['value']
    except KeyError:
        career_development_detailed_feedback = None
    try:
        career_development_detailed_feedbackHistory = contact_by_id[
            'properties']['career_development_detailed_feedback']['versions']
    except KeyError:
        career_development_detailed_feedbackHistory = None
    try:
        overall_grade = contact_by_id['properties']['overall_grade']['value']
    except KeyError:
        overall_grade = None
    try:
        overall_gradeHistory = contact_by_id['properties']['overall_grade']['versions']
    except KeyError:
        overall_gradeHistory = None
    try:
        general_detailed_feedback = contact_by_id['properties']['general_detailed_feedback']['value']
    except KeyError:
        general_detailed_feedback = None
    try:
        general_detailed_feedbackHistory = contact_by_id[
            'properties']['general_detailed_feedback']['versions']
    except KeyError:
        general_detailed_feedbackHistory = None
    try:
        good_standing = contact_by_id['properties']['good_standing']['value']
    except KeyError:
        good_standing = None
    try:
        good_standingHistory = contact_by_id['properties']['good_standing']['value']
    except KeyError:
        good_standingHistory = None
    try:
        tc_cohort = contact_by_id['properties']['tc_cohort']['value']
    except KeyError:
        tc_cohort = None
    try:
        tc_cohortHistory = contact_by_id['properties']['tc_cohort']['versions']
    except KeyError:
        tc_cohortHistory = None
    try:
        tc_email = contact_by_id['properties']['tc_email']['value']
    except KeyError:
        tc_email = None
    try:
        tc_emailHistory = contact_by_id['properties']['tc_email']['versions']
    except KeyError:
        tc_emailHistory = None
    try:
        tc_grad_date = contact_by_id['properties']['tc_grad_date']['value']
    except KeyError:
        tc_grad_date = None
    try:
        tc_grad_dateHistory = contact_by_id['properties']['tc_grad_date']['versions']
    except KeyError:
        tc_grad_dateHistory = None
    try:
        tc_projects = contact_by_id['properties']['tc_projects']['value']
    except KeyError:
        tc_projects = None
    try:
        tc_projectsHistory = contact_by_id['properties']['tc_projects']['versions']
    except KeyError:
        tc_projectsHistory = None
    try:
        tc_start_date = contact_by_id['properties']['tc_start_date']['value']
    except KeyError:
        tc_start_date = None
    try:
        tc_start_dateHistory = contact_by_id['properties']['tc_start_date']['versions']
    except KeyError:
        tc_start_dateHistory = None
    try:
        tc_track = contact_by_id['properties']['tc_track']['value']
    except KeyError:
        tc_track = None
    try:
        tc_trackHistory = contact_by_id['properties']['tc_track']['versions']
    except KeyError:
        tc_trackHistory = None
    try:
        n140_character_bio = contact_by_id['properties']['n140_character_bio']['value']
    except KeyError:
        n140_character_bio = None
    try:
        n140_character_bioHistory = contact_by_id['properties']['n140_character_bio']['versions']
    except KeyError:
        n140_character_bioHistory = None
    try:
        mbti_types = contact_by_id['properties']['mbti_types']['value']
    except KeyError:
        mbti_types = None
    try:
        mbti_typesHistory = contact_by_id['properties']['mbti_types']['versions']
    except KeyError:
        mbti_typesHistory = None
    try:
        hs_eventbrite_lastregisteredevent = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredevent']['value']
    except KeyError:
        hs_eventbrite_lastregisteredevent = None
    try:
        hs_eventbrite_lastregisteredeventHistory = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredevent']['versions']
    except KeyError:
        hs_eventbrite_lastregisteredeventHistory = None
    try:
        hs_eventbrite_lastregisteredeventdate = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredeventdate']['value']
    except:
        hs_eventbrite_lastregisteredeventdate = None
    try:
        hs_eventbrite_lastregisteredeventdateHistory = contact_by_id[
            'properties']['hs_eventbrite_lastregisteredeventdate']['versions']
    except KeyError:
        hs_eventbrite_lastregisteredeventdateHistory = None
    try:
        are_you_open_to_new_roles_ = contact_by_id['properties']['are_you_open_to_new_roles_']['value']
    except KeyError:
        are_you_open_to_new_roles_ = None
    try:
        are_you_open_to_new_roles_History = contact_by_id[
            'properties']['are_you_open_to_new_roles_']['versions']
    except KeyError:
        are_you_open_to_new_roles_History = None
    try:
        job1CompanyName = contact_by_id['properties']['job_1_company_name']['value']
    except KeyError:
        job1CompanyName = None
    try:
        job1CompanyNameHistory = contact_by_id['properties']['job_1_company_name']['versions']
    except KeyError:
        job1CompanyNameHistory = None
    try:
        job1EndDate = contact_by_id['properties']['job_1_end_date']['value']
    except KeyError:
        job1EndDate = None
    try:
        job1EndDateHistory = contact_by_id['properties']['job_1_end_date']['versions']
    except KeyError:
        job1EndDateHistory = None
    try:
        job1Equity = contact_by_id['properties']['equity']['value']
    except KeyError:
        job1Equity = None
    try:
        job1EquityHistory = contact_by_id['properties']['equity']['versions']
    except KeyError:
        job1EquityHistory = None
    try:
        job1OfficeAdress = contact_by_id['properties']['office_address_location']['value']
    except KeyError:
        job1OfficeAdress = None
    try:
        job1OfficeAdressHistory = contact_by_id['properties']['office_address_location']['versions']
    except KeyError:
        job1OfficeAdressHistory = None
    try:
        job1Compensation = contact_by_id['properties']['other_compensation']['value']
    except KeyError:
        job1Compensation = None
    try:
        job1CompensationHistory = contact_by_id['properties']['other_compensation']['versions']
    except KeyError:
        job1CompensationHistory = None
    try:
        job1PerformanceReview1 = contact_by_id['properties']['job_1_performance_review_1']['value']
    except KeyError:
        job1PerformanceReview1 = None
    try:
        job1PerformanceReview1History = contact_by_id['properties']['job_1_performance_review_1']['versions']
    except KeyError:
        job1PerformanceReview1History = None
    try:
        job1PerformanceReview2 = contact_by_id['properties']['job_1_performance_review_2']['value']
    except KeyError:
        job1PerformanceReview2 = None
    try:
        job1PerformanceReview2History = contact_by_id['properties']['job_1_performance_review_2']['versions']
    except KeyError:
        job1PerformanceReview2History = None
    try:
        job1PerformanceReview3 = contact_by_id['properties']['job_1_performance_review_3']['value']
    except KeyError:
        job1PerformanceReview3 = None
    try:
        job1PerformanceReview3History = contact_by_id['properties']['job_1_performance_review_3']['versions']
    except KeyError:
        job1PerformanceReview3History = None
    try:
        job1PerformanceReview4 = contact_by_id['properties']['job_1_performance_review_4']['value']
    except KeyError:
        job1PerformanceReview4 = None
    try:
        job1PerformanceReview4History = contact_by_id['properties']['job_1_performance_review_4']['versions']
    except KeyError:
        job1PerformanceReview4History = None
    try:
        job1PerformanceReview5 = contact_by_id['properties']['job_1_performance_review_5']['value']
    except KeyError:
        job1PerformanceReview5 = None
    try:
        job1PerformanceReview5History = contact_by_id['properties']['job_1_performance_review_5']['versions']
    except KeyError:
        job1PerformanceReview5History = None
    try:
        job1PerformanceReview6 = contact_by_id['properties']['job_1_performance_review_6']['value']
    except KeyError:
        job1PerformanceReview6 = None
    try:
        job1PerformanceReview6History = contact_by_id['properties']['job_1_performance_review_6']['versions']
    except KeyError:
        job1PerformanceReview6History = None
    try:
        job1PerformanceReview7 = contact_by_id['properties']['job_1_performance_review_7']['value']
    except KeyError:
        job1PerformanceReview7 = None
    try:
        job1PerformanceReview7History = contact_by_id['properties']['job_1_performance_review_7']['versions']
    except KeyError:
        job1PerformanceReview7History = None
    try:
        job1PerformanceReview8 = contact_by_id['properties']['job_1_performance_review_8']['value']
    except KeyError:
        job1PerformanceReview8 = None
    try:
        job1PerformanceReview8History = contact_by_id['properties']['job_1_performance_review_8']['versions']
    except KeyError:
        job1PerformanceReview8History = None
    try:
        job1Salary = contact_by_id['properties']['salary']['value']
    except KeyError:
        job1Salary = None
    try:
        job1SalaryHistory = contact_by_id['properties']['salary']['versions']
    except KeyError:
        job1SalaryHistory = None
    try:
        job1StartDate = contact_by_id['properties']['start_date']['value']
    except KeyError:
        job1StartDate = None
    try:
        job1StartDateHistory = contact_by_id['properties']['start_date']['versions']
    except KeyError:
        job1StartDateHistory = None
    try:
        job1Title = contact_by_id['properties']['job_1_title']['value']
    except KeyError:
        job1Title = None
    try:
        job1TitleHistory = contact_by_id['properties']['job_1_title']['versions']
    except KeyError:
        job1TitleHistory = None
    try:
        job2CompanyName = contact_by_id['properties']['job_2_company_name']['value']
    except KeyError:
        job2CompanyName = None
    try:
        job2CompanyNameHistory = contact_by_id['properties']['job_2_company_name']['versions']
    except KeyError:
        job2CompanyNameHistory = None
    try:
        job2EndDate = contact_by_id['properties']['job_2_end_date']['value']
    except KeyError:
        job2EndDate = None
    try:
        job2EndDateHistory = contact_by_id['properties']['job_2_end_date']['versions']
    except KeyError:
        job2EndDateHistory = None
    try:
        job2Equity = contact_by_id['properties']['job_2_equity']['value']
    except KeyError:
        job2Equity = None
    try:
        job2EquityHistory = contact_by_id['properties']['job_2_equity']['versions']
    except KeyError:
        job2EquityHistory = None
    try:
        job2Location = contact_by_id['properties']['job_2_location']['value']
    except KeyError:
        job2Location = None
    try:
        job2LocationHistory = contact_by_id['properties']['job_2_location']['versions']
    except KeyError:
        job2LocationHistory = None
    try:
        job2Compensation = contact_by_id['properties']['job_2_other_compensation']['value']
    except KeyError:
        job2Compensation = None
    try:
        job2CompensationHistory = contact_by_id['properties']['job_2_other_compensation']['versions']
    except KeyError:
        job2CompensationHistory = None
    try:
        job2PerformanceReview1 = contact_by_id['properties']['job_2_performance_review_1']['value']
    except KeyError:
        job2PerformanceReview1 = None
    try:
        job2PerformanceReview1History = contact_by_id['properties']['job_2_performance_review_1']['versions']
    except KeyError:
        job2PerformanceReview1History = None
    try:
        job2PerformanceReview2 = contact_by_id['properties']['job_2_performance_review_2']['value']
    except KeyError:
        job2PerformanceReview2 = None
    try:
        job2PerformanceReview2History = contact_by_id['properties']['job_2_performance_review_2']['versions']
    except KeyError:
        job2PerformanceReview2History = None
    try:
        job2PerformanceReview3 = contact_by_id['properties']['job_2_performance_review_3']['value']
    except KeyError:
        job2PerformanceReview3 = None
    try:
        job2PerformanceReview3History = contact_by_id['properties']['job_2_performance_review_3']['versions']
    except KeyError:
        job2PerformanceReview3History = None
    try:
        job2PerformanceReview4 = contact_by_id['properties']['job_3_performance_review_4']['value']
    except KeyError:
        job2PerformanceReview4 = None
    try:
        job2PerformanceReview4History = contact_by_id['properties']['job_3_performance_review_4']['versions']
    except KeyError:
        job2PerformanceReview4History = None
    try:
        job2PerformanceReview5 = contact_by_id['properties']['job_2_performance_review_5']['value']
    except KeyError:
        job2PerformanceReview5 = None
    try:
        job2PerformanceReview5History = contact_by_id['properties']['job_2_performance_review_5']['versions']
    except KeyError:
        job2PerformanceReview5History = None
    try:
        job2PerformanceReview6 = contact_by_id['properties']['job_2_performance_review_6']['value']
    except KeyError:
        job2PerformanceReview6 = None
    try:
        job2PerformanceReview6History = contact_by_id['properties']['job_2_performance_review_6']['versions']
    except KeyError:
        job2PerformanceReview6History = None
    try:
        job2PerformanceReview7 = contact_by_id['properties']['job_2_performance_review_7']['value']
    except KeyError:
        job2PerformanceReview7 = None
    try:
        job2PerformanceReview7History = contact_by_id['properties']['job_2_performance_review_7']['versions']
    except KeyError:
        job2PerformanceReview7History = None
    try:
        job2PerformanceReview8 = contact_by_id['properties']['job_2_performance_review_8']['value']
    except KeyError:
        job2PerformanceReview8 = None
    try:
        job2PerformanceReview8History = contact_by_id['properties']['job_2_performance_review_8']['versions']
    except KeyError:
        job2PerformanceReview8History = None
    try:
        job2Salary = contact_by_id['properties']['job_2_salary']['value']
    except KeyError:
        job2Salary = None
    try:
        job2SalaryHistory = contact_by_id['properties']['job_2_salary']['versions']
    except KeyError:
        job2SalaryHistory = None
    try:
        job2StartDate = contact_by_id['properties']['job_2_start_date']['value']
    except KeyError:
        job2StartDate = None
    try:
        job2StartDateHistory = contact_by_id['properties']['job_2_start_date']['versions']
    except KeyError:
        job2StartDateHistory = None
    try:
        job2Title = contact_by_id['properties']['job_2_title']['value']
    except KeyError:
        job2Title = None
    try:
        job2TitleHistory = contact_by_id['properties']['job_2_title']['versions']
    except KeyError:
        job2TitleHistory = None
    try:
        job3CompanyName = contact_by_id['properties']['job_3_company_name']['value']
    except KeyError:
        job3CompanyName = None
    try:
        job3CompanyNameHistory = contact_by_id['properties']['job_3_company_name']['versions']
    except KeyError:
        job3CompanyNameHistory = None
    try:
        job3EndDate = contact_by_id['properties']['job_3_end_date']['value']
    except KeyError:
        job3EndDate = None
    try:
        job3EndDateHistory = contact_by_id['properties']['job_3_end_date']['versions']
    except KeyError:
        job3EndDateHistory = None
    try:
        job3Equity = contact_by_id['properties']['job_3_equity']['value']
    except KeyError:
        job3Equity = None
    try:
        job3EquityHistory = contact_by_id['properties']['job_3_equity']['versions']
    except KeyError:
        job3EquityHistory = None
    try:
        job3Location = contact_by_id['properties']['job_3_location']['value']
    except KeyError:
        job3Location = None
    try:
        job3LocationHistory = contact_by_id['properties']['job_3_location']['versions']
    except KeyError:
        job3LocationHistory = None
    try:
        job3Compensation = contact_by_id['properties']['job_3_other_compensation']['value']
    except KeyError:
        job3Compensation = None
    try:
        job3CompensationHistory = contact_by_id['properties']['job_3_other_compensation']['versions']
    except KeyError:
        job3CompensationHistory = None
    try:
        job3PerformanceReview1 = contact_by_id['properties']['job_3_performance_review_1']['value']
    except KeyError:
        job3PerformanceReview1 = None
    try:
        job3PerformanceReview1History = contact_by_id['properties']['job_3_performance_review_1']['versions']
    except KeyError:
        job3PerformanceReview1History = None
    try:
        job3PerformanceReview2 = contact_by_id['properties']['job_3_performance_review_2']['value']
    except KeyError:
        job3PerformanceReview2 = None
    try:
        job3PerformanceReview2History = contact_by_id['properties']['job_3_performance_review_2']['versions']
    except KeyError:
        job3PerformanceReview2History = None
    try:
        job3PerformanceReview3 = contact_by_id['properties']['job_3_performance_review_3']['value']
    except KeyError:
        job3PerformanceReview3 = None
    try:
        job3PerformanceReview3History = contact_by_id['properties']['job_3_performance_review_3']['versions']
    except KeyError:
        job3PerformanceReview3History = None
    try:
        job3PerformanceReview4 = contact_by_id['properties']['job_3_performance_review_4']['value']
    except KeyError:
        job3PerformanceReview4 = None
    try:
        job3PerformanceReview4History = contact_by_id['properties']['job_3_performance_review_4']['versions']
    except KeyError:
        job3PerformanceReview4History = None
    try:
        job3PerformanceReview5 = contact_by_id['properties']['job_3_performance_review_5']['value']
    except KeyError:
        job3PerformanceReview5 = None
    try:
        job3PerformanceReview5History = contact_by_id['properties']['job_3_performance_review_5']['versions']
    except KeyError:
        job3PerformanceReview5History = None
    try:
        job3PerformanceReview6 = contact_by_id['properties']['job_3_performance_review_6']['value']
    except KeyError:
        job3PerformanceReview6 = None
    try:
        job3PerformanceReview6History = contact_by_id['properties']['job_3_performance_review_6']['versions']
    except KeyError:
        job3PerformanceReview6History = None
    try:
        job3PerformanceReview7 = contact_by_id['properties']['job_3_performance_review_7']['value']
    except KeyError:
        job3PerformanceReview7 = None
    try:
        job3PerformanceReview7History = contact_by_id['properties']['job_3_performance_review_7']['versions']
    except KeyError:
        job3PerformanceReview7History = None
    try:
        job3PerformanceReview8 = contact_by_id['properties']['job_3_performance_review_8']['value']
    except KeyError:
        job3PerformanceReview8 = None
    try:
        job3PerformanceReview8History = contact_by_id['properties']['job_3_performance_review_8']['versions']
    except KeyError:
        job3PerformanceReview8History = None
    try:
        job3Salary = contact_by_id['properties']['job_3_salary']['value']
    except KeyError:
        job3Salary = None
    try:
        job3SalaryHistory = contact_by_id['properties']['job_3_salary']['versions']
    except KeyError:
        job3SalaryHistory = None
    try:
        job3StartDate = contact_by_id['properties']['job_3_start_date']['value']
    except KeyError:
        job3StartDate = None
    try:
        job3StartDateHistory = contact_by_id['properties']['job_3_start_date']['versions']
    except KeyError:
        job3StartDateHistory = None
    try:
        job3Title = contact_by_id['properties']['job_3_title']['value']
    except KeyError:
        job3Title = None
    try:
        job3TitleHistory = contact_by_id['properties']['job_3_title']['versions']
    except KeyError:
        job3TitleHistory = None
    try:
        pipelineCompany1Name = contact_by_id['properties']['pipeline_activity_company_1_name']['value']
    except KeyError:
        pipelineCompany1Name = None
    try:
        pipelineCompany1NameHistory = contact_by_id['properties']['pipeline_activity_company_1_name']['versions']
    except KeyError:
        pipelineCompany1NameHistory = None
    try:
        pipelineCompany1Status = contact_by_id['properties']['pipeline_activity_company_1_status']['value']
    except KeyError:
        pipelineCompany1Status = None
    try:
        pipelineCompany1StatusHistory = contact_by_id['properties']['pipeline_activity_company_1_status']['versions']
    except KeyError:
        pipelineCompany1StatusHistory = None
    try:
        pipelineCompany1Summary = contact_by_id['properties']['pipeline_activity_company_1_summary']['value']
    except KeyError:
        pipelineCompany1Summary = None
    try:
        pipelineCompany1SummaryHistory = contact_by_id['properties']['pipeline_activity_company_1_summary']['versions']
    except KeyError:
        pipelineCompany1SummaryHistory = None
    try:
        pipelineCompany2Name = contact_by_id['properties']['pipeline_activity_company_2_name']['value']
    except KeyError:
        pipelineCompany2Name = None
    try:
        pipelineCompany2NameHistory = contact_by_id['properties']['pipeline_activity_company_2_name']['versions']
    except KeyError:
        pipelineCompany2NameHistory = None
    try:
        pipelineCompany2Status = contact_by_id['properties']['pipeline_activity_company_2_status']['value']
    except KeyError:
        pipelineCompany2Status = None
    try:
        pipelineCompany2StatusHistory = contact_by_id['properties']['pipeline_activity_company_2_status']['versions']
    except KeyError:
        pipelineCompany2StatusHistory = None
    try:
        pipelineCompany2Summary = contact_by_id['properties']['pipeline_activity_company_2_summary']['value']
    except KeyError:
        pipelineCompany2Summary = None
    try:
        pipelineCompany2SummaryHistory = contact_by_id['properties']['pipeline_activity_company_2_summary']['versions']
    except KeyError:
        pipelineCompany2SummaryHistory = None
    try:
        pipelineCompany3Name = contact_by_id['properties']['pipeline_activity_company_3_name']['value']
    except KeyError:
        pipelineCompany3Name = None
    try:
        pipelineCompany3NameHistory = contact_by_id['properties']['pipeline_activity_company_3_name']['versions']
    except KeyError:
        pipelineCompany3NameHistory = None
    try:
        pipelineCompany3Status = contact_by_id['properties']['pipeline_activity_company_3_status']['value']
    except KeyError:
        pipelineCompany3Status = None
    try:
        pipelineCompany3StatusHistory = contact_by_id['properties']['pipeline_activity_company_3_status']['versions']
    except KeyError:
        pipelineCompany3StatusHistory = None
    try:
        pipelineCompany3Summary = contact_by_id['properties']['pipeline_activity_company_3_summary']['value']
    except KeyError:
        pipelineCompany3Summary = None
    try:
        pipelineCompany3SummaryHistory = contact_by_id['properties']['pipeline_activity_company_3_summary']['versions']
    except KeyError:
        pipelineCompany3SummaryHistory = None
    try:
        pipelineCompany4Name = contact_by_id['properties']['pipeline_activity_company_4_name']['value']
    except KeyError:
        pipelineCompany4Name = None
    try:
        pipelineCompany4NameHistory = contact_by_id['properties']['pipeline_activity_company_4_name']['versions']
    except KeyError:
        pipelineCompany4NameHistory = None
    try:
        pipelineCompany4Status = contact_by_id['properties']['pipeline_activity_company_4_status']['value']
    except KeyError:
        pipelineCompany4Status = None
    try:
        pipelineCompany4StatusHistory = contact_by_id['properties']['pipeline_activity_company_4_status']['versions']
    except KeyError:
        pipelineCompany4StatusHistory = None
    try:
        pipelineCompany4Summary = contact_by_id['properties']['pipeline_activity_company_4_summary']['value']
    except KeyError:
        pipelineCompany4Summary = None
    try:
        pipelineCompany4SummaryHistory = contact_by_id['properties']['pipeline_activity_company_4_summary']['versions']
    except KeyError:
        pipelineCompany4SummaryHistory = None
    try:
        pipelineCompany5Name = contact_by_id['properties']['pipeline_activity_company_5_name']['value']
    except KeyError:
        pipelineCompany5Name = None
    try:
        pipelineCompany5NameHistory = contact_by_id['properties']['pipeline_activity_company_5_name']['versions']
    except KeyError:
        pipelineCompany5NameHistory = None
    try:
        pipelineCompany5Status = contact_by_id['properties']['pipeline_activity_company_5_status']['value']
    except KeyError:
        pipelineCompany5Status = None
    try:
        pipelineCompany5StatusHistory = contact_by_id['properties']['pipeline_activity_company_5_status']['versions']
    except KeyError:
        pipelineCompany5StatusHistory = None
    try:
        pipelineCompany5Summary = contact_by_id['properties']['pipeline_activity_company_5_summary']['value']
    except KeyError:
        pipelineCompany5Summary = None
    try:
        pipelineCompany5SummaryHistory = contact_by_id['properties']['pipeline_activity_company_5_summary']['versions']
    except KeyError:
        pipelineCompany5SummaryHistory = None
    try:
        mentorRoleReachable3Years = contact_by_id['properties']['mentor_role_reachable_in_3years']['value']
    except KeyError:
        mentorRoleReachable3Years = None
    try:
        mentorRoleReachable3YearsHistory = contact_by_id['properties']['mentor_role_reachable_in_3years']['versions']
    except KeyError:
        mentorRoleReachable3YearsHistory = None
    


    with open('data/{}.json'.format(email), 'w') as f:
        data = {
            "hubspot_id": "{}".format(i),
            "email": {"value": email, "versions": emailHistory},
            "firstname": {"value": firstname, "versions": firstnameHistory},
            "lastname": {"value": lastname, "versions": lastnameHistory},
            "lifecycle_stage": {"value": lifecyclestage, "versions": lifecyclestageHistory},
            "good_standing": {"value": good_standing, "versions": good_standingHistory},
            "personal_info": {
                "closest_friend_name": {"value": closestFriend, "versions": closestFriendHistory},
                "closest_friend_number": {"value": closestFriendNumber, "versions": closestFriendNumberHistory},
                "fax": {"value": fax, "versions": faxHistory},
                "legal_name": {"value": legalName, "versions": legalNameHistory},
                "grew_up_in": {"value": growUpLocation, "versions": growUpLocationHistory},
                "weight": {"value": weight, "versions": weightHistory},
                "siblings": {"value": siblings, "versions": siblingsHistory},
                "religious_affiliations": {"value": religiousAffiliations, "versions": religiousAffiliationsHistory},
                "preferred_name": {"value": preferredName, "versions": preferredNameHistory},
                "notes_on_sibling": {"value": siblingNotes, "versions": siblingNotesHistory},
                "notes_on_children": {"value": childrenNotes, "versions": childrenNotesHistory},
                "significant_other_name": {"value": significantOtherName, "versions": significantOtherNameHistory},
                "marital_status": {"value": maritalStatus, "versions": maritalStatusHistory},
                "immigration_status": {"value": immigrationStatus, "versions": immigrationStatusHistory},
                "hobbies": {"value": hobbies, "versions": hobbiesHistory},
                "height": {"value": height, "versions": heightHistory},
                "glasses": {"value": glasses, "versions": glassesHistory},
                "gender": {"value": gender, "versions": genderHistory},
                "gear_size": {"value": gearSize, "versions": gearSizeHistory},
                "family_in_bay_area": {"value": familyInBayArea, "versions": familyInBayAreaHistory},
                "ethnicity": {"value": ethnicity, "versions": ethnicityHistory},
                "citizenship": {"value": citizenship, "versions": citizenshipHistory},
                "children": {"value": children, "versions": childrenHistory},
                "birthplace": {"value": birthplace, "versions": birthplaceHistory},
                "birthday": {"value": birthday, "versions": birthdayHistory},
                "additional_languages": {"value": languagesSpoken, "versions": languagesSpokenHistory},
                "fears": {"value": fears, "versions": fearsHistory},
                "insurance_company": {"value": insuranceCompany, "versions": insuranceCompanyHistory},
                "chronic_conditions": {"value": chronicConditions, "versions": chronicConditionsHistory},
                "medications": {"value": medications, "versions": medicationsHistory},
                "recent_injuries": {"value": recentInjuries, "versions": recentInjuriesHistory},
                "stress_factors": {"value": stressFactors, "versions": stressFactorsHistory},
                "140_bio": {"value": n140_character_bio, "versions": n140_character_bioHistory},
                "mbti": {"value": mbti_types, "versions": mbti_typesHistory}
            },
            "location": {
                "bay_area_address": {"value": bayAreaAddress, "versions": bayAreaAddressHistory},
                "city": {"value": city, "versions": cityHistory},
                "country": {"value": country, "versions": countryHistory},
                "current_location": {"value": currentLocation, "versions": currentLocationHistory},
                "postal_code": {"value": postalCode, "versions": postalCodeHistory},
                "state": {"value": state, "versions": stateHistory},
                "address": {"value": address, "versions": addressHistory},
                "office_address": {"value": officeAddress, "versions": officeAddressHistory},
                "job_2": {"value": job2Location, "versions": job2LocationHistory},
                "job_3": {"value": job3Location, "versions": job3LocationHistory}
            },
            "emergency_contact": {
                "email": {"value": emergencyContactEmail, "versions": emergencyContactEmailHistory},
                "location": {"value": emergencyContactLocation, "versions": emergencyContactLocationHistory},
                "name": {"value": emergencyContactName, "versions": emergencyContactNameHistory},
                "number": {"value": emergencyContactNumber, "versions": emergencyContactNumberHistory}
            },
            "contact_info": {
                "mobilephone": {"value": mobilePhone, "versions": mobilePhoneHistory},
                "permanent_address": {"value": permanentAddress, "versions": permanentAddressHistory},
                "phone": {"value": phone, "versions": phoneHistory},
                "family_location": {"value": familyLocation, "versions": familyLocationHistory},
                "second_email": {"value": secondEmail, "versions": secondEmailHistory},
                "tc_email": {"value": tc_email, "versions": tc_emailHistory},
            },
            "offer_letter": {
                "compensation_options": {"value": compensationOptions, "versions": compensationOptionsHistory},
                "manager_time": {"value": managerTimeAtCompany, "versions": managerTimeAtCompanyHistory},
                "manager_name": {"value": nameOfManager, "versions": nameOfManagerHistory},
                "direct_reports_num": {"value": numOfDirectReports, "versions": numOfDirectReportsHistory},
                "employee_num": {"value": numOfEmployeesOfferLetter, "versions": numOfEmployeesOfferLetterHistory},
                "payment_timing_3": {"value": paymentTiming3, "versions": paymentTiming3History},
                "job_title": {"value": positionTitle, "versions": positionTitleHistory},
                "recruiter": {"value": recruiterName, "versions": recruiterNameHistory},
                "recruiter_company": {"value": recruiterCompany, "versions": recruiterCompanyHistory},
                "shares_issued": {"value": totalSharesIssued, "versions": totalSharesIssuedHistory},
                "post_money_valuation": {"value": postMoneyValuation, "versions": postMoneyValuationHistory},
                "direct_reports": {"value": managersDirectReports, "versions": managersDirectReportsHistory},
                "annualized_salary": {"value": annualizedSalary, "versions": annualizedSalaryHistory},
                "amount_raised": {"value": amountRaisedLastRound, "versions": amountRaisedLastRoundHistory},
                "round_type": {"value": roundType, "versions": roundTypeHistory},
                "bonuses": {"value": bonuses, "versions": bonusesHistory},
                "upload": {"value": offerLetterUpload, "versions": offerLetterUploadHistory},
                "fully_vested": {"value": whenFullyVested, "versions": whenFullyVestedHistory},
                "vesting_start_date": {"value": vestingStartDate, "versions": vestingStartDateHistory},
                "engagement_type": {"value": typeOfEngagement, "versions": typeOfEngagementHistory},
                "total_raised": {"value": totalAmountRaised, "versions": totalAmountRaisedHistory},
                "stock_shares": {"value": sharesOfStock, "versions": sharesOfStockHistory},
                "stock_shares2": {"value": sharesOfStock2, "versions": sharesOfStock2History},
                "stock_shares3": {"value": sharesOfStock3, "versions": sharesOfStock3History},
                "proposed_start_date": {"value": proposedStartDate, "versions": proposedStartDateHistory},
                "proposed_salary3": {"value": proposedSalaryOption3, "versions": proposedSalaryOption3History},
                "payment_timing": {"value": paymentTiming, "versions": paymentTimingHistory},
                "parent_company": {"value": parentCompanyName, "versions": parentCompanyNameHistory},
                "paid_time_off": {"value": paidTimeOff, "versions": paidTimeOffHistory},
                "other_benefits": {"value": otherBenefits, "versions": otherBenefitsHistory},
                "expiration_date": {"value": offerLetterExpirationDate, "versions": offerLetterExpirationDateHistory},
                "manager_title": {"value": managerTitle, "versions": managerTitleHistory},
                "manager_time_in_role": {"value": managerTimeInRole, "versions": managerTimeInRoleHistory},
                "last_funding_date": {"value": lastFundingRoundDate, "versions": lastFundingRoundDateHistory},
                "offer_given_date": {"value": offerGivenDate, "versions": offerGivenDateHistory},
                "bonuses2": {"value": bonuses2, "versions": bonuses2History},
                "bonuses3": {"value": bonuses3, "versions": bonuses3History},
                "benefits": {"value": benefits, "versions": benefitsHistory},
                "proposed_salary2": {"value": proposedSalaryOption2, "versions": proposedSalaryOption2History},
                "payment_schedule": {"value": paymentSchedule2, "versions": paymentSchedule2History},
                "company_name": {"value": offerLetterCompanyName, "versions": offerLetterCompanyNameHistory},
                "placed_by_recruiter": {"value": workWithRecruiter, "versions": workWithRecruiterHistory}
            },
            "career_development": {
                "priority_goals": {"value": priorityGoals, "versions": priorityGoalsHistory},
                "num_companies_reached": {"value": numCompaniesReachedOut, "versions": numCompaniesReachedOutHistory},
                "companies_reached": {"value": namesCompaniesReachedOut, "versions": namesCompaniesReachedOutHistory},
                "job_search_stage": {"value": jobSearchStage, "versions": jobSearchStageHistory},
                "feeling_this_week": {"value": feelLastWeek, "versions": feelLastWeekHistory},
                "support_this_week": {"value": supportThisWeek, "versions": supportThisWeekHistory},
                "interviewing_companies": {"value": currentlyInterviewing, "versions": currentlyInterviewingHistory},
                "extra_info": {"value": extraInfo, "versions": extraInfoHistory},
                "update_asset": {"value": carDevWeeklyUpdateAssets, "versions": carDevWeeklyUpdateAssetsHistory},
                "on_contract": {"value": currentlyOnContracts, "versions": currentlyOnContractsHistory},
                "current_contract_company": {"value": currentContractCompany, "versions": currentContractCompanyHistory},
                "current_manager": {"value": currentManager, "versions": currentManagerHistory},
                "pipeline_company1_name": {"value": pipelineCompany1Name, "versions": pipelineCompany1NameHistory},
                "pipeline_company1_status": {"value": pipelineCompany1Status, "versions": pipelineCompany1StatusHistory},
                "pipeline_company1_summary": {"value": pipelineCompany1Summary, "versions": pipelineCompany1SummaryHistory},
                "pipeline_company2_name": {"value": pipelineCompany2Name, "versions": pipelineCompany2NameHistory},
                "pipeline_company2_status": {"value": pipelineCompany2Status, "versions": pipelineCompany2StatusHistory},
                "pipeline_company2_summary": {"value": pipelineCompany2Summary, "versions": pipelineCompany2SummaryHistory},
                "pipeline_company3_name": {"value": pipelineCompany3Name, "versions": pipelineCompany3NameHistory},
                "pipeline_company3_status": {"value": pipelineCompany3Status, "versions": pipelineCompany3StatusHistory},
                "pipeline_company3_summary": {"value": pipelineCompany3Summary, "versions": pipelineCompany3SummaryHistory},
                "pipeline_company4_name": {"value": pipelineCompany4Name, "versions": pipelineCompany4NameHistory},
                "pipeline_company4_status": {"value": pipelineCompany4Status, "versions": pipelineCompany4StatusHistory},
                "pipeline_company4_summary": {"value": pipelineCompany4Summary, "versions": pipelineCompany4SummaryHistory},
                "pipeline_company5_name": {"value": pipelineCompany5Name, "versions": pipelineCompany5NameHistory},
                "pipeline_company5_status": {"value": pipelineCompany5Status, "versions": pipelineCompany5StatusHistory},
                "pipeline_company5_summary": {"value": pipelineCompany5Summary, "versions": pipelineCompany5SummaryHistory}
            },
            "career_info": {
                "work_email": {"value": currentWorkEmail, "versions": currentWorkEmailHistory},
                "employee_num": {"value": numOfEmployees, "versions": numOfEmployeesHistory},
                "tool_expertise": {"value": toolExpertise, "versions": toolExpertiseHistory},
                "sector_experience": {"value": sectorExperience, "versions": sectorExperienceHistory},
                "past_profession": {"value": pastProfession, "versions": pastProfessionHistory},
                "great_resume": {"value": greatResume, "versions": greatResumeHistory}
            },
            "program_info": {
                "feedback": {

                },
            },
            "mentor_talks": {

            },
            "financial_info": {

            },
            "events_info": {

            },
            "social_info": {

            },
            "hubspot": {

            },
            "tracking": {

            }
        }
        json_data = json.dumps(data, default=set_default)
        print('data on file for {}'.format(i))
        f.write(json_data)
        f.close()
    contacts.append(contact_by_id)
