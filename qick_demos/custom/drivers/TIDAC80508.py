import spidev

class TIDAC80508:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(1, 0)
        self.spi.mode = 0b01
        self.spi.max_speed_hz = 500000
        to_send = [0x04, 0x00, 0xff] # All gains set x2
        self.spi.xfer(to_send)
        to_send = [0x08, 0x80, 0x00] # Initialize DAC0
        self.spi.xfer(to_send)
        to_send = [0x09, 0x80, 0x00] # Initialize DAC1
        self.spi.xfer(to_send)
        to_send = [0x0a, 0x80, 0x00] # Initialize DAC2
        self.spi.xfer(to_send)
        to_send = [0x0b, 0x80, 0x00] # Initialize DAC3
        self.spi.xfer(to_send)        
        to_send = [0x0c, 0x80, 0x00] # Initialize DAC4
        self.spi.xfer(to_send)
        to_send = [0x0d, 0x80, 0x00] # Initialize DAC5
        self.spi.xfer(to_send)
        to_send = [0x0e, 0x80, 0x00] # Initialize DAC6
        self.spi.xfer(to_send)
        to_send = [0x0f, 0x80, 0x00] # Initialize DAC7
        self.spi.xfer(to_send)

    def set_bias(self, dac, bias_value: float):
        #if abs(bias_value) > 1.:
        #   raise ValueError("Bias values should be between -1 and 1")
        if dac==0:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x08
        elif dac==1:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x09
        elif dac==2:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x0a
        elif dac==3:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x0b
        elif dac==4:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x0c
        elif dac==5:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x0d
        elif dac==6:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x0e
        elif dac==7:
            register_value = int(bias_value * (0xffff - 0x8000) / 2.5000) + 0x8000
            dest = 0x0f          
        high_byte = (register_value & 0xff00) >> 8
        low_byte  = (register_value & 0x00ff)
        to_send = [dest, high_byte, low_byte]
        self.spi.xfer(to_send)