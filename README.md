# 🌍 WanderAI – Travel Itinerary Planner

WanderAI is an intelligent travel assistant that creates personalized trip itineraries, combining real-time web search, expert recommendations, and seamless planning. Enter your travel details, and WanderAI delivers a custom itinerary with attractions, food, logistics, and more.

**Streamlit App Link** : https://trip-itinerary-generator.streamlit.app/


---

## Features

- **Personalized Day-Wise Itineraries:**  
  Tailored plans based on your interests, travel dates, and destination.

- **Expert Recommendations:**  
  Suggestions for attractions, local food, events, and hidden gems.

- **Comprehensive Travel Logistics:**  
  Accommodation, transportation, visa requirements, cost of living, and weather.

- **Real-Time Web Search:**  
  Up-to-date information using DuckDuckGo search integration.

- **Downloadable Reports:**  
  Get your full itinerary as a downloadable text file.

---

## Quick Start

### 1. Clone the Repository

```
git clone 
cd 
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

- Obtain a Google Gemini API key.
- Set the `GEMINI_API_KEY` environment variable:
  ```
  export GEMINI_API_KEY=your_api_key_here
  ```

### 4. Run the App

```
streamlit run app.py
```

---

## Usage

1. **Launch the app** – The Streamlit UI will prompt you for:
    - Source City
    - Destination City
    - Departure and Return Dates
    - Your Interests (choose from museums, nature, food, adventure, etc.)

2. **Generate Itinerary** – Click the button to create your plan.

3. **View & Download** – Your personalized itinerary appears on-screen and can be downloaded as a text file.

---

## Project Structure

| File/Folder        | Purpose                                                      |
|--------------------|--------------------------------------------------------------|
| `app.py`           | Main Streamlit app; user interface and workflow orchestration|
| `agents.py`        | Defines travel expert agents (guide, logistics, planner)     |
| `tasks.py`         | Task functions for guides, logistics, and itinerary planning |
| `tools.py`         | Web search tool integration (DuckDuckGo)                     |
| `requirements.txt` | Python dependencies                                          |

---

## Agents Overview

| Agent Name         | Role                                      | Goal                                                      |
|--------------------|-------------------------------------------|-----------------------------------------------------------|
| `city_guide`       | City Local Guide & Cultural Ambassador    | Personalized recommendations, local insights              |
| `trip_expert`      | Experienced Travel Logistics Specialist   | Logistics, safety, accommodation, regulations             |
| `planning_expert`  | Master Travel Planner                     | Synthesizes info, crafts detailed itineraries             |

---

## Task Functions

| Function         | Output File         | Description                                              |
|------------------|--------------------|----------------------------------------------------------|
| `guide_task`     | `guide_report.md`  | Attractions, food, events, day-wise recommendations      |
| `location_task`  | `city_report.md`   | Accommodation, cost, visa, transport, weather, events    |
| `planner_task`   | `travel_plan.md`   | Structured itinerary: intro, daily plan, expenses, tips  |


