# Devleoped by Abdul Rahiman Naufal
# abdulrahimannaufal@gmail.com

import subprocess
import re
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import xml.etree.ElementTree as ET
from pathlib import Path

'''arg1 = 
'''

username=sys.argv[1]

email_ID=""
config_file="C:/Program Files/LogRhythm/SmartResponse Plugins/MultiCountryLoginConfigFile.xml"

result = subprocess.run(["powershell", "-Command", "Get-ADUser -Identity "+username+" -Properties EmailAddress | Select-Object -ExpandProperty EmailAddress"], capture_output=True).stdout

s = str(result)

pattern = r"b'(.*?)\\r\\n'"

try:
    email_ID = re.search(pattern, s).group(1)   
except Exception:
    print("No email ID found.")
    sys.exit(1)



SMTP_Server=""

mail_From=""

mail_To=""


tree = ET.parse(config_file)


root = tree.getroot()


for elem in root.iter('item'):

    if(elem.attrib["name"] == "from"):

        mail_From = elem.text

    elif(elem.attrib["name"] == "to"):

        mail_To = elem.text

    elif(elem.attrib["name"] == "SMTP"):

        SMTP_Server = elem.text




mail_To=list(mail_To.split(",")) 

mail_To.append(email_ID)

msg = MIMEMultipart()

subject = "Login from another country"


html = """\

<html>

  <head></head>

  <body>

    <p>Dear User,<br>

      <br>

      Your user account was successfully logged in from another country. Kindly contact IT Dept if it was not you.

      <br><br>

     

       <table style="width: 100%;">

        <tr>

            <td style="font-weight: bold; width: 61px;" class="modal-sm">Username:</td>

            <td style="color: #FF0000">"""+username+"""</td>

        </tr>

    </table>

    </p>

  </body>

</html>

"""


msg['From'] = mail_From

msg['To'] = ", ".join(mail_To)

msg['Subject'] = subject

msg.attach(MIMEText(html, 'html'))

text=msg.as_string()

s = smtplib.SMTP(SMTP_Server)

s.sendmail(mail_From,mail_To, text)

s.quit()

print("Mail sent successfully.")



