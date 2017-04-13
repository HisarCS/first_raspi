import RPi.GPIO as GPIO
#ultrasonic sensors
#rear (serial)
rear_tx = 0;

#left e/t
left_echo = 0;
left_trig = 0;

#right e/t
right_echo = 0;
right_trig = 0;

#front e/t
front_echo = 0;
front_trig = 0;

#digital IR sensors
front_ir_1 = 0;
front_ir_2 = 0;

for i in [left_echo, right_echo, front_echo]:
    GPIO.setup(i, GPIO.IN)

for i in [left_trig, right_trig, front_trig]:
    GPIO.setup(i, GPIO.OUT);
