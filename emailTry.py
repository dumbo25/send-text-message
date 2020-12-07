#! /usr/bin/env python
import smtplib

# DO NOT PUBLISH
# 
# Change the items enclosed by angle brackets and delete the angle brackets
gmail_password = '♣your gmail password♣'
gmail_address = '♣your gmail address♣'
ID = '<ID-from-genID.py♣'	# This is the ID gmail fowards to your smart phone
#
# CHANGE THE ITEMS ABOVE - DO NOT PUBLISH

# the length of subject should be less than 40 characters
p = " Project: "
m = "Garage door open"
subject = ID + p + m
message = 'Subject: %s' % (subject)

# 587 uses TLS
# 465 uses SSL - not supported see edits to /etc/ssmtp/ssmtp.conf
mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(gmail_address, gmail_password)
mail.sendmail("cell", gmail_address, message)
mail.close()

print 'text message sent'
