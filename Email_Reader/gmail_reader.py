# Script to pull emails from gmail and sort them
# Script was pulled from https://codehandbook.org/how-to-read-email-from-gmail-using-python/

# The script will now sort through emails and pulls the ones I think should be fwd. Now I just have to code the fwd job 2/11/21

# This script now sends the fwd emails. I now just have to adjust to actually get the msg, not weird script. Creating a V2, so I don't lose my place. 4/8/2021

from API_Module.API_keypull import get_api_key
from dateutil import parser
from datetime import datetime, timedelta, timezone
import smtplib
import imaplib
import email
import traceback
import yagmail

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "Removed" + ORG_EMAIL
FROM_PWD    = get_api_key('gmail_app')
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
now = datetime.now(timezone.utc)

emails_to_fwd = [Removed]

def email_fwd(msg, email_subject):
    ''' This is the yagmail module that will be used to fwd the actual msg'''
    with yagmail.SMTP(FROM_EMAIL, FROM_PWD) as yag:
        yag.send(FROM_EMAIL, email_subject, msg)
        # print('Sent Email Succesfully')


def read_email_from_gmail():
    # current_time =
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        data = mail.search(None, 'ALL')
        search_criteria = 'REVERSE DATE'
        # data = mail.sort(search_criteria, 'UTF-8', 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        #
        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    # print(msg.keys())
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_date = parser.parse(msg['date'])
                    if now-timedelta(hours=24) <= email_date <= now+timedelta(hours=24): # is within 24 hours of 07:00:
                        for item in emails_to_fwd:
                            if item in email_from:
                                email_fwd(msg, email_subject)
                                # print(item + '\n \n')
                                # print(email_subject)
                                # email_fwd(item)# Here is where I need to add the fwd function to fwd the email
                                # print("This email " + email_from + "will be fwd to Removed. ")
                        # print('From : ' + email_from)
                        # print('Subject : ' + email_subject)
                        # print('Date : ' + str(email_date) + '\n')
                    else:
                        return
    except Exception as e:
        traceback.print_exc()
        print(str(e))

read_email_from_gmail()
