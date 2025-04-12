import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATA = "/home/mike32/data.txt"
RESPALDO = "/home/mike32/respaldo.txt"


def sendToEmail(path):

	server = "smtp.gmail.com"
	port = 587
	senderMail = "jeitestcron@gmail.com"
	pwd = "nsho ggng rdpg mpsq"

	message = MIMEMultipart()
	message["From"] = senderMail
	message["To"] = "miguelmatute2004@gmail.com"
	message["Subject"] = "Respaldo exitoso"

	messageBody = f"El respaldo de {DATA} se hizo exitosamente"

	message.attach(MIMEText(messageBody, "plain"))

	smtpObj = None

	try:
		smtpObj = smtplib.SMTP(server, port)
		smtpObj.starttls()

		smtpObj.login(senderMail, pwd)

		smtpObj.sendmail(senderMail, "miguelmatute2004@gmail.com", message.as_string())
		print("Coreo enviado exitosamente")
	except Exception as e:
		raise Exception(f"Error al enviar correo: {e}")
	


def main():
	try:
		shutil.copyfile(DATA, RESPALDO)
		sendToEmail(RESPALDO)
	except Exception as e:
		raise Exception(f"No se pudo crear el respaldo:{e}")


if __name__ == '__main__':
	main()


