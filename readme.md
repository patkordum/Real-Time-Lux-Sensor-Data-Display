# Real-Time Lux Sensor Data Display

This Flask application provides a real-time display of lux sensor data retrieved from a TSL2591 sensor connected to a Raspberry Pi. It includes a web interface that dynamically updates the lux value and background color based on the ambient light intensity.

## Features

- Real-time display of lux sensor data.
- Dynamically updates the background color based on the lux value.
- Simple and intuitive web interface.

## Requirements

- Raspberry Pi with GPIO pins.
- Python 3 installed.
- Flask and adafruit-circuitpython-tsl2591 Python libraries.

## Installation

1. Clone this repository to your Raspberry Pi:

git clone https://github.com/your_username/lux_sensor_display.git

2. Install the required Python libraries:

pip install flask adafruit-circuitpython-tsl2591

3. Run the Flask application:

python app.py

4. Open a web browser and navigate to http://<your_pi_ip_address>:5000 to view the real-time lux sensor data display.

## Directory Structure

lux_sensor_display/
├── app.py         # Flask application file
├── templates/     # Directory for HTML templates
│   └── index.html # HTML template for lux sensor data display
└── README.md      # Project documentation


License
This project is licensed under the MIT License. 