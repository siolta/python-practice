import os
import requests
import urllib.parse
import argparse


# check this isn't none before making calls to the api
API_KEY = os.getenv("OW_API_KEY")
BASE_URL = "http://api.openweathermap.org/"


def get_location_args():
    # add args for:
    # zip code without input
    # country code
    # unit to return temps in

    parser = argparse.ArgumentParser()

    parser.add_argument("zip", help="zip/postal code to request weather for", nargs="?")

    return parser.parse_args()


def get_location_via_input():
    while True:
        location = input("input location (zipcode): ")
        if len(location) > 0:
            break
    return location


def validate_location(location: str):
    pass


def get_coordinates(location: str):
    geo_url = f"geo/1.0/zip?zip={location},US&appid={API_KEY}"
    try:
        r = requests.get(BASE_URL + geo_url)
        r.raise_for_status()
        location_data = r.json()
    except requests.HTTPError as e:
        SystemExit(e)

    return location_data


def request_weather_data(lat, lon):
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "unit": "metric"}
    data_url = "data/2.5/weather?" + urllib.parse.urlencode(params)
    try:
        r = requests.get(BASE_URL + data_url)
        r.raise_for_status()
        weather_data = r.json()
    except requests.HTTPError as e:
        SystemExit(e)

    return weather_data


def display_forecast(forecast):
    print(f"The weather is {forecast['weather'][0]['description']}")


def main():
    args = get_location_args()
    if not args.zip:
        args.zip = get_location_via_input()
    location_data = get_coordinates(args.zip)
    # print(location_data)
    forecast = request_weather_data(location_data["lat"], location_data["lon"])
    # print(forecast)
    display_forecast(forecast)


if __name__ == "__main__":
    main()
