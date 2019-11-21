
class BPM280:


    def __init__(self):
        pass
    
    def i2c(self):
        import board
        import busio 
        import adafruit_bmp280
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
        
    def SPI(self):
        import board
        import busio
        import digitalio

    def temperature(self):
        
        i2c = busio.I2C(board.SCL, board.SDA)
        bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

        bmp280.sea_level_pressure = 1013.25
        
        
        
        
