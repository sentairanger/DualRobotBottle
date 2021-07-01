from bottle import route, run, template, request
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import OutputDevice, AngularServo, LED, PWMOutputDevice

#Define the factories
factory = PiGPIOFactory(host='192.168.0.22')
factory2 = PiGPIOFactory(host='192.168.0.21')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

#Define the eyes
linus_eye = LED(16, pin_factory=factory)
torvalds_eye = LED(25, pin_factory=factory2)

# Define the servo
angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=factory)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=factory)

@route('/')
def index():
    return template('dual_bottle.html')

@route('/forward')
def direction_one():
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return template('dual_bottle.html')

# backwards
@route('/backward')
def direction_two():
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return template('dual_bottle.html')

#right
@route('/right')
def direction_three():
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return template('dual_bottle.html')

#left
@route('/left')
def direction_four():
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return template('dual_bottle.html')

@route('/stop')
def stop():
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return template('dual_bottle.html')

@route('/eyeon')
def eye_on():
    linus_eye.on()
    return template('dual_bottle.html')

@route('/eyeoff')
def eye_off():
    linus_eye.off()
    return template('dual_bottle.html')

# Forwards
@route('/up')
def north():
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return template('dual_bottle.html')

# backwards
@route('/down')
def south():
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return template('dual_bottle.html')

#right
@route('/east')
def east():
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return template('dual_bottle.html')

#left
@route('/west')
def west():
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return template('dual_bottle.html')

@route('/stop2')
def stop_two():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return template('dual_bottle.html')

@route('/torvaldson')
def torvalds_on():
    torvalds_eye.on()
    return template('dual_bottle.html')

@route('/torvaldsoff')
def torvalds_off():
    torvalds_eye.off()
    return template('dual_bottle.html')

@route('/angle', method='POST')
def angle():
    servo_angle = request.forms.get('servo1')
    servo_angle2 = request.forms.get('servo2')
    angular_servo.angle = int(servo_angle)
    angular_servo2.angle = int(servo_angle2)
    return template('dual_bottle.html')

@route('/pwm', method='POST')
def pwm():
    pwm_one = request.forms.get('pwm1')
    pwm_two = request.forms.get('pwm2')
    en_1.value = int(pwm_one) / 10
    en_2.value = int(pwm_two) / 10
    return template('dual_bottle.html')

run(host='0.0.0.0', port=8080, debug=True)
