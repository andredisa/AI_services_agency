## --- FILE: agents/product_manager.py
from agency_swarm import Agent

def get_pm_agent(api_headers):
    return Agent(
        name="Product Manager",
        description="Experienced PM focused on product delivery and roadmap.",
        instructions="""
        Review project analysis.
        Define roadmap, MVP scope, and user journeys.
        Coordinate with CEO, CTO, and Developer.
        """,
        api_headers=api_headers,
        temperature=0.4,
        max_prompt_tokens=25000
    )

