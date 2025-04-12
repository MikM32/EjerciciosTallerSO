import os
import shutil
import smtplib
import subprocess
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATA = "/home/mike32/data.txt"
RESPALDO = "/home/mike32/repoRespaldo/respaldo.txt"
GIT_PATH = "/usr/bin/git"


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
		print("Correo enviado exitosamente")
	except Exception as e:
		raise Exception(f"Error al enviar correo: {e}")
	


def main():
	a = None
	fecha_respaldo = datetime.datetime.now().strftime("%Y-%m-%d")
	try:
		shutil.copyfile(DATA, RESPALDO)
		os.system("chmod 777 /home/mike32/repoRespaldo")
		os.chdir("/home/mike32/repoRespaldo")
		os.system(f"cd /home/mike32/repoRespaldo && pwd && git init /home/mike32/repoRespaldo && git config --global --add safe.directory /home/mike32/repoRespaldo && git pull origin master && git add {RESPALDO} && git commit -m \"Respaldo fecha: {fecha_respaldo}\" && git push")
		#sendToEmail(RESPALDO)
	except Exception as e:
		
		raise Exception(f"No se pudo crear el respaldo:{e}")


if __name__ == '__main__':
	main()

