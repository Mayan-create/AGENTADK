
import os
from agents.planner_agent import PlannerAgent
from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.delay_analysis_agent import DelayAnalysisAgent

def run_system(user_goal):
    planner = PlannerAgent()
    plan = planner.create_plan(user_goal)

    context = {}
    for step in plan:
        agent_name = step['agent']
        input_data = context.get(step['input_from'], {})

        print(f"\n🔹 Running Agent: {agent_name} (Step: {step['name']})")

        if agent_name == 'spacex':
            agent = SpaceXAgent()
            result = agent.run()
        elif agent_name == 'weather':
            agent = WeatherAgent()
            result = agent.run(input_data)
        elif agent_name == 'delay':
            agent = DelayAnalysisAgent()
            result = agent.run(input_data)
        else:
            raise Exception(f"❌ Unknown agent: {agent_name}")

        print(f"✅ Result from {agent_name}:\n{result}")
        context[step['name']] = result

    return context[plan[-1]['name']]

if __name__ == "__main__":
    goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."
    print("⚙️ Starting system for goal:\n", goal)

    final_output = run_system(goal)

    print("\n🏁 ✅ Final Output:")
    print(final_output)
