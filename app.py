import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os
from agents import city_guide, trip_expert, planning_expert
from tasks import guide_task, location_task, planner_task
from crewai import Crew, Process
import streamlit as st

st.title("🌍 WanderAI - Your trip itinerary planner")

st.markdown("""
**Plan your next trip with us!**  
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
- Best places to visit 🎡
- Accommodation & budget planning 💰
- Local food recommendations 🍕
- Transportation & visa details 🚆
""")

source = st.text_input("Source City")
destination = st.text_input("Destination City")
date_from = st.date_input("Departure Date")
date_to = st.date_input("Return Date")
interests = st.multiselect(
    "Select Your Interests",
    [
        "Museums",
        "Monuments",
        "City Life",
        "Local Markets",
        "Malls",
        "Nature",
        "Mountains",
        "Beaches",
        "Parks & Gardens",
        "Food",
        "Nightlife",
        "Adventure"
    ]
)

if st.button("Generate my itinerary"):
    if not source or not destination or not date_from or not date_to or not interests:
        st.error("⚠️ Please fill in all fields so that we can generate the best itinerary for you.")
    else:
        st.write("⏳ Your personalized travel itinerary is being prepared... Please wait.")
        try:
            loc_task = location_task(trip_expert, source, destination, date_from, date_to)
            gde_task = guide_task(city_guide, destination, interests, date_from, date_to)
            plan_task = planner_task([loc_task, gde_task], planning_expert, destination, interests, date_from, date_to)
            my_crew = Crew(
                agents=[trip_expert, city_guide, planning_expert],
                tasks=[loc_task, gde_task, plan_task],
                process=Process.sequential,
                full_output=True,
                verbose=True
            )
            result = my_crew.kickoff()
            if not result or "failed" in str(result).lower():
                st.error("Sorry, we couldn't generate your itinerary. Please check your inputs and try again.")
            else:
                st.subheader("Here's your travel itinerary: ")
                st.markdown(result)
                st.download_button(
                    label="📥 Download Travel Plan",
                    data=str(result),
                    file_name=f"Travel_Plan_{destination}.txt",
                    mime="text/plain"
                )

                # Download .md files as .txt
                md_files = [
                    ("guide_report.md", "Guide_Report.txt"),
                    ("city_report.md", "City_Report.txt"),
                    ("travel_plan.md", "Travel_Plan.txt")
                ]
                for md_file, txt_file in md_files:
                    if os.path.exists(md_file):
                        with open(md_file, "r", encoding="utf-8") as f:
                            content = f.read()
                        st.download_button(
                            label=f"📥 Download {txt_file}",
                            data=content,
                            file_name=txt_file,
                            mime="text/plain"
                        )
        except Exception as e:
            st.error(f"An error occurred while generating your itinerary: {e}")

