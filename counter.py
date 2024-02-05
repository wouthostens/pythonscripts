"""
This script is used to count the number of people entering and exiting a space using sensors and buttons.
The count is displayed on an OLED screen and sent to an InfluxDB database.
"""
import RPi.GPIO as GPIO
from gpiozero import Button
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import warnings
warnings.filterwarnings("ignore")
import board
import busio
import adafruit_ssd1306
from PIL import Image

# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED display object
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# You can generate a Token from the "Tokens Tab" in the UI
token = "VN-NCfNZ-nUd3S_Mo60lzns2jAfO2_EQifpEbNqEDQ_TPqtOOkG9E21tQ04QlDL18w7VOYPmTvbHK2iiotfDrg=="
org = "vives"
bucket = "peoplecounter"

# Initialize the last sensor triggered
last_sensor_triggered = None

# create an instance of the InfluxDB client
client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, verify_ssl=False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number for the button and the sensors
button_pin = 10
sensorIn_pin = 23
sensorOut_pin = 25

# Set the GPIO pin as input with a pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensorIn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensorOut_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize the sensor for in and out
sensorIn_pressed = False
sensorIn = Button(sensorIn_pin)
sensorOut_pressed = False
sensorOut = Button(sensorOut_pin)

# Initialize button state
button_pressed = False
global counter
counter = 0 # Global variable

# Clear the display
def clear_display():
  oled.fill(0)
  oled.show()

#Display counter on the screen
def display_counter():
  global counter
  clear_display()
  oled.text(str(counter), 0, 0, 1)
  oled.show()

# This function is responsible for displaying an image on the OLED screen.
# The image displayed corresponds to the current count of people inside.
def display_image():
  # Load the images from the file system, convert them to black and white, and resize them to fit the OLED screen.
  image_leeg = Image.open("/home/wouthostens/Desktop/images/leeg.png").convert('1')
  image_niet_druk = Image.open("/home/wouthostens/Desktop/images/nietDruk.png").convert('1')
  image_iets_drukker= Image.open("/home/wouthostens/Desktop/images/ietsDrukker.png").convert('1')
  image_super_druk = Image.open("/home/wouthostens/Desktop/images/druk.png").convert('1')
  image_volzet = Image.open("/home/wouthostens/Desktop/images/volzet.png").convert('1')

  # Access the global counter variable
  global counter
  # Clear the current display
  clear_display()
  # Depending on the value of the counter, display the corresponding image
  if counter > 10:
    # If there are more than 10 people, display the 'full' image
    oled.image(image_volzet)
  elif counter > 7:
    # If there are more than 7 people, display the 'very busy' image
    oled.image(image_super_druk)
  elif counter > 4:
    # If there are more than 4 people, display the 'somewhat busy' image
    oled.image(image_iets_drukker)
  elif counter > 1:
    # If there are more than 1 person, display the 'not busy' image
    oled.image(image_niet_druk)
  else:
    # If there are no people, display the 'empty' image
    oled.image(image_leeg)
  # Update the OLED display with the new image
  oled.show()

#Display message on the screen (max 21 characters per row)
def display_message(message):
  clear_display()
  max_chars_per_row = 21
  num_rows = len(message) // max_chars_per_row + 1
  for i in range(num_rows):
    start_index = i * max_chars_per_row
    end_index = start_index + max_chars_per_row
    row_message = message[start_index:end_index]
    oled.text(row_message, 0, i * 10, 1)
  oled.show() 

#define a function to send the counter to the database
def send_counter():
  global counter
  write_api = client.write_api(write_options=SYNCHRONOUS)
  point = Point("my_measurement").field("value",counter)
  write_api.write(bucket, org, point)
  display_image()

#define a function to get the counter from the database
def get_counter():
  global counter
  query_api = client.query_api()
  query = f'from(bucket: "{bucket}") |> range(start: -1h) |> filter(fn: (r) => r["_measurement"] == "my_measurement") |> last()'
  result = query_api.query(query, org=org)
  for table in result:
    for record in table.records:
      counter = record.get_value() # Get the counter from the database

# Define a function to increment the counter when the sensor is triggered
def increment_counter():
  global counter
  get_counter()
  if counter < 15:
    counter += 1
  else:
    display_message("Max capacity reached!")
  send_counter()

#define a function to decrement the counter when the sensor is triggered
def decrement_counter():
  global counter
  get_counter()
  if counter > 0:
    counter -= 1
    send_counter()
  else:
    display_message("Counter cannot go below 0")

#define a function to reset the counter when the button is pressed
def reset_counter():
  global counter
  counter = 0
  send_counter()
  display_message("Counter reset!")

# Main loop
while True:
  # Check if the button is pressed
  if GPIO.input(button_pin) == GPIO.LOW and not button_pressed:
    button_pressed = True
    reset_counter()
    print("Button pressed!")
  elif GPIO.input(button_pin) == GPIO.HIGH and button_pressed:
    button_pressed = False
  # Check if the sensors are triggered (out)
  if sensorIn.is_pressed and not sensorIn_pressed:
    sensorIn_pressed = True
    if last_sensor_triggered == 'sensorOut':
      decrement_counter()
      last_sensor_triggered = None
    else:
      last_sensor_triggered = 'sensorIn'
  elif not sensorIn.is_pressed and sensorIn_pressed:
    sensorIn_pressed = False
  # Check if the sensors are triggered (in)
  if sensorOut.is_pressed and not sensorOut_pressed:
    sensorOut_pressed = True
    if last_sensor_triggered == 'sensorIn':
      increment_counter()
      last_sensor_triggered = None
    else:
      last_sensor_triggered = 'sensorOut'
  elif not sensorOut.is_pressed and sensorOut_pressed:
    sensorOut_pressed = False
  # Delay for a short period of time to avoid excessive CPU usage
  time.sleep(0.2)

# Clean up the GPIO pins
GPIO.cleanup()
