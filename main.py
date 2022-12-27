import esp32, time

hall = esp32.hall_sensor()     # read the internal hall sensor
temp = esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
#esp32.ULP()             # access to the Ultra-Low-Power Co-processor

while True:
	hall = esp32.hall_sensor()     # read the internal hall sensor
	temp = esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
	print(hall)
	print(temp)
	time.sleep(2)
