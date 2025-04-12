import psutil
import datetime
import matplotlib.pyplot as plt
import re

PATH = "/home/mike32/usoRecursos.txt"

def graficar():

	timeL = []
	cpuL = []
	memL = []
	diskL = []

	try:

		pattern = r'\[(.*?)\] CPU: ([\d.]+)%, Memoria: ([\d.]+)%, Disco: ([\d.]+)%'
		with open(PATH, "r") as f:
			for line in f:
				match = re.match(pattern, line.strip())
				if match:
					timestamp = match.group(1)
					cpu = match.group(2)
					mem = match.group(3)
					disk = match.group(4)

					timeL.append(datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
					cpuL.append(cpu)
					memL.append(mem)
					diskL.append(disk)

		print(timeL)
		print(cpuL)
		print(memL)
		print(diskL)

		plt.figure(figsize=(12,6))
		plt.plot(timeL, cpuL, label="CPU %", marker="o")
		plt.plot(timeL, memL, label="Memoria %", marker="o")
		plt.plot(timeL, diskL, label="Disco %", marker="o")

		plt.title("Uso de recursos")
		plt.xlabel("Tiempo")
		plt.ylabel("Uso %")
		plt.legend()
		plt.grid(True)
		plt.xticks(rotation=45)
		plt.tight_layout()
		plt.savefig("/home/mike32/graficoMonitorRecursos.png")
	except Exception as e:
		raise Exception(f"Error al graficar: {e}")

	print("grafico creado correctamente")
	#plt.show()

def monitorear():

	try:
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		cpu = psutil.cpu_percent(interval=1)
		memory = psutil.virtual_memory()
		mem_uso = memory.percent

		disk_info = psutil.disk_usage('/')
		disk_uso = disk_info.percent

		log = (f"[{timestamp}] "
			f"CPU: {cpu}%, "
			f"Memoria: {mem_uso}%, "
			f"Disco: {disk_uso}%\n")

		with open(PATH, "a") as f:
			f.write(log)

		graficar()

	except Exception as e:
		raise Exception(f"Error al monitorear los recursos: {e}")


def main():
	monitorear()

if __name__ == '__main__':
	main()