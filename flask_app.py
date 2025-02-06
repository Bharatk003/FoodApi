from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Directly set the API key (replace with your actual key)
GEMINI_API_KEY = "AIzaSyBNVqdWlXvmVd1MAJ_k2QBzxfJ95lbAilw"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_nutrition_prompt(food_item, quantity, unit):
    return f"""
    Provide detailed nutritional information for {quantity} {unit} of {food_item} in strict JSON format.
    Use metric units and follow this exact structure:
    {{
        "food_item": "{food_item}",
        "served_quantity": {quantity},
        "served_unit": "{unit}",
        "calories": number,
        "protein_grams": number,
        "carbohydrates_grams": number,
        "fat_grams": number,
        "sugar_grams": number,
        "fiber_grams": number,
        "sodium_mg": number
    }}
    If the item is not food, return {{ "error": "Invalid food item" }}.
    """

@app.route('/api/get_nutrition/<food_item>/<quantity>/<unit>', methods=['GET'])
def get_nutrition(food_item, quantity, unit):
    try:
        quantity = float(quantity)  # Convert quantity to float
        prompt = get_nutrition_prompt(food_item, quantity, unit)
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return jsonify(response.text)
        else:
            return jsonify({"error": "Invalid response from API"}), 500

    except ValueError:
        return jsonify({'error': 'Quantity must be a valid number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_merits_demerits_prompt(food_item):
    return f"""
    Provide the merits (benefits) and demerits (drawbacks) of consuming {food_item} in strict JSON format.
    Follow this exact structure:
    {{
        "food_item": "{food_item}",
        "merits": [
            "Benefit 1",
            "Benefit 2",
            "Benefit 3"
        ],
        "demerits": [
            "Drawback 1",
            "Drawback 2",
            "Drawback 3"
        ]
    }}
    If the item is not a valid food, return {{ "error": "Invalid food item" }}.
    """

@app.route('/api/get_merits_demerits/<food_item>', methods=['GET'])
def get_merits_demerits(food_item):
    try:
        prompt = get_merits_demerits_prompt(food_item)
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return jsonify(response.text)
        else:
            return jsonify({"error": "Invalid response from API"}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get_reply', methods=['POST'])
def get_reply():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user_query = data.get('user_query')
    user_goal = data.get('user_goal')
    current_macros_details = data.get('current_macros_details')

    if not user_query or not user_goal or not current_macros_details:
        return jsonify({'error': 'Missing required parameters: user_query, user_goal, or current_macros_details'}), 400

    try:
        prompt = f"User Query: {user_query}\nUser Goal: {user_goal}\nCurrent Macros: {current_macros_details}"
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return jsonify({'reply': response.text})
        else:
            return jsonify({'error': 'Invalid response from API'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get_suggestions', methods=['POST'])
def get_suggestions():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user_goal = data.get('user_goal')
    current_macros_details = data.get('current_macros_details')
    last_meals_of_day = data.get('last_meals_of_day')

    if not user_goal or not current_macros_details or not last_meals_of_day:
        return jsonify({'error': 'Missing required parameters: user_goal, current_macros_details, or last_meals_of_day'}), 400

    try:
        prompt = f"""
        User Goal: {user_goal}
        Current Macros: {current_macros_details}
        Last Meals of Day: {last_meals_of_day}
        Current Time: {datetime.now().time()}
        Suggest 5 food items considering user goals and macros.
        """
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return jsonify({'suggestions': response.text})
        else:
            return jsonify({'error': 'Invalid response from API'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
