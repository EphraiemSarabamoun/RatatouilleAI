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
    persona = "You are a nutritionist providing meal suggestions to a client based on the information they provide about the ingredients they have in their fridge. Give the client, three meal suggestions along with time estimates for each meal, and the meal recipies."
    print(prompt)
    
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