## --- FILE: agents/client_manager.py
from agency_swarm import Agent

def get_client_agent(api_headers):
    return Agent(
        name="Client Success Manager",
        description="Ensures client satisfaction and go-to-market.",
        instructions="""
        Review project goals and audience.
        Provide GTM strategy, launch plan, and onboarding recommendations.
        Coordinate with PM.
        """,
        api_headers=api_headers,
        temperature=0.6,
        max_prompt_tokens=25000
    )

