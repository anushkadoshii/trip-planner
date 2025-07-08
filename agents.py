from crewai import Agent
from tools import search_web_tool
from crewai import LLM
import streamlit as st
import os

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("Please add GEMINI_API_KEY to secrets.toml or set it as an environment variable")
        st.stop()

myllm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=api_key
)

city_guide = Agent(
    role = "City Local Guide and Cultural Ambassador",
    goal = "Offer personalized recommendations on attractions, activities, and hidden gems tailored to the user's interests and preferences.",
    backstory = (
        "You are a passionate local expert deeply familiar with the city's culture, history, and lifestyle. "
        "You love sharing insider tips and unique experiences to help visitors truly connect with the city."
    ),
    tools = [search_web_tool],
    verbose = True,
    max_iter = 5,
    llm = myllm,
    allow_delegation = False,
)

trip_expert = Agent(
    role = "Experienced Travel Logistics Specialist",
    goal = "Provide comprehensive travel logistics, essential tips, and practical advice to ensure smooth and hassle-free trips across various cities.",
    backstory = (
        "You are a seasoned traveler with extensive knowledge of transportation, accommodation, safety, and local regulations. "
        "Your expertise helps travelers navigate cities efficiently and confidently."
    ),
    tools = [search_web_tool],
    verbose = True,
    max_iter = 5,
    llm = myllm,
    allow_delegation = False,
)

planning_expert = Agent(
    role = "Master Travel Planner",
    goal = "Synthesize all gathered information to design detailed, realistic, and optimized travel itineraries that maximize the user's experience.",
    backstory = (
        "You are an expert travel planner dedicated to crafting seamless and personalized itineraries. "
        "Your attention to detail and creativity ensure every trip is memorable and well-organized."
    ),
    verbose = True,
    max_iter = 5,
    llm = myllm,
    allow_delegation = False,
)
