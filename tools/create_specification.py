## --- FILE: tools/create_specification.py
from agency_swarm import BaseTool
from pydantic import Field
from typing import Literal

class CreateTechnicalSpecification(BaseTool):
    architecture_type: Literal["monolithic", "microservices", "serverless", "hybrid"] = Field(...)
    core_technologies: str = Field(...)
    scalability_requirements: Literal["high", "medium", "low"] = Field(...)

    class ToolConfig:
        name = "create_technical_spec"
        description = "Creates technical specifications based on project analysis"
        one_call_at_a_time = True

    def run(self) -> str:
        project_analysis = self._shared_state.get("project_analysis")
        if project_analysis is None:
            raise ValueError("Analyze project requirements first.")

        tech_stack = [tech.strip() for tech in self.core_technologies.split(",")]

        spec = {
            "project_name": project_analysis["name"],
            "architecture": self.architecture_type,
            "technologies": tech_stack,
            "scalability": self.scalability_requirements,
            "security": "OAuth2, HTTPS, JWT",
            "infrastructure": "Docker, Kubernetes, AWS",
            "documentation": "OpenAPI spec, ReadTheDocs",
        }
        self._shared_state.set("technical_specification", spec)
        return f"Technical specification for '{project_analysis['name']}' created successfully."

