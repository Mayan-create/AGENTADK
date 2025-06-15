
class DelayAnalysisAgent:
    def run(self, input_data):
        description = input_data.get("description", "").lower()

        if any(word in description for word in ["storm", "rain", "wind", "thunder"]):
            delay_risk = "High chance of delay due to weather conditions."
        elif any(word in description for word in ["cloud", "overcast"]):
            delay_risk = "Moderate risk of delay due to clouds."
        else:
            delay_risk = "Weather conditions look clear. Launch is likely on time."

        return {
            "weather_summary": input_data,
            "delay_assessment": delay_risk
        }