import gpiozero

class Controller:
    def __init__(self, outputs : dict) -> None:
        self.outputs = {}
        for name,gpiopin in outputs.items():
            self.outputs[name] = gpiozero.DigitalOutputDevice(gpiopin,False)

    def set_schedule(self, name, on_time, off_time) -> None:
        if (name not in self.outputs):
            raise AttributeError(f"No Sensor called '{name}'!")
        else:
            self.outputs[name].blink(on_time,off_time,n=None,background=True)