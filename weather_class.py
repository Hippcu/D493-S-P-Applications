import openmeteo_requests

class WeatherData:
    # Location and Date from user
    # date expected to be in (year-month-day) format
    def __init__(self, latitude, longitude, date: str): 
        self.latitude = latitude
        self.longitude = longitude
        self.date = date

        # Five year data to be collected from methods
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_seped = None

        self.avg_precip = None
        self.min_precip = None
        self.max_precip = None

        # -- End of C1 -- #

    # -- Start of C2 -- #
    # Method to fetch weather data from WeatherAPI (openmeteo)*
    def fetch_weather_data(self):
        openmeteo = openmeteo_requests.Client() 
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
             "latitude": self.latitude,
             "longitude": self.longitude,
             "start_date": self.date,
             "end_date": self.date,
             # Order matters --> returns responses in same order as declared here
             "daily": ["temperature_2m_mean", "temperature_2m_min", "temperature_2m_max",
                       "wind_speed_10m_max", "precipitation_sum"],
        }

        # Get response data for start-end dates returned as an array (should be same day for us)
        responses = openmeteo.weather_api(url=url, params=params)
        # The day we need is the first one (the only one for us)
        response = responses[0]
        print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation: {response.Elevation()} m asl")
        print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

        daily = response.Daily()
        # daily.Variables holds all of the goodies 
