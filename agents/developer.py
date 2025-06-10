## --- FILE: agents/developer.py
from agency_swarm import Agent

def get_developer_agent(api_headers):
    return Agent(
        name="Lead Developer",
        description="Senior full-stack developer.",
        instructions="""
        Based on specification, define module-level plan and provide estimates.
        Suggest tools, frameworks, and CI/CD pipelines.
        Collaborate with CTO and PM.
        """,
        api_headers=api_headers,
        temperature=0.3,
        max_prompt_tokens=25000
    )

