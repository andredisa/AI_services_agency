## --- FILE: agents/ceo.py
from agency_swarm import Agent
from tools.analyze_project import AnalyzeProjectRequirements

def get_ceo_agent(api_headers):
    return Agent(
        name="Project Director",
        description="Experienced CEO for strategic project evaluation.",
        instructions="""
        Use AnalyzeProjectRequirements tool with the provided data.
        Wait for completion and provide strategic recommendations based on budget, goals, and market fit.
        """,
        tools=[AnalyzeProjectRequirements],
        api_headers=api_headers,
        temperature=0.7,
        max_prompt_tokens=25000
    )

