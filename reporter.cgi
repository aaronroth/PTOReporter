#!/usr/bin/env python

import cgi
import smtplib
import cgitb
cgitb.enable()

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
receiverEmail = ''

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

# Build the message.
