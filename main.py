import esp32, time
print('Corriendo main.py')
while True:
	hall = esp32.hall_sensor()     # read the internal hall sensor
	temp = esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
	print('Hall Sensor: ', hall)
	print('Temperatura: ', temp)
	print('<-+-+-+-+-+-+-+-+-+-+->')
	time.sleep(1)
