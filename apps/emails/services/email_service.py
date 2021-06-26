import json
import logging
import requests

from django.conf import settings
from rest_framework import status

logger = logging.getLogger(__name__)


class EmailService:
    """ Service for sending emails """

    SENDINBLUE_API = 'https://api.sendinblue.com/v3'

    def send_email(self, to_email, template_id, sender=None, subject=None, data=None,
                   attachments=None, bcc=False, tags=None):
        """
        Send email using Sendinblue tool.

        Examples:
            attachments=[
                {
                    "url":"https://attachment.domain.com/foto.jpg",
                    "name":"My photo"
                },
                {
                    "content": "file",
                    "name": "name.pdf"
                }
            ]

        :param to_email: (str or list) Mail that will receive the email
        :param template_id: (int) Template id
        :param sender: (str) Sender
        :param subject: (str) Subject
        :param data: (dict) Data to be sent to the template
        :param attachments: (list) Attachments
        :param bcc: (bool) Hide email recipients
        :param tags: (list) Tags
        :return: (bool) If the email was sent correctly or not
        """
        # if email sending is enabled
        if settings.ENABLE_SENDING_EMAILS:
            # check if the mail is on the blocked mailing list
            to_email = self.is_contact_email_blocked(email=to_email)
            if not to_email:
                return False

            payload = {
                'templateId': template_id,
                'tags': [str(settings.ENVIRONMENT_NAME)]
            }

            if type(to_email) is list:
                if bcc:
                    payload['to'] = [{"email": to_email.pop(0)}]
                    payload["bcc"] = [{"email": email} for email in to_email]
                else:
                    payload['to'] = [{'email': email} for email in to_email]
            else:
                payload['to'] = [{'email': to_email}]

            if data:
                payload['params'] = data

            if subject:
                payload['subject'] = subject

            if sender:
                payload['sender'] = {'email': sender}

            if attachments:
                att = []
                for attachment in attachments:
                    att.append(attachment)

                payload['attachment'] = att

            if tags:
                payload['tags'].append(tags)

            url = '{api}/smtp/email'.format(api=self.SENDINBLUE_API)
            headers = {
                'content-type': "application/json",
                'api-key': settings.SENDINBLUE_API_KEY,
            }

            try:
                string_payload = json.dumps(payload)
                response = requests.post(
                    url=url,
                    data=string_payload,
                    headers=headers)
                # if the email was correct
                if response.status_code == status.HTTP_201_CREATED:
                    return True

                logger.exception("Email error", response.status_code)
                return False
            except Exception as ex:
                msg = "Error sending email"
                logger.exception(msg, ex)
                return False
        else:
            return True

    def is_contact_email_blocked(self, email):
        """ Verify that email is not blocked """
        try:
            url = '{api}/smtp/blockedContacts'.format(api=self.SENDINBLUE_API)
            headers = {
                'content-type': "application/json",
                'api-key': settings.SENDINBLUE_API_KEY,
            }
            response = requests.get(url=url, headers=headers)
            emails_blocked = [item.get("email") for item in response.json().get("contacts")]

            # to know if it is an email or an email list
            if type(email) is list:
                new_emails_list = []
                for email_item in email:
                    if email_item not in emails_blocked:
                        new_emails_list.append(email_item)
                return new_emails_list
            else:
                if email in emails_blocked:
                    return False

            return email
        except:
            return False
