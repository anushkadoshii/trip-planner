from agents import city_guide, trip_expert, planning_expert
from tasks import guide_task, location_task, planner_task
from crewai import Crew, Process
import streamlit as st

st.title("🌍 WanderAI - Your trip itinerary planner")

st.markdown("""
**Plan your next trip with us!**  
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
 Best places to visit 🎡   Accommodation & budget planning 💰
 Local food recommendations 🍕   Transportation & visa details 🚆
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
        loc_task = location_task(trip_expert, source, destination, date_from, date_to)
        gde_task = guide_task(city_guide, destination, interests, date_from, date_to)
        plan_task = planner_task([loc_task, gde_task], planning_expert, destination, interests, date_from, date_to)
        my_crew = Crew(
            agents = [trip_expert, city_guide, planning_expert],
            tasks = [loc_task, gde_task, plan_task],
            process = Process.sequential,
            full_output = True,
            verbose = True
        )
        result = my_crew.kickoff()

        st.subheader("Here's your travel itinerary: ")
        st.markdown(result)

        travel_plan = str(result)
        st.download_button(
            label="📥 Download Travel Plan",
            data=travel_plan, 
            file_name=f"Travel_Plan_{destination}.txt",
            mime="text/plain"
        )