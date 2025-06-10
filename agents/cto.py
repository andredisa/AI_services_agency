## --- FILE: agents/cto.py
from agency_swarm import Agent
from tools.create_specification import CreateTechnicalSpecification

def get_cto_agent(api_headers):
    return Agent(
        name="Technical Architect",
        description="Senior technical architect with deep expertise in system design.",
        instructions="""
        Wait for project analysis completion.
        Use CreateTechnicalSpecification to define architecture and implementation stack.
        """,
        tools=[CreateTechnicalSpecification],
        api_headers=api_headers,
        temperature=0.5,
        max_prompt_tokens=25000
    )

