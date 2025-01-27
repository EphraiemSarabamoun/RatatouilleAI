import openai
import json
import os
from dotenv import load_dotenv

# Load your API key from an environment variable or secret management service
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def load_groceries(file_path):
    with open(file_path, 'r') as file:
        groceries = json.load(file)
    return groceries

def generate_meals(groceries):
    prompt = f"Here are the ingredients I have: {', '.join(groceries["fridge"])}. Suggest three meals I can make with these ingredients."
    persona = f"""
You are a nutritionist providing meal suggestions to a client based on the information they provide about the ingredients they have in their fridge.

Here are the ingredients I have: {', '.join(groceries["fridge"])}.

Please provide:
1. Three meal suggestions enclosed in `<suggestion></suggestion>` tags.
2. Corresponding time estimates for each meal enclosed in `<time></time>` tags, as a single integer representing the number of minutes (e.g., 15).
3. Detailed recipes for each meal enclosed in `<recipe></recipe>` tags.

Format your response like this:
<suggestion>Meal 1</suggestion>
<time>15</time>
<recipe>Recipe for Meal 1</recipe>
<suggestion>Meal 2</suggestion>
<time>20</time>
<recipe>Recipe for Meal 2</recipe>
<suggestion>Meal 3</suggestion>
<time>5</time>
<recipe>Recipe for Meal 3</recipe>
"""
        
    response = openai.ChatCompletion.create(model="gpt-4-turbo", messages=[
                {"role": "system", "content": persona},
                {"role": "user", "content": prompt}], temperature = 0.7)
    
    return response['choices'][0]['message']['content'].strip()

def main():
    groceries = load_groceries('/Users/fatherdomadious/Desktop/Personal_Projects/RatatouilleAI/Backend/groceries.json')
    meals = generate_meals(groceries)
    print("Here are three meal suggestions:")
    print(meals)


main()