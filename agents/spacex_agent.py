
import requests

class SpaceXAgent:
    def run(self):
        url = "https://api.spacexdata.com/v4/launches/next"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "Failed to fetch launch data"}

        data = response.json()
        launch_site = data.get("launchpad", "Unknown")
        launch_name = data.get("name", "Unnamed Launch")
        launch_time = data.get("date_utc", "Unknown")

        # Note: You can enrich location with another API if needed
        return {
            "launch_name": launch_name,
            "launch_time": launch_time,
            "launch_site_id": launch_site
        }
