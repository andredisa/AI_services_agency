from agency_swarm import BaseTool
from pydantic import Field
from typing import Literal

class AnalyzeProjectRequirements(BaseTool):
    project_name: str = Field(..., description="Name of the project")
    project_description: str = Field(..., description="Project description and goals")
    project_type: Literal["Web Application", "Mobile App", "API Development", 
                          "Data Analytics", "AI/ML Solution", "Other"] = Field(..., description="Type of project")
    budget_range: Literal["$10k-$25k", "$25k-$50k", "$50k-$100k", "$100k+"] = Field(..., description="Budget range")

    class ToolConfig:
        name = "analyze_project"
        description = "Analyzes project requirements and feasibility"
        one_call_at_a_time = True

    def run(self) -> str:
        if self._shared_state.get("project_analysis") is not None:
            raise ValueError("Project analysis already exists.")
        analysis = {
            "name": self.project_name,
            "type": self.project_type,
            "description": self.project_description,
            "budget": self.budget_range,
            "complexity": "high" if self.project_type in ["AI/ML Solution", "Data Analytics"] else "medium",
            "timeline": "6 months",
            "budget_feasibility": "within range",
            "requirements": [
                "Scalable architecture",
                "Security",
                "API integration",
                "Cross-team collaboration",
                "Robust documentation"
            ]
        }
        self._shared_state.set("project_analysis", analysis)
        return f"Project analysis for '{self.project_name}' completed. Ready for technical specification."

