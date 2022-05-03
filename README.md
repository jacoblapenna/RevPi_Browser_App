# RevPi_Browser_App
Basic browser app to show data from first channel of AIO connected to a Revolution Pi.

## Install
1. SSH to the Revolution Pi.
2. Install Redis on the Revolution Pi: https://redis.io/docs/getting-started/installation/install-redis-on-linux/
3. Clone this repo to the Revolution Pi. AIO channel 1 is setup with default name `InputValue_1` in PiCtory.
4. From within project directory on Revolution Pi:<br/>
    `$ python -m venv .env`<br/>
    `$ source .env/bin/activate`<br/>
    `$ pip install -r requirements.text`<br/>

## Run
1. Check that redis-server is running: `$ systemctl status redis-server.service`

    a. If the redis service is not running, use `$ sudo systemctl restart redis-server.service` or, simply `$ redis-server`.
2. `$ python app.py`

    a. Program automatically obtains IP of device it's running on (printed in debug message).
3. In a browser, navigate to the Revolution Pi's IP (stated in the terminal from step 2) via port 8080.

## Issues with revpimodio2
