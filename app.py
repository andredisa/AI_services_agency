## --- FILE: app.py
import streamlit as st
from agency_swarm import Agency, set_openai_key

from core.session import init_session_state
from agents.ceo import get_ceo_agent
from agents.cto import get_cto_agent
from agents.product_manager import get_pm_agent
from agents.developer import get_developer_agent
from agents.client_manager import get_client_agent

def main():
    st.set_page_config(page_title="AI Services Agency", layout="wide")
    init_session_state()
    st.title("🚀 AI Services Agency")

    with st.sidebar:
        st.header("🔑 API Configuration")
        key = st.text_input("OpenAI API Key", type="password")
        if key:
            st.session_state.api_key = key
            set_openai_key(key)
            st.success("API Key set!")
        else:
            st.warning("Please enter your OpenAI API key.")
            return

    st.subheader("Project Details")
    with st.form("project_form"):
        project_name = st.text_input("Project Name")
        project_description = st.text_area("Project Description")
        project_type = st.selectbox("Project Type", ["Web Application", "Mobile App", "API Development", "Data Analytics", "AI/ML Solution", "Other"])
        timeline = st.selectbox("Expected Timeline", ["1-2 months", "3-4 months", "5-6 months", "6+ months"])
        budget_range = st.selectbox("Budget Range", ["$10k-$25k", "$25k-$50k", "$50k-$100k", "$100k+"])
        priority = st.selectbox("Project Priority", ["High", "Medium", "Low"])
        tech_requirements = st.text_area("Technical Requirements (optional)")
        special_considerations = st.text_area("Special Considerations (optional)")

        submitted = st.form_submit_button("Analyze Project")

        if submitted and project_name and project_description:
            api_headers = {"Authorization": f"Bearer {st.session_state.api_key}"}

            ceo = get_ceo_agent(api_headers)
            cto = get_cto_agent(api_headers)
            pm = get_pm_agent(api_headers)
            dev = get_developer_agent(api_headers)
            client = get_client_agent(api_headers)

            agency = Agency(
                [ceo, cto, pm, dev, client,
                 [ceo, cto], [ceo, pm], [ceo, dev], [ceo, client],
                 [cto, dev], [pm, dev], [pm, client]],
                async_mode='threading',
                shared_files='shared_files'
            )

            project_info = {
                "name": project_name,
                "description": project_description,
                "type": project_type,
                "timeline": timeline,
                "budget": budget_range,
                "priority": priority,
                "technical_requirements": tech_requirements,
                "special_considerations": special_considerations
            }

            st.session_state.messages.append({"role": "user", "content": str(project_info)})

            with st.spinner("AI Services Agency is analyzing your project..."):
                ceo_response = agency.get_completion(
                    message=f"Analyze this project: {project_info}",
                    recipient_agent=ceo
                )

                cto_response = agency.get_completion(
                    message="Create technical specification based on project analysis.",
                    recipient_agent=cto
                )

                pm_response = agency.get_completion(
                    message=f"Analyze project management aspects: {project_info}",
                    recipient_agent=pm
                )

                dev_response = agency.get_completion(
                    message=f"Technical implementation plan: {project_info}",
                    recipient_agent=dev
                )

                client_response = agency.get_completion(
                    message=f"Client success strategy: {project_info}",
                    recipient_agent=client
                )

                tabs = st.tabs([
                    "CEO's Project Analysis",
                    "CTO's Technical Specification",
                    "Product Manager's Plan",
                    "Developer's Implementation",
                    "Client Success Strategy"
                ])

                with tabs[0]:
                    st.markdown(ceo_response)
                with tabs[1]:
                    st.markdown(cto_response)
                with tabs[2]:
                    st.markdown(pm_response)
                with tabs[3]:
                    st.markdown(dev_response)
                with tabs[4]:
                    st.markdown(client_response)

if __name__ == "__main__":
    main()
