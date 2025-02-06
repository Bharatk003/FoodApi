# FoodApi
Base URL
Your API is hosted at:
🔗 https://foodapi-w4h3.onrender.com/

🍎 API Endpoints
⿡ Get Nutrition Details
📌 Endpoint:

plaintext
Copy
Edit
GET /api/get_nutrition/<food_item>/<quantity>/<unit>
📌 Description:

Fetches nutritional information for a given food item.
Requires:
food_item → The name of the food (e.g., apple).
quantity → The amount (e.g., 2).
unit → The measurement unit (e.g., kg, grams, etc.).
📌 Example Request:

plaintext
Copy
Edit
GET https://foodapi-w4h3.onrender.com/api/get_nutrition/apple/2/kg
📌 Example Response:

json
Copy
Edit
{
    "food_item": "apple",
    "served_quantity": 2,
    "served_unit": "kg",
    "calories": 1040,
    "protein_grams": 2.1,
    "carbohydrates_grams": 270,
    "fat_grams": 2,
    "sugar_grams": 220,
    "fiber_grams": 20,
    "sodium_mg": 2
}
⿢ Get Merits & Demerits
📌 Endpoint:

plaintext
Copy
Edit
GET /api/get_merits_demerits/<food_item>
📌 Description:

Returns the health benefits (merits) and risks (demerits) of a food item.
📌 Example Request:

plaintext
Copy
Edit
GET https://foodapi-w4h3.onrender.com/api/get_merits_demerits/apple
📌 Example Response:

json
Copy
Edit
{
    "food_item": "apple",
    "merits": [
        "Rich in fiber and supports digestion.",
        "Good source of vitamin C for immunity.",
        "Low in calories and good for weight management."
    ],
    "demerits": [
        "May cause bloating if eaten in excess.",
        "Contains natural sugars that may affect diabetics."
    ]
}
⿣ Get AI-Powered Reply
📌 Endpoint:

plaintext
Copy
Edit
POST /api/get_reply
📌 Description:

Generates a short AI-powered reply based on:
user_query → The question/query about food/nutrition.
user_goal → The dietary goal (e.g., weight loss, muscle gain).
current_macros_details → Current macros (carbs, protein, fats).
📌 Example Request (JSON Body):

json
Copy
Edit
{
    "user_query": "What should I eat for muscle gain?",
    "user_goal": "Increase muscle mass",
    "current_macros_details": "High protein, moderate carbs, low fat"
}
📌 Example Response:

json
Copy
Edit
{
    "reply": "You should consume protein-rich foods like chicken breast, eggs, Greek yogurt, and legumes. Balance it with carbs for energy."
}
⿤ Get Food Suggestions
📌 Endpoint:

plaintext
Copy
Edit
POST /api/get_suggestions
📌 Description:

Suggests 5 food items based on:
user_goal → What the user wants to achieve.
current_macros_details → Their current diet.
last_meals_of_day → What they ate earlier.
📌 Example Request (JSON Body):

json
Copy
Edit
{
    "user_goal": "Weight loss",
    "current_macros_details": "High protein, low carbs",
    "last_meals_of_day": "Eggs, avocado toast, green tea"
}
📌 Example Response:

json
Copy
Edit
{
    "suggestions": {
        "grilled_salmon": {
            "short_description": "Rich in omega-3, great for heart health.",
            "calories": 300,
            "protein_grams": 35,
            "carbohydrates_grams": 0,
            "fat_grams": 15,
            "sugar_grams": 0,
            "fiber_grams": 0,
            "sodium_mg": 50
        },
        "quinoa_salad": {
            "short_description": "High in fiber and plant protein.",
            "calories": 250,
            "protein_grams": 10,
            "carbohydrates_grams": 45,
            "fat_grams": 5,
            "sugar_grams": 2,
            "fiber_grams": 5,
            "sodium_mg": 30
        }
    }
}
