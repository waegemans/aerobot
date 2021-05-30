# aerobot
Telegram Chatbot to monitor and controll aeroponics systems using a raspberry pi


## remote development
To test/develop this library without access to a Raspberry Pi use the mock GPIO pins:
```
GPIOZERO_PIN_FACTORY=mock python <...>
```