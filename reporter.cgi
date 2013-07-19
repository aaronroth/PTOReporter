#!/usr/bin/env python

import cgi
import os

csEmail = 'cs@example.com'
financeEmail = 'finance@example.com'
hrEmail = 'hr@example.com'
managementEmail = 'management@example.com'
programmingEmail = 'programming@example.com'
sysadminEmail = 'sysadmin@example.com'

print 'Content-type: text/html'
print

# Get form values.
form = cgi.FieldStorage()
typeOfPTO = form.getvalue('type', 'no PTO type entered')
fromDate = form.getvalue('from', 'no from date entered')
toDate = form.getvalue('to', 'no to entered')
hoursRequested = form.getvalue('hours', 'no hours entered')
deptName = form.getvalue('dept', 'no department entered')
senderEmail = form.getvalue('sender', 'no sender address entered')
senderName = form.getvalue('name', 'no sender name entered')

# Determine which department manager is emailed.
if deptName == 'cs':
	receiverEmail = csEmail
elif deptName == 'finance':
	receiverEmail = financeEmail
elif deptName == 'management':
	receiverEmail = managementEmail
elif deptName == 'programming':
	receiverEmail = programmingEmail
elif deptName == 'sysadmin':
	receiverEmail = sysadminEmail
else:
	receiverEmail = 'error'

# Create email recipient list.
recipientEmails = [receiverEmail, hrEmail]

# Build the message.
if typeOfPTO == 'future':
    futurePTO = ' X request approval for the following PTO day(s).'
    pastPTO = '__ report the following unanticipated/unapproved PTO day(s).'
else:
    futurePTO = '__ request approval for the following PTO day(s).'
    pastPTO = ' X report the following unanticipated/unapproved PTO day(s).'

emailSubject = 'PTO - ' + senderName
messageText = ('I would like to:\n\n%s\n\n%s\n\nPTO Dates(s) Requested/To Report:\n\n%s - %s\n\nTotal PTO Hours Requested/Reported:\n\n%s'
                % (futurePTO, pastPTO, fromDate, toDate, hoursRequested))

fullMessage = ('From: %s\r\nTo: %s\r\nCc: %s\r\nSubject: %s\r\n\r\n%s'
               % (senderEmail, receiverEmail, hrEmail, emailSubject, messageText))

# Send email via UNIX sendmail.
sendmailLocation = '/usr/bin/sendmail'
pipe = os.popen('%s -t -i' % sendmailLocation, 'w')
pipe.write(fullMessage)
status = pipe.close()

if status:
	print 'sendmail exit status', status