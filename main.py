import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from secret import email, pwd 

email_sender = email 
email_password = pwd 
subject = "Submit your assignment by today."


with open('email.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
		text=("Hello, I am your google classroomBot."+"\n"
		+line[1]+" you need to please submit your inspection report assignment by today(20 dec 2022)."+"\n"+
		"Created by Sujan Shrestha.")
		# print(text)

		send_email = line[0]
		msg = MIMEMultipart()
		msg['From'] = email_sender
		msg['To'] = send_email
		msg['Subject'] = subject
		msg.attach(MIMEText(text,"plain"))
		text = msg.as_string()

		server = smtplib.SMTP_SSL("smtp.gmail.com",465)
		server.login(email_sender,email_password)
		server.sendmail(email_sender,send_email,text)

		server.quit()