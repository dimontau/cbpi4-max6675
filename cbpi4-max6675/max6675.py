import spidev
import time

# Установите соответствующие пины SPI на Raspberry Pi
SPI_CLK = 0  # Номер SPI-канала для клока
SPI_CS = 0   # Номер SPI-канала для CS
SPI_BUS = 0  # Номер шины SPI

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_CS)
spi.max_speed_hz = 1000000  # Установите максимальную скорость передачи в Hz

def read_temp(self):
    # Отправляем и принимаем данные по SPI
    raw_data = spi.xfer2([0x00, 0x00])
    
    # Обрабатываем принятые данные
    value = ((raw_data[0] << 8) + raw_data[1]) >> 3
    tempC = value * 0.25
    
    return tempC


class FaultError(Exception):
	pass

if __name__ == "__main__":

	tempC = max.readTemp()
	