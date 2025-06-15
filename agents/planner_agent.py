
class PlannerAgent:
    def create_plan(self, goal: str):
        """
        Based on the user goal, define agent execution plan.
        Each step must include:
          - name: identifier for context storage
          - agent: which agent to run
          - input_from: previous step name to depend on (if any)
        """
        return [
            {"name": "launch_info", "agent": "spacex", "input_from": None},
            {"name": "weather_info", "agent": "weather", "input_from": "launch_info"},
            {"name": "delay_summary", "agent": "delay", "input_from": "weather_info"},
        ]