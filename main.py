import esp32, time, ssd1306
from machine import Pin, I2C

# using default address 0x3C
i2c = I2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 32, i2c)

print('Corriendo main.py')
while True:
	hall = esp32.hall_sensor()     # read the internal hall sensor
	temp = esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
	display.fill(0)
	display.text(f'SHall: {hall}', 0, 0)
	display.text(f'Temp: {(temp-32.0)/1.8} C°', 0, 15) # F° to C°
	display.show()
	time.sleep(1)

