from crewai import Agent
from tools import search_web_tool
from langchain_ollama.llms import OllamaLLM

myllm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
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
