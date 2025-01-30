from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.get("/random")
def read_root():
    return {"message": "Random roast!"}

# Categorized IT Roasts
roasts = {
    "general": [
        "Your code is like a time capsule—future archaeologists will study it.",
        "You have more dependencies than a toddler.",
        "Your documentation is so vague, it could be a horoscope.",
    ],
    "debugging": [
        "You spend more time debugging than coding.",
        "Your logs are just stack traces with timestamps.",
        "Your debugging strategy is ‘Try-Catch-Pray’.",
    ],
    "sql": [
        "Your SQL queries run so slow, they have their own time zone.",
        "Your database schema is a conspiracy theory in table form.",
        "Your JOINs are so bad, even your tables want a divorce.",
    ],
    "corporate": [
        "You have more meetings than completed tasks.",
        "Your ‘agile’ process is just chaos with sticky notes.",
        "Your ‘hotfix’ is just a band-aid on a bullet wound.",
    ],
    "devops": [
        "Your cloud costs are higher than my rent.",
        "Your AWS bill is so high, Jeff Bezos sent you a thank-you card.",
        "Your uptime is measured in coin flips.",
    ],
    "frontend": [
        "Your CSS skills are just ‘copy from Stack Overflow’.",
        "Your UI is so bad, it’s a UX horror story.",
        "Your animations are so janky, they need a chiropractor.",
    ],
    "ai": [
        "Your AI model is just a random number generator in disguise.",
        "Your neural network has fewer connections than you on LinkedIn.",
        "Your chatbot is dumber than a rock with Wi-Fi.",
    ]
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the IT Roasts API! Use /random or /random?category=debugging"}

@app.get("/random")
def get_random_roast(category: str = Query(None, description="Category of roast")):
    """Returns a random IT roast. If a category is specified, returns a roast from that category."""
    if category:
        category = category.lower()
        if category in roasts:
            return {"category": category, "roast": random.choice(roasts[category])}
        else:
            return {"error": "Invalid category. Available categories: " + ", ".join(roasts.keys())}
    
    # Get a random roast from any category
    all_roasts = [joke for sublist in roasts.values() for joke in sublist]
    return {"category": "random", "roast": random.choice(all_roasts)}

@app.get("/all")
def get_all_roasts():
    """Returns all IT roasts categorized."""
    return roasts