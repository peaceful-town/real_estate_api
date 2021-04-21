import yagmail
from datetime import datetime
from API_Module.API_keypull import get_api_key

user = [EMAIL ADDRESS]
app_password = get_api_key('gmail_app')
to = [[EMAIL ADDRESS], [EMAIL ADDRESS_2]]
today = datetime.today().strftime('%b %d, %Y')
currentdate = (str(datetime.now())[:10])
# print(currentdate)
filename =('[CITY] Houses for Sale_') + currentdate + '.xlsx'

spreadsheet = 'C:\\Users\[REDACTED]\\Documents\\A Home for Us\\Realtor API\\Properties for Sale Spreadsheets' +'\\' +  filename

subject = [today,'Weekly Real Esatate Spreadsheet']
# print(subject)
content = [today, 'Weekly Real estate report. Lets get this house!', spreadsheet]

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    # print('Sent Email Succesfully')
