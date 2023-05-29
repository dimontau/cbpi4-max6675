import time
import RPi.GPIO as GPIO
import logging


class max6675(object):
    
    def __init__(self, csPin, misoPin, clkPin):
        self.csPin = csPin
        self.misoPin = misoPin
        self.clkPin = clkPin

        self.setupGPIO()

    def __del__(self):
        logging.info("Delete max6675 object")
    
    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.csPin, GPIO.OUT)
        GPIO.setup(self.misoPin, GPIO.IN)
        GPIO.setup(self.clkPin, GPIO.OUT)
    
    def readTemp(self):
        # Установка CS пина в низкий уровень для начала передачи данных
        GPIO.output(self.csPin, GPIO.LOW)
        time.sleep(0.001)

        # Чтение 16 бит данных
        data = 0
        for i in range(15, -1, -1):
            GPIO.output(self.clkPin, GPIO.HIGH)
            time.sleep(0.001)
            bit = GPIO.input(self.misoPin)
            if bit:
                data |= (1 << i)
            GPIO.output(self.clkPin, GPIO.LOW)
            time.sleep(0.001)

        # Признак ошибки
        if data & 0x4:
            return -1

        # Извлечение температуры из 12 бит данных
        temp_C = (data >> 3) / 4.0
        
        # Установка CS пина в высокий уровень для завершения передачи данных
        GPIO.output(self.csPin, GPIO.HIGH)
                            
        return temp_C


class FaultError(Exception):
    pass


if __name__ == "__main__":
    csPin = 8
    misoPin = 9
    clkPin = 11
    max = max6675(csPin, misoPin, clkPin)
    GPIO.cleanup()
