# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Initialize GPIO pins for servos (adjust pin numbers as needed)
servo1_pin = 17
servo2_pin = 27
servo3_pin = 22

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)
GPIO.setup(servo3_pin, GPIO.OUT)

# Define servo control functions (you may need to adjust angles)
def move_servo(servo_pin, angle):
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
    pwm.start(2.5)  # Initial position (adjust as needed)
    duty_cycle = angle / 18.0 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    pwm.stop()

# Tower of Hanoi solver
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        move_servo(servo1_pin, 90)  # Adjust servo angles
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        move_servo(servo1_pin, 90)  # Adjust servo angles
        tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage
num_disks = 3  # Adjust as needed
tower_of_hanoi(num_disks, "A", "C", "B")

# Clean up GPIO
GPIO.cleanup()
