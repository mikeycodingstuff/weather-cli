# weather-cli

A weather CLI app built in python following this tutorial: https://realpython.com/build-a-python-weather-app-cli/

## Setup

1. Install python
2. Clone this repo: `git@github.com:mikeycodingstuff/weather-cli.git`
3. Sign up for an account at https://openweathermap.org/api to get your API key
4. Inside the directory, create a `secrets.ini` file and add the following:

    ```
    [openweather]
    api_key=<YOUR-OPENWEATHER-API-KEY>
    ```
5. To be able to run the CLI from anywhere, add the script to your PATH
6. You could then add an alias e.g. `alias weather=weather.py` to your shell profile so that you can run the script with:

    ```
    weather <cityname>
    ```
