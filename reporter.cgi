#!/usr/bin/env python

import cgi
import smtplib
import cgitb
cgitb.enable()

print 'Content-type: text/html'
print

form = cgi.FieldStorage()
typeOfPTO = form.getvalue('type', 'no PTO type entered')
fromDate = form.getvalue('from', 'no from date entered')
toDate = form.getvalue('to', 'no to entered')
hoursRequested = form.getvalue('hours', 'no hours entered')
deptName = form.getvalue('dept', 'no department entered')
senderEmail = form.getvalue('sender', 'no sender address entered')