from crewai import Task

def guide_task(agent, destination, interests, date_from, date_to):
    return Task(
        description=f"""
        Provide a travel guide with attractions, food recommendations, and events.
        Tailor recommendations based on user interests: {interests}.
        
        Destination: {destination}
        Arrival Date: {date_from}
        Departure Date: {date_to}
        """,
        expected_output="A day-wise itinerary including attractions, food, and activities.",
        agent=agent,
        output_file='guide_report.md',
    )

def location_task(agent, source, destination, date_from, date_to):
     return Task(
        description=f"""
        Provide travel-related information including accommodations, cost of living, visa requirements, transportation, weather, and local events.
        Traveling from: {source}
        Destination: {destination}
        Arrival Date: {date_from}
        Departure Date: {date_to}
        """,
        expected_output="A detailed report with relevant travel data.",
        agent=agent,
        output_file='city_report.md',
    )

def planner_task(context, agent, destination, interests, date_from, date_to):
     return Task(
        description=f"""
        Combine information into a well-structured itinerary. Include:
        - City introduction (4 paragraphs)
        - Daily travel plan with time allocations
        - Expenses and tips

        Destination: {destination}
        Interests: {interests}
        Arrival: {date_from}
        Departure: {date_to}
        """,
        expected_output="A structured travel itinerary.",
        context=context,
        agent=agent,
        output_file='travel_plan.md',
    )
