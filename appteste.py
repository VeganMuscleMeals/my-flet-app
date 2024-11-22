import flet as ft
import json
import os

# Dados do usuário e favoritos
data_file = "user_data.json"
user_data = {"weight": None, "height": None, "age": None, "gender": None, "goal": None, "favorites": []}
is_dark_mode = {"enabled": False}

# Paleta de Cores
PALETTE = {
    "background_light": "#F8F9FA",  # Fundo claro
    "background_dark": "#2C2C2C",  # Fundo escuro
    "primary": "#A1C9F1",          # Azul pastel
    "secondary": "#E3D5CA",        # Bege claro
    "accent": "#C3AED6",           # Lilás
    "text_dark": "#1A1A1A",        # Preto para textos
    "text_light": "#FFFFFF",       # Branco para textos
    "button_bg": "#A1C9F1",        # Botão com azul pastel
    "button_text": "#1A1A1A",      # Texto do botão em preto
}

# Proporções de calorias diárias por refeição
meal_proportions = {
    "Smoothies": 0.1,  # Lanche da manhã ou ceia
    "Snacks": 0.1,     # Lanche da tarde
    "Lunch": 0.3,      # Almoço
}

# Função para carregar dados locais
def load_user_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return {"weight": None, "height": None, "age": None, "gender": None, "goal": None, "favorites": []}

# Função para salvar dados locais
def save_user_data():
    with open(data_file, "w") as f:
        json.dump(user_data, f)

# Carregar os dados salvos
user_data.update(load_user_data())

# Receitas
recipes = {
    "Smoothies": [
            {
        "name": "Banana and Oat Smoothie",
        "calories": 280,
        "protein": 20,
        "carbs": 40,
        "fats": 10,
        "ingredients": [
            {"name": "Almond milk", "quantity": 240, "unit": "ml"},
            {"name": "Frozen banana", "quantity": 100, "unit": "g"},
            {"name": "Oats", "quantity": 40, "unit": "g"},
            {"name": "Sunflower seeds", "quantity": 10, "unit": "g"},
            {"name": "Protein powder", "quantity": 25, "unit": "g"},
        ],
    },
    {
        "name": "Strawberry and Flaxseed Smoothie",
        "calories": 300,
        "protein": 18,
        "carbs": 45,
        "fats": 8,
        "ingredients": [
            {"name": "Almond milk", "quantity": 240, "unit": "ml"},
            {"name": "Frozen strawberries", "quantity": 150, "unit": "g"},
            {"name": "Flax seeds", "quantity": 10, "unit": "g"},
            {"name": "Protein powder", "quantity": 25, "unit": "g"},
        ],
    },
    {
        "name": "Blueberry and Yogurt Smoothie",
        "calories": 250,
        "protein": 15,
        "carbs": 40,
        "fats": 6,
        "ingredients": [
            {"name": "Fresh blueberries", "quantity": 150, "unit": "g"},
            {"name": "Greek soy yogurt", "quantity": 120, "unit": "g"},
            {"name": "Pea protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Honey", "quantity": 20, "unit": "g"},
        ],
    },
    {
        "name": "Avocado and Spinach Smoothie",
        "calories": 320,
        "protein": 12,
        "carbs": 25,
        "fats": 18,
        "ingredients": [
            {"name": "Avocado", "quantity": 75, "unit": "g"},
            {"name": "Fresh spinach", "quantity": 30, "unit": "g"},
            {"name": "Pea protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Honey", "quantity": 20, "unit": "g"},
        ],
    },
    {
        "name": "Mango and Coconut Milk Smoothie",
        "calories": 350,
        "protein": 10,
        "carbs": 50,
        "fats": 15,
        "ingredients": [
            {"name": "Ripe mango", "quantity": 150, "unit": "g"},
            {"name": "Coconut milk", "quantity": 120, "unit": "ml"},
            {"name": "Rice protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Honey", "quantity": 20, "unit": "g"},
        ],
    },
    {
        "name": "Banana Peanut Butter Smoothie",
        "calories": 360,
        "protein": 25,
        "carbs": 35,
        "fats": 15,
        "ingredients": [
            {"name": "Sliced banana", "quantity": 100, "unit": "g"},
            {"name": "Peanut butter", "quantity": 60, "unit": "g"},
            {"name": "Almond milk", "quantity": 60, "unit": "ml"},
            {"name": "Flavored protein powder", "quantity": 25, "unit": "g"},
            {"name": "Golden flaxseed", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Strawberry and Tofu Smoothie",
        "calories": 290,
        "protein": 22,
        "carbs": 40,
        "fats": 6,
        "ingredients": [
            {"name": "Frozen strawberries", "quantity": 150, "unit": "g"},
            {"name": "Tofu", "quantity": 120, "unit": "g"},
            {"name": "Flavored protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 60, "unit": "ml"},
            {"name": "Golden flaxseed", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Pineapple and Coconut Smoothie",
        "calories": 300,
        "protein": 20,
        "carbs": 45,
        "fats": 10,
        "ingredients": [
            {"name": "Frozen pineapple", "quantity": 150, "unit": "g"},
            {"name": "Coconut water", "quantity": 60, "unit": "ml"},
            {"name": "Flavored protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 60, "unit": "ml"},
            {"name": "Golden flaxseed", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Spinach and Almond Smoothie",
        "calories": 320,
        "protein": 22,
        "carbs": 30,
        "fats": 14,
        "ingredients": [
            {"name": "Spinach", "quantity": 30, "unit": "g"},
            {"name": "Almonds", "quantity": 30, "unit": "g"},
            {"name": "Flavored protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 60, "unit": "ml"},
            {"name": "Golden flaxseed", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Papaya and Chia Smoothie",
        "calories": 280,
        "protein": 20,
        "carbs": 35,
        "fats": 8,
        "ingredients": [
            {"name": "Chopped papaya", "quantity": 150, "unit": "g"},
            {"name": "Almond milk", "quantity": 60, "unit": "ml"},
            {"name": "Protein powder", "quantity": 25, "unit": "g"},
            {"name": "Chia seeds", "quantity": 10, "unit": "g"},
            {"name": "Golden flaxseed", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Avocado and Cocoa Smoothie",
        "calories": 340,
        "protein": 18,
        "carbs": 28,
        "fats": 22,
        "ingredients": [
            {"name": "Avocado", "quantity": 75, "unit": "g"},
            {"name": "Almond milk", "quantity": 60, "unit": "ml"},
            {"name": "Cocoa-flavored protein powder", "quantity": 25, "unit": "g"},
            {"name": "Golden flaxseed", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Blueberry Banana Smoothie",
        "calories": 290,
        "protein": 18,
        "carbs": 42,
        "fats": 8,
        "ingredients": [
            {"name": "Banana", "quantity": 100, "unit": "g"},
            {"name": "Blueberries", "quantity": 150, "unit": "g"},
            {"name": "Vegan protein powder", "quantity": 25, "unit": "g"},
            {"name": "Rolled oats", "quantity": 20, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Chia seeds", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Mango Avocado Smoothie",
        "calories": 320,
        "protein": 15,
        "carbs": 40,
        "fats": 12,
        "ingredients": [
            {"name": "Ripe mango", "quantity": 150, "unit": "g"},
            {"name": "Ripe avocado", "quantity": 75, "unit": "g"},
            {"name": "Vegan protein powder", "quantity": 25, "unit": "g"},
            {"name": "Coconut milk", "quantity": 120, "unit": "ml"},
            {"name": "Almond butter", "quantity": 20, "unit": "g"},
        ],
    },
    {
        "name": "Green Power Smoothie",
        "calories": 240,
        "protein": 10,
        "carbs": 30,
        "fats": 5,
        "ingredients": [
            {"name": "Spinach", "quantity": 30, "unit": "g"},
            {"name": "Banana", "quantity": 100, "unit": "g"},
            {"name": "Vegan protein powder", "quantity": 25, "unit": "g"},
            {"name": "Rolled oats", "quantity": 20, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Flax seeds", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Strawberry Banana Smoothie",
        "calories": 270,
        "protein": 14,
        "carbs": 40,
        "fats": 6,
        "ingredients": [
            {"name": "Banana", "quantity": 100, "unit": "g"},
            {"name": "Strawberries", "quantity": 150, "unit": "g"},
            {"name": "Vegan protein powder", "quantity": 25, "unit": "g"},
            {"name": "Rolled oats", "quantity": 20, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Hemp seeds", "quantity": 10, "unit": "g"},
        ],
    },
    {
        "name": "Chocolate Peanut Butter Smoothie",
        "calories": 310,
        "protein": 25,
        "carbs": 35,
        "fats": 10,
        "ingredients": [
            {"name": "Banana", "quantity": 100, "unit": "g"},
            {"name": "Chocolate protein powder", "quantity": 25, "unit": "g"},
            {"name": "Peanut butter", "quantity": 20, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Rolled oats", "quantity": 20, "unit": "g"},
        ],
    },
    {
        "name": "Peach Ginger Smoothie",
        "calories": 260,
        "protein": 15,
        "carbs": 40,
        "fats": 5,
        "ingredients": [
            {"name": "Peach", "quantity": 150, "unit": "g"},
            {"name": "Fresh ginger", "quantity": 5, "unit": "g"},
            {"name": "Vegan protein powder", "quantity": 25, "unit": "g"},
            {"name": "Almond milk", "quantity": 120, "unit": "ml"},
            {"name": "Rolled oats", "quantity": 20, "unit": "g"},
            {"name": "Chia seeds", "quantity": 10, "unit": "g"},
        ],
    },
    {
    "name": "Strawberry and Oat Smoothie",
    "calories": 300,
    "protein": 18,
    "carbs": 45,
    "fats": 8,
    "ingredients": [
        {"name": "Almond milk", "quantity": 240, "unit": "ml"},
        {"name": "Frozen strawberries", "quantity": 150, "unit": "g"},
        {"name": "Flax seeds", "quantity": 10, "unit": "g"},
        {"name": "Protein powder", "quantity": 25, "unit": "g"},
        ],
    },
],
    "Snacks": [
        {
        "name": "Veggie Burger",
        "calories": 450,
        "protein": 25,
        "carbs": 50,
        "fats": 15,
        "ingredients": [
            {"name": "Ground chickpeas", "quantity": 150, "unit": "g"},
            {"name": "Grated carrots", "quantity": 120, "unit": "g"},
            {"name": "Chopped onion", "quantity": 40, "unit": "g"},
            {"name": "Oatmeal", "quantity": 20, "unit": "g"},
            {"name": "Olive oil", "quantity": 15, "unit": "ml"},
            {"name": "Whole-grain buns", "quantity": 60, "unit": "g"},
            {"name": "Tomatoes", "quantity": 50, "unit": "g"},
            {"name": "Lettuce", "quantity": 10, "unit": "g"},
            {"name": "Cucumber", "quantity": 30, "unit": "g"},
            {"name": "Hummus", "quantity": 15, "unit": "g"},
        ],
    },
    {
        "name": "Bean and Vegetable Tacos",
        "calories": 380,
        "protein": 15,
        "carbs": 45,
        "fats": 10,
        "ingredients": [
            {"name": "Cooked beans", "quantity": 150, "unit": "g"},
            {"name": "Diced vegetables", "quantity": 100, "unit": "g"},
            {"name": "Cornflour tortillas", "quantity": 40, "unit": "g"},
            {"name": "Chopped tofu", "quantity": 30, "unit": "g"},
            {"name": "Salsa", "quantity": 30, "unit": "g"},
            {"name": "Guacamole", "quantity": 30, "unit": "g"},
        ],
    },
    {
        "name": "Avocado and Chickpea Tostadas",
        "calories": 320,
        "protein": 12,
        "carbs": 30,
        "fats": 15,
        "ingredients": [
            {"name": "Avocado", "quantity": 100, "unit": "g"},
            {"name": "Lemon juice", "quantity": 15, "unit": "ml"},
            {"name": "Chickpea tostadas", "quantity": 30, "unit": "g"},
            {"name": "Cooked chickpeas", "quantity": 75, "unit": "g"},
        ],
    },
    {
        "name": "Wholemeal Bread with Chickpea Paste and Vegetables",
        "calories": 350,
        "protein": 20,
        "carbs": 40,
        "fats": 8,
        "ingredients": [
            {"name": "Wholemeal bread", "quantity": 60, "unit": "g"},
            {"name": "Cooked chickpeas", "quantity": 150, "unit": "g"},
            {"name": "Garlic", "quantity": 5, "unit": "g"},
            {"name": "Olive oil", "quantity": 15, "unit": "ml"},
            {"name": "Tomatoes", "quantity": 50, "unit": "g"},
            {"name": "Cucumber", "quantity": 30, "unit": "g"},
            {"name": "Arugula", "quantity": 10, "unit": "g"},
            {"name": "Tofu cubes", "quantity": 30, "unit": "g"},
        ],
    },
    {
        "name": "Vegetable Wraps",
        "calories": 300,
        "protein": 12,
        "carbs": 35,
        "fats": 8,
        "ingredients": [
            {"name": "Diced vegetables", "quantity": 100, "unit": "g"},
            {"name": "Chopped tofu", "quantity": 30, "unit": "g"},
            {"name": "Whole wheat wrap", "quantity": 40, "unit": "g"},
            {"name": "Olive oil", "quantity": 10, "unit": "ml"},
        ],
    },
    {
        "name": "Vegetable Pie",
        "calories": 420,
        "protein": 15,
        "carbs": 45,
        "fats": 15,
        "ingredients": [
            {"name": "Oatmeal", "quantity": 100, "unit": "g"},
            {"name": "Chopped onion", "quantity": 40, "unit": "g"},
            {"name": "Chopped walnuts", "quantity": 30, "unit": "g"},
            {"name": "Olive oil", "quantity": 15, "unit": "ml"},
            {"name": "Diced vegetables", "quantity": 200, "unit": "g"},
            {"name": "Chopped tofu", "quantity": 30, "unit": "g"},
        ],
    },
    {
        "name": "Tofu Salad Sandwich",
        "calories": 360,
        "protein": 20,
        "carbs": 35,
        "fats": 10,
        "ingredients": [
            {"name": "Wholemeal bread", "quantity": 60, "unit": "g"},
            {"name": "Firm tofu", "quantity": 100, "unit": "g"},
            {"name": "Mustard", "quantity": 10, "unit": "g"},
            {"name": "Honey", "quantity": 10, "unit": "g"},
            {"name": "Apple cider vinegar", "quantity": 15, "unit": "ml"},
            {"name": "Olive oil", "quantity": 10, "unit": "ml"},
            {"name": "Green salad", "quantity": 50, "unit": "g"},
        ],
    },
    {
        "name": "Bean Sandwich with Vegetables",
        "calories": 340,
        "protein": 18,
        "carbs": 40,
        "fats": 8,
        "ingredients": [
            {"name": "Wholemeal bread", "quantity": 60, "unit": "g"},
            {"name": "Cooked beans", "quantity": 150, "unit": "g"},
            {"name": "Tomato", "quantity": 50, "unit": "g"},
            {"name": "Cucumber", "quantity": 30, "unit": "g"},
            {"name": "Carrot", "quantity": 50, "unit": "g"},
            {"name": "Vegan mayonnaise", "quantity": 15, "unit": "g"},
        ],
    },
    {
        "name": "Eggplant Sandwich with Hummus",
        "calories": 350,
        "protein": 15,
        "carbs": 35,
        "fats": 10,
        "ingredients": [
            {"name": "Wholemeal bread", "quantity": 60, "unit": "g"},
            {"name": "Eggplant", "quantity": 100, "unit": "g"},
            {"name": "Hummus", "quantity": 30, "unit": "g"},
            {"name": "Olive oil", "quantity": 10, "unit": "ml"},
            {"name": "Tomato", "quantity": 50, "unit": "g"},
            {"name": "Cucumber", "quantity": 30, "unit": "g"},
        ],
    },
    {
        "name": "Tofu Avocado Sandwich",
        "calories": 340,
        "protein": 18,
        "carbs": 35,
        "fats": 8,
        "ingredients": [
            {"name": "Wholemeal bread", "quantity": 60, "unit": "g"},
            {"name": "Firm tofu", "quantity": 100, "unit": "g"},
            {"name": "Avocado", "quantity": 50, "unit": "g"},
            {"name": "Tomato sauce", "quantity": 20, "unit": "ml"},
            {"name": "Lettuce", "quantity": 10, "unit": "g"},
            {"name": "Olive oil", "quantity": 10, "unit": "ml"},
        ],
    },
    {
    "name": "Spinach Mushroom Sandwich",
    "calories": 340,
    "protein": 15,
    "carbs": 38,
    "fats": 8,
    "ingredients": [
        {"name": "Rye bread", "quantity": 60, "unit": "g"},
        {"name": "Fresh mushrooms", "quantity": 100, "unit": "g"},
        {"name": "Fresh spinach", "quantity": 30, "unit": "g"},
        {"name": "Vegan curd", "quantity": 15, "unit": "g"},
        {"name": "Mustard", "quantity": 10, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "ml"},
        ],
    },
    {
    "name": "Vegan Vegetable Nuggets",
    "calories": 320,
    "protein": 10,
    "carbs": 40,
    "fats": 15,
    "ingredients": [
        {"name": "Potatoes", "quantity": 200, "unit": "g"},
        {"name": "Green corn", "quantity": 150, "unit": "g"},
        {"name": "Peas", "quantity": 150, "unit": "g"},
        {"name": "Onion", "quantity": 40, "unit": "g"},
        {"name": "Garlic", "quantity": 5, "unit": "g"},
        {"name": "Salt", "quantity": 5, "unit": "g"},
        {"name": "Cumin powder", "quantity": 2, "unit": "g"},
        {"name": "Turmeric powder", "quantity": 2, "unit": "g"},
        {"name": "Cornflour", "quantity": 50, "unit": "g"},
        {"name": "Oil", "quantity": 15, "unit": "ml"},
        ],
    },
    {
    "name": "Savory Broccoli and Tofu Crepe",
    "calories": 290,
    "protein": 12,
    "carbs": 35,
    "fats": 10,
    "ingredients": [
        {"name": "Rice flour", "quantity": 20, "unit": "g"},
        {"name": "Golden flax meal", "quantity": 10, "unit": "g"},
        {"name": "Oat flakes", "quantity": 10, "unit": "g"},
        {"name": "Chia seeds", "quantity": 5, "unit": "g"},
        {"name": "Turmeric powder", "quantity": 2, "unit": "g"},
        {"name": "Salt", "quantity": 2, "unit": "g"},
        {"name": "Black pepper", "quantity": 2, "unit": "g"},
        {"name": "Water", "quantity": 50, "unit": "ml"},
        {"name": "Fried tofu", "quantity": 50, "unit": "g"},
        {"name": "Broccoli with garlic", "quantity": 50, "unit": "g"},
        ],
    },
    {
    "name": "Vegan Frying Pan Pizza",
    "calories": 310,
    "protein": 10,
    "carbs": 40,
    "fats": 12,
    "ingredients": [
        {"name": "Beetroot juice", "quantity": 30, "unit": "ml"},
        {"name": "Chia seeds", "quantity": 10, "unit": "g"},
        {"name": "Oats", "quantity": 10, "unit": "g"},
        {"name": "Rice flour", "quantity": 20, "unit": "g"},
        {"name": "Herb salt", "quantity": 5, "unit": "g"},
        {"name": "Baking powder", "quantity": 5, "unit": "g"},
        {"name": "Kale leaf", "quantity": 10, "unit": "g"},
        {"name": "Cashew nuts", "quantity": 30, "unit": "g"},
        {"name": "Cherry tomatoes", "quantity": 50, "unit": "g"},
        {"name": "Oregano", "quantity": 5, "unit": "g"},
        ],
    },
    {
    "name": "Easy Vegan Blender Pie",
    "calories": 350,
    "protein": 10,
    "carbs": 45,
    "fats": 15,
    "ingredients": [
        {"name": "Olive oil", "quantity": 10, "unit": "ml"},
        {"name": "Onion", "quantity": 40, "unit": "g"},
        {"name": "Garlic", "quantity": 5, "unit": "g"},
        {"name": "Carrot", "quantity": 50, "unit": "g"},
        {"name": "Tomato", "quantity": 50, "unit": "g"},
        {"name": "Peas", "quantity": 50, "unit": "g"},
        {"name": "Corn", "quantity": 50, "unit": "g"},
        {"name": "Salt", "quantity": 5, "unit": "g"},
        {"name": "Smoked paprika", "quantity": 5, "unit": "g"},
        {"name": "Olives", "quantity": 30, "unit": "g"},
        {"name": "Black pepper", "quantity": 5, "unit": "g"},
        {"name": "Wheat flour", "quantity": 200, "unit": "g"},
        {"name": "Yeast", "quantity": 5, "unit": "g"},
        {"name": "Sunflower oil", "quantity": 15, "unit": "ml"},
        {"name": "Turmeric", "quantity": 5, "unit": "g"},
        ],
    },
    {
    "name": "Vegan Protein Pancakes",
    "calories": 300,
    "protein": 15,
    "carbs": 40,
    "fats": 10,
    "ingredients": [
        {"name": "Banana", "quantity": 100, "unit": "g"},
        {"name": "Vegan protein powder", "quantity": 20, "unit": "g"},
        {"name": "Rolled oats", "quantity": 20, "unit": "g"},
        {"name": "Almond milk", "quantity": 50, "unit": "ml"},
        {"name": "Baking powder", "quantity": 5, "unit": "g"},
        {"name": "Vanilla extract", "quantity": 5, "unit": "ml"},
        ],
    },
    {
    "name": "Vegan Blueberry Muffins",
    "calories": 260,
    "protein": 8,
    "carbs": 38,
    "fats": 6,
    "ingredients": [
        {"name": "Whole wheat flour", "quantity": 200, "unit": "g"},
        {"name": "Vegan protein powder", "quantity": 50, "unit": "g"},
        {"name": "Baking powder", "quantity": 10, "unit": "g"},
        {"name": "Baking soda", "quantity": 5, "unit": "g"},
        {"name": "Salt", "quantity": 5, "unit": "g"},
        {"name": "Non-dairy milk", "quantity": 50, "unit": "ml"},
        {"name": "Coconut oil", "quantity": 15, "unit": "ml"},
        {"name": "Vanilla extract", "quantity": 5, "unit": "ml"},
        {"name": "Blueberries", "quantity": 100, "unit": "g"},
        {"name": "Applesauce", "quantity": 50, "unit": "g"},
        {"name": "Maple syrup", "quantity": 50, "unit": "ml"},
        ],
    },
    {
    "name": "Vegan Pretzels",
    "calories": 330,
    "protein": 10,
    "carbs": 50,
    "fats": 8,
    "ingredients": [
        {"name": "Warm water", "quantity": 250, "unit": "ml"},
        {"name": "Vegan butter", "quantity": 30, "unit": "g"},
        {"name": "Baking soda", "quantity": 10, "unit": "g"},
        {"name": "Coarse salt", "quantity": 5, "unit": "g"},
        {"name": "All-purpose flour", "quantity": 200, "unit": "g"},
        {"name": "Vegan protein powder", "quantity": 50, "unit": "g"},
        {"name": "Yeast", "quantity": 5, "unit": "g"},
        {"name": "Sugar", "quantity": 10, "unit": "g"},
        {"name": "Salt", "quantity": 5, "unit": "g"},
        ],
    },
    {
    "name": "Vegan Cookie Mug Cake",
    "calories": 280,
    "protein": 10,
    "carbs": 30,
    "fats": 12,
    "ingredients": [
        {"name": "Almond flour", "quantity": 30, "unit": "g"},
        {"name": "Vegan protein powder", "quantity": 15, "unit": "g"},
        {"name": "Baking powder", "quantity": 5, "unit": "g"},
        {"name": "Salt", "quantity": 2, "unit": "g"},
        {"name": "Unsweetened almond milk", "quantity": 30, "unit": "ml"},
        {"name": "Coconut oil", "quantity": 15, "unit": "ml"},
        {"name": "Vanilla extract", "quantity": 5, "unit": "ml"},
        {"name": "Vegan chocolate chips", "quantity": 10, "unit": "g"},
        ],
    },
    {
    "name": "Tofu Scramble Burrito",
    "calories": 320,
    "protein": 26,
    "carbs": 32,
    "fats": 12,
    "ingredients": [
        {"name": "Firm tofu", "quantity": 200, "unit": "g"},
        {"name": "Onion", "quantity": 40, "unit": "g"},
        {"name": "Bell pepper", "quantity": 50, "unit": "g"},
        {"name": "Tomato", "quantity": 50, "unit": "g"},
        {"name": "Turmeric", "quantity": 5, "unit": "g"},
        {"name": "Whole wheat tortillas", "quantity": 50, "unit": "g"},
        ],
    },
    {
    "name": "Avocado Toast with Tempeh Bacon",
    "calories": 350,
    "protein": 12,
    "carbs": 32,
    "fats": 24,
    "ingredients": [
        {"name": "Whole grain bread", "quantity": 60, "unit": "g"},
        {"name": "Avocado", "quantity": 100, "unit": "g"},
        {"name": "Tempeh bacon", "quantity": 30, "unit": "g"},
        {"name": "Tomato", "quantity": 50, "unit": "g"},
        {"name": "Sprouts", "quantity": 10, "unit": "g"},
        {"name": "Salt", "quantity": 5, "unit": "g"},
        {"name": "Black pepper", "quantity": 5, "unit": "g"},
        ],
    },
    {
    "name": "Vegan Protein Bar",
    "calories": 450,
    "protein": 30,
    "carbs": 50,
    "fats": 15,
    "ingredients": [
        {"name": "Rolled oats", "quantity": 100, "unit": "g"},
        {"name": "Vegan protein powder", "quantity": 100, "unit": "g"},
        {"name": "Chopped nuts", "quantity": 30, "unit": "g"},
        {"name": "Dried fruit", "quantity": 30, "unit": "g"},
        {"name": "Cinnamon", "quantity": 5, "unit": "g"},
        {"name": "Salt", "quantity": 5, "unit": "g"},
        {"name": "Almond butter", "quantity": 50, "unit": "g"},
        {"name": "Maple syrup", "quantity": 50, "unit": "g"},
        {"name": "Water", "quantity": 50, "unit": "ml"},
        ],
    },
],
    "Lunch": [
        {
    "name": "Vegan Zucchini Lasagna",
    "calories": 450,
    "protein": 18,
    "carbs": 40,
    "fats": 22,
    "ingredients": [
        {"name": "Cashew nuts", "quantity": 300, "unit": "g"},
        {"name": "Tomatoes", "quantity": 500, "unit": "g"},
        {"name": "Leek", "quantity": 100, "unit": "g"},
        {"name": "Scallion", "quantity": 20, "unit": "g"},
        {"name": "Parsley", "quantity": 10, "unit": "g"},
        {"name": "Zucchini", "quantity": 300, "unit": "g"},
        ],
    },
    {
    "name": "Vegan Mushroom and Spinach Risotto",
    "calories": 420,
    "protein": 12,
    "carbs": 50,
    "fats": 15,
    "ingredients": [
        {"name": "Arborio rice", "quantity": 200, "unit": "g"},
        {"name": "Vegetable broth", "quantity": 800, "unit": "ml"},
        {"name": "Mushrooms", "quantity": 200, "unit": "g"},
        {"name": "Spinach", "quantity": 100, "unit": "g"},
        {"name": "Nutritional yeast", "quantity": 25, "unit": "g"},
        {"name": "Olive oil", "quantity": 30, "unit": "g"},
        {"name": "Vegan butter", "quantity": 10, "unit": "g"},
        ],
    },
    {
    "name": "Chickpea Salad with Grilled Tofu",
    "calories": 350,
    "protein": 25,
    "carbs": 20,
    "fats": 15,
    "ingredients": [
        {"name": "Chickpeas", "quantity": 150, "unit": "g"},
        {"name": "Tofu", "quantity": 200, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        {"name": "Parsley", "quantity": 5, "unit": "g"},
        ],
    },
    {
    "name": "Vegetable Stroganoff",
    "calories": 400,
    "protein": 18,
    "carbs": 45,
    "fats": 12,
    "ingredients": [
        {"name": "Onion", "quantity": 100, "unit": "g"},
        {"name": "Garlic", "quantity": 15, "unit": "g"},
        {"name": "Olive oil", "quantity": 15, "unit": "g"},
        {"name": "Tofu", "quantity": 100, "unit": "g"},
        {"name": "Carrot", "quantity": 100, "unit": "g"},
        {"name": "Broccoli", "quantity": 50, "unit": "g"},
        {"name": "Brown rice", "quantity": 150, "unit": "g"},
        ],
    },
    {
    "name": "Zucchini Spaghetti with Tofu Sauce",
    "calories": 300,
    "protein": 15,
    "carbs": 30,
    "fats": 10,
    "ingredients": [
        {"name": "Tomatoes", "quantity": 400, "unit": "g"},
        {"name": "Scallion", "quantity": 20, "unit": "g"},
        {"name": "Zucchini", "quantity": 200, "unit": "g"},
        {"name": "Garlic", "quantity": 15, "unit": "g"},
        {"name": "Tofu", "quantity": 100, "unit": "g"},
        ],
    },
    {
    "name": "Quinoa Salad with Grains and Veggies",
    "calories": 340,
    "protein": 14,
    "carbs": 45,
    "fats": 10,
    "ingredients": [
        {"name": "Quinoa", "quantity": 100, "unit": "g"},
        {"name": "Grains (e.g., beans, lentils, chickpeas)", "quantity": 100, "unit": "g"},
        {"name": "Parsley", "quantity": 5, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        ],
    },
    {
    "name": "Chickpea and Quinoa Wrap",
    "calories": 360,
    "protein": 18,
    "carbs": 50,
    "fats": 12,
    "ingredients": [
        {"name": "Chickpeas", "quantity": 150, "unit": "g"},
        {"name": "Quinoa", "quantity": 150, "unit": "g"},
        {"name": "Parsley", "quantity": 50, "unit": "g"},
        {"name": "Lemon juice", "quantity": 50, "unit": "g"},
        ],
    },
    {
    "name": "Stir-fry Tofu and Vegetables",
    "calories": 280,
    "protein": 20,
    "carbs": 18,
    "fats": 10,
    "ingredients": [
        {"name": "Tofu", "quantity": 200, "unit": "g"},
        {"name": "Mixed vegetables", "quantity": 100, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        {"name": "Soy sauce", "quantity": 50, "unit": "g"},
        ],
    },
    {
    "name": "Lentil Soup",
    "calories": 320,
    "protein": 22,
    "carbs": 40,
    "fats": 8,
    "ingredients": [
        {"name": "Onion", "quantity": 100, "unit": "g"},
        {"name": "Garlic", "quantity": 20, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        {"name": "Lentils", "quantity": 200, "unit": "g"},
        {"name": "Parsley", "quantity": 10, "unit": "g"},
        {"name": "Walnuts", "quantity": 50, "unit": "g"},
        ],
    },
    {
    "name": "Vegetable Soup",
    "calories": 250,
    "protein": 10,
    "carbs": 35,
    "fats": 5,
    "ingredients": [
        {"name": "Onion", "quantity": 100, "unit": "g"},
        {"name": "Garlic", "quantity": 20, "unit": "g"},
        {"name": "Carrot", "quantity": 100, "unit": "g"},
        {"name": "Tofu", "quantity": 50, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        ],
    },
    {
    "name": "Black Bean and Quinoa Salad",
    "calories": 340,
    "protein": 18,
    "carbs": 45,
    "fats": 12,
    "ingredients": [
        {"name": "Black beans", "quantity": 100, "unit": "g"},
        {"name": "Quinoa", "quantity": 100, "unit": "g"},
        {"name": "Parsley", "quantity": 50, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        {"name": "Balsamic vinegar", "quantity": 10, "unit": "g"},
        {"name": "Walnuts", "quantity": 50, "unit": "g"},
        ],
    },
    {
    "name": "Chickpea Dumplings",
    "calories": 370,
    "protein": 15,
    "carbs": 50,
    "fats": 10,
    "ingredients": [
        {"name": "Chickpeas", "quantity": 300, "unit": "g"},
        {"name": "Onion", "quantity": 100, "unit": "g"},
        {"name": "Garlic", "quantity": 10, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        {"name": "Chickpea flour", "quantity": 30, "unit": "g"},
        ],
    },
    {
    "name": "Brown Rice with Vegetables and Tofu",
    "calories": 380,
    "protein": 18,
    "carbs": 55,
    "fats": 8,
    "ingredients": [
        {"name": "Brown rice", "quantity": 200, "unit": "g"},
        {"name": "Tofu", "quantity": 100, "unit": "g"},
        {"name": "Garlic", "quantity": 15, "unit": "g"},
        {"name": "Olive oil", "quantity": 10, "unit": "g"},
        ],
    },
    {
    "name": "Chickpea and Broccoli Risotto",
    "calories": 350,
    "protein": 15,
    "carbs": 45,
    "fats": 12,
    "ingredients": [
        {"name": "Chickpeas", "quantity": 45, "unit": "g"},
        {"name": "Broccoli", "quantity": 75, "unit": "g"},
        {"name": "Onion", "quantity": 30, "unit": "g"},
        {"name": "Olive oil", "quantity": 30, "unit": "g"},
        {"name": "Oat flour", "quantity": 30, "unit": "g"},
        ],
    },
    {
    "name": "Whole Wheat Pasta with Vegetables",
    "calories": 420,
    "protein": 18,
    "carbs": 65,
    "fats": 10,
    "ingredients": [
        {"name": "Whole grain pasta", "quantity": 75, "unit": "g"},
        {"name": "Tempeh", "quantity": 45, "unit": "g"},
        {"name": "Onion", "quantity": 30, "unit": "g"},
        {"name": "Olive oil", "quantity": 30, "unit": "g"},
        ],
    },
    {
    "name": "Vegan Stuffed Bell Peppers",
    "calories": 350,
    "protein": 15,
    "carbs": 50,
    "fats": 10,
    "ingredients": [
        {"name": "Bell peppers", "quantity": 400, "unit": "g"},
        {"name": "Brown rice", "quantity": 100, "unit": "g"},
        {"name": "Black beans", "quantity": 150, "unit": "g"},
        {"name": "Onion", "quantity": 100, "unit": "g"},
        {"name": "Olive oil", "quantity": 30, "unit": "g"},
        {"name": "Avocado", "quantity": 200, "unit": "g"},
        ],
    },
    {
    "name": "Sweet Potato and Black Bean Bowl",
    "calories": 400,
    "protein": 12,
    "carbs": 55,
    "fats": 10,
    "ingredients": [
        {"name": "Sweet potato", "quantity": 200, "unit": "g"},
        {"name": "Black beans", "quantity": 150, "unit": "g"},
        {"name": "Quinoa", "quantity": 50, "unit": "g"},
        {"name": "Parsley", "quantity": 5, "unit": "g"},
        {"name": "Salsa", "quantity": 100, "unit": "g"},
        ],
    },
    {
    "name": "Heart of Palm Stroganoff",
    "calories": 350,
    "protein": 10,
    "carbs": 45,
    "fats": 12,
    "ingredients": [
        {"name": "Heart of palm", "quantity": 300, "unit": "g"},
        {"name": "Garlic", "quantity": 20, "unit": "g"},
        {"name": "Olive oil", "quantity": 20, "unit": "g"},
        {"name": "Onion", "quantity": 100, "unit": "g"},
        {"name": "Mustard", "quantity": 30, "unit": "g"},
        ],
    },
    {
    "name": "Mushroom Ramen",
    "calories": 400,
    "protein": 15,
    "carbs": 50,
    "fats": 10,
    "ingredients": [
        {"name": "Mushrooms", "quantity": 200, "unit": "g"},
        {"name": "Tofu", "quantity": 100, "unit": "g"},
        {"name": "Sesame oil", "quantity": 10, "unit": "g"},
        {"name": "Garlic", "quantity": 10, "unit": "g"},
        {"name": "Ginger", "quantity": 10, "unit": "g"},
        {"name": "Miso rice", "quantity": 20, "unit": "g"},
        {"name": "Yakisoba noodles", "quantity": 100, "unit": "g"},
        ],
    },
    {
    "name": "Rice and Beans Bowl with Avocado",
    "calories": 350,
    "protein": 10,
    "carbs": 50,
    "fats": 10,
    "ingredients": [
        {"name": "Brown rice", "quantity": 50, "unit": "g"},
        {"name": "Black beans", "quantity": 50, "unit": "g"},
        {"name": "Avocado", "quantity": 100, "unit": "g"},
        {"name": "Carrot", "quantity": 50, "unit": "g"},
        {"name": "Tomato", "quantity": 50, "unit": "g"},
        {"name": "Olive oil", "quantity": 15, "unit": "g"},
            ],
        },
    ],
}

# Links para imagens de categorias
category_images = {
    "Smoothies": "https://cdn.pixabay.com/photo/2019/01/12/16/20/chia-3928799_1280.jpg",
    "Snacks": "https://cdn.pixabay.com/photo/2020/02/09/12/45/vegan-4833041_960_720.jpg",
    "Lunch": "https://cdn.pixabay.com/photo/2022/03/27/15/09/gourmet-7095380_1280.jpg",
}

# Função para calcular a TMB e as calorias ajustadas
def calculate_calories_and_macros(weight, height, age, gender, goal):
    if gender == "Male":
        tmb = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:  # Female
        tmb = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    # Ajustar calorias de acordo com o objetivo
    if goal == "Lose Weight":
        calories = tmb * 0.85
        macro_distribution = {"protein": 0.4, "carbs": 0.4, "fats": 0.2}
    elif goal == "Maintain Weight":
        calories = tmb
        macro_distribution = {"protein": 0.3, "carbs": 0.4, "fats": 0.3}
    elif goal == "Gain Muscle":
        calories = tmb * 1.15
        macro_distribution = {"protein": 0.25, "carbs": 0.5, "fats": 0.25}
    else:
        raise ValueError("Unknown goal provided.")

    return calories, macro_distribution

# Ajustar a receita para considerar a proporção das calorias diárias
def adjust_recipe(recipe, user_calories, macro_distribution, category):
    # Calcular as calorias alocadas para esta categoria
    category_proportion = meal_proportions.get(category, 0.1)  # Default: 10%
    allocated_calories = user_calories * category_proportion

    # Calcular os macronutrientes ajustados
    protein_calories = allocated_calories * macro_distribution["protein"]
    carbs_calories = allocated_calories * macro_distribution["carbs"]
    fats_calories = allocated_calories * macro_distribution["fats"]

    # Cada grama de proteína e carboidrato tem 4 kcal, e cada grama de gordura tem 9 kcal
    protein_target = protein_calories / 4
    carbs_target = carbs_calories / 4
    fats_target = fats_calories / 9

    # Ajustar a escala dos ingredientes
    scale_factor = allocated_calories / recipe["calories"]
    adjusted_ingredients = [
        {
            "name": ingredient["name"],
            "quantity": round(ingredient["quantity"] * scale_factor, 2),
            "unit": ingredient["unit"],
        }
        for ingredient in recipe["ingredients"]
    ]

    adjusted_nutrition = {
        "calories": round(recipe["calories"] * scale_factor),
        "protein": round(recipe["protein"] * scale_factor, 2),
        "carbs": round(recipe["carbs"] * scale_factor, 2),
        "fats": round(recipe["fats"] * scale_factor, 2),
    }

    return adjusted_ingredients, adjusted_nutrition, protein_target, carbs_target, fats_target

# Atualizar cores com base no tema claro/escuro
def get_theme_colors():
    return {
        "background": PALETTE["background_dark"] if is_dark_mode["enabled"] else PALETTE["background_light"],
        "text": PALETTE["text_light"] if is_dark_mode["enabled"] else PALETTE["text_dark"],
        "button_bg": PALETTE["button_bg"],
        "button_text": PALETTE["button_text"],
    }

# Função para criar botões estilizados
def styled_button(text, on_click, bgcolor, text_color, hover_bgcolor=None):
    button = ft.ElevatedButton(
        text,
        on_click=on_click,
        bgcolor=bgcolor,
        color=text_color,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
            elevation=5,
        ),
    )

    # Adiciona a funcionalidade de mudança de cor ao passar o mouse
    def on_hover(e):
        button.bgcolor = hover_bgcolor if e.data == "true" else bgcolor
        button.update()

    if hover_bgcolor:
        button.on_hover = on_hover

    return button

# Função principal
def main(page: ft.Page):
    page.title = "ChefMaker"
    page.scroll = "auto"
    page.padding = 10

    # Alternar entre modo claro e escuro
    def toggle_dark_mode(e):
        is_dark_mode["enabled"] = not is_dark_mode["enabled"]
        theme_colors = get_theme_colors()
        page.bgcolor = theme_colors["background"]
        page.update()

    # Página inicial
    def home_page():
        theme_colors = get_theme_colors()

        weight_field = ft.TextField(label="Weight (kg)", value=user_data["weight"], width=300)
        height_field = ft.TextField(label="Height (cm)", value=user_data["height"], width=300)
        age_field = ft.TextField(label="Age", value=user_data["age"], width=300)
        gender_dropdown = ft.Dropdown(
            label="Gender",
            value=user_data["gender"],
            options=[
                ft.dropdown.Option("Male"),
                ft.dropdown.Option("Female"),
            ],
        )
        goal_dropdown = ft.Dropdown(
            label="Goal",
            value=user_data["goal"],
            options=[
                ft.dropdown.Option("Lose Weight"),
                ft.dropdown.Option("Maintain Weight"),
                ft.dropdown.Option("Gain Muscle"),
            ],
        )

        def save_user_data_and_continue(e):
            try:
                user_data["weight"] = float(weight_field.value)
                user_data["height"] = float(height_field.value)
                user_data["age"] = int(age_field.value)
                user_data["gender"] = gender_dropdown.value
                user_data["goal"] = goal_dropdown.value
                save_user_data()
                navigate_to_categories()
            except ValueError as err:
                page.dialog = ft.AlertDialog(
                    title=ft.Text("Invalid Input"),
                    content=ft.Text("Please ensure all fields are filled correctly."),
                    actions=[ft.TextButton("OK", on_click=lambda _: page.dialog.close())],
                )
                page.dialog.open = True
                page.update()

        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        [
                            ft.Text("ChefMaker", size=30, weight="bold", color=theme_colors["text"]),
                            ft.IconButton(
                                icon=ft.icons.DARK_MODE if is_dark_mode["enabled"] else ft.icons.LIGHT_MODE,
                                on_click=toggle_dark_mode,
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Text("Enter your details to personalize your experience.", size=18, color=theme_colors["text"]),
                    ft.Divider(),
                    weight_field,
                    height_field,
                    age_field,
                    gender_dropdown,
                    goal_dropdown,
                    styled_button(
                        "Continue",
                        on_click=save_user_data_and_continue,
                        bgcolor=theme_colors["button_bg"],
                        text_color=theme_colors["button_text"],
                        hover_bgcolor=PALETTE["primary"],
                    ),
                ],
                scroll="adaptive",
                bgcolor=theme_colors["background"],
            )
        )
        page.update()

    # Navegar para categorias
    def navigate_to_categories():
        theme_colors = get_theme_colors()

        grid = ft.GridView(
            expand=1,
            runs_count=2,
            max_extent=350,
            child_aspect_ratio=1,
            spacing=20,
        )

        for category, image_url in category_images.items():
            def explore_category_handler(category):
                return lambda e: show_recipes(e, category)

            grid.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(
                                    src=image_url,
                                    width=300,
                                    height=200,
                                    fit=ft.ImageFit.COVER,
                                ),
                                ft.Text(category, size=24, weight="bold", color=theme_colors["text"]),
                                styled_button(
                                    "Explore",
                                    on_click=explore_category_handler(category),
                                    bgcolor=theme_colors["button_bg"],
                                    text_color=theme_colors["button_text"],
                                    hover_bgcolor=PALETTE["primary"],
                                ),
                            ],
                            horizontal_alignment="center",
                            alignment="center",
                        ),
                        padding=10,
                        bgcolor=PALETTE["secondary"],
                        border_radius=15,
                        alignment=ft.alignment.center,
                    ),
                )
            )

        explanation_text = ft.Column(
            [
                ft.Text(
                    "Welcome to Muscle Meals",
                    size=24,
                    weight="bold",
                    color=theme_colors["text"],
                ),
                ft.Text(
                    "Here are the 60 recipes you acquired with the Muscle Meals eBook. Each recipe is personalized to match your unique nutritional needs and goals.",
                    size=18,
                    color=theme_colors["text"],
                ),
                ft.Divider(),
                ft.Text(
                    "How it works:",
                    size=20,
                    weight="bold",
                    color=theme_colors["text"],
                ),
                ft.ListView(
                    controls=[
                        ft.Text(
                            "• Each recipe is adjusted to provide calories based on a balanced daily meal plan: snacks are ~10%, lunch ~30%, etc.",
                            size=16,
                            color=theme_colors["text"],
                        ),
                        ft.Text(
                            "• Recipes differ in ingredients, nutrients, and flavors while still aligning with your caloric needs.",
                            size=16,
                            color=theme_colors["text"],
                        ),
                        ft.Text(
                            "• Protein, carbs, and fats are tailored to your goal: weight loss, maintenance, or muscle gain.",
                            size=16,
                            color=theme_colors["text"],
                        ),
                    ],
                    spacing=10,
                ),
                ft.Divider(),
            ],
            spacing=20,
        )

        page.views.append(
            ft.View(
                "/categories",
                [
                    ft.Row(
                        [
                            ft.Text("Categories", size=30, weight="bold", color=theme_colors["text"]),
                            ft.IconButton(
                                icon=ft.icons.DARK_MODE if is_dark_mode["enabled"] else ft.icons.LIGHT_MODE,
                                on_click=toggle_dark_mode,
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    explanation_text,
                    grid,
                    styled_button(
                        "Back to Home",
                        on_click=lambda _: home_page(),
                        bgcolor=theme_colors["button_bg"],
                        text_color=theme_colors["button_text"],
                        hover_bgcolor=PALETTE["primary"],
                    ),
                ],
                scroll="adaptive",
                bgcolor=theme_colors["background"],
            )
        )
        page.update()

    # Mostrar receitas de uma categoria
    def show_recipes(e, category):
        theme_colors = get_theme_colors()

        grid = ft.GridView(expand=1, runs_count=1, max_extent=400, spacing=20)

        for recipe in recipes[category]:
            def view_ingredients_handler(recipe):
                return lambda e: show_ingredients(category, recipe)

            grid.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(recipe["name"], size=20, weight="bold", color=theme_colors["text"]),
                                ft.Text(f"Calories: {recipe['calories']} kcal", color=theme_colors["text"]),
                                ft.Text(f"Protein: {recipe['protein']} g", color=theme_colors["text"]),
                                ft.Text(f"Carbs: {recipe['carbs']} g", color=theme_colors["text"]),
                                ft.Text(f"Fats: {recipe['fats']} g", color=theme_colors["text"]),
                                styled_button(
                                    "View Ingredients",
                                    on_click=view_ingredients_handler(recipe),
                                    bgcolor=theme_colors["button_bg"],
                                    text_color=theme_colors["button_text"],
                                    hover_bgcolor=PALETTE["primary"],
                                ),
                            ],
                            alignment="start",
                        ),
                        padding=10,
                        bgcolor=PALETTE["accent"],
                        border_radius=10,
                    ),
                )
            )

        page.views.append(
            ft.View(
                f"/categories/{category}",
                [
                    ft.Row(
                        [
                            ft.Text(f"{category} Recipes", size=30, weight="bold", color=theme_colors["text"]),
                            ft.IconButton(
                                icon=ft.icons.DARK_MODE if is_dark_mode["enabled"] else ft.icons.LIGHT_MODE,
                                on_click=toggle_dark_mode,
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    grid,
                    styled_button(
                        "Back to Categories",
                        on_click=lambda _: navigate_to_categories(),
                        bgcolor=theme_colors["button_bg"],
                        text_color=theme_colors["button_text"],
                        hover_bgcolor=PALETTE["primary"],
                    ),
                ],
                scroll="adaptive",
                bgcolor=theme_colors["background"],
            )
        )
        page.update()

    # Mostrar ingredientes de uma receita
    def show_ingredients(category, recipe):
        theme_colors = get_theme_colors()

        try:
            weight = float(user_data["weight"])
            height = float(user_data["height"])
            age = int(user_data["age"])
            gender = user_data["gender"]
            goal = user_data["goal"]

            # Calcular calorias e macronutrientes com base no objetivo
            user_calories, macro_distribution = calculate_calories_and_macros(weight, height, age, gender, goal)

            # Ajustar receita com base na proporção da categoria
            adjusted_ingredients, adjusted_nutrition, protein_target, carbs_target, fats_target = adjust_recipe(
                recipe, user_calories, macro_distribution, category
            )
        except Exception as err:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(f"An error occurred while processing: {err}"),
                actions=[ft.TextButton("OK", on_click=lambda _: page.dialog.close())],
            )
            page.dialog.open = True
            page.update()
            return

        # Mostrar dados ajustados na interface
        ingredients_list = ft.Column(
            [
                ft.Text(f"{ingredient['name']}: {ingredient['quantity']} {ingredient['unit']}")
                for ingredient in adjusted_ingredients
            ]
        )

        page.views.append(
            ft.View(
                f"/ingredients/{recipe['name']}",
                [
                    ft.Row(
                        [
                            ft.Text(f"Ingredients for {recipe['name']}", size=24, weight="bold", color=theme_colors["text"]),
                            ft.IconButton(
                                icon=ft.icons.DARK_MODE if is_dark_mode["enabled"] else ft.icons.LIGHT_MODE,
                                on_click=toggle_dark_mode,
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Text(
                        f"This recipe has been adjusted for your caloric and macronutrient needs.",
                        size=16,
                        italic=True,
                        color=PALETTE["secondary"],
                    ),
                    ft.Text(f"Adjusted Nutrition:", size=20, weight="bold", color=theme_colors["text"]),
                    ft.Text(f"- Calories: {adjusted_nutrition['calories']} kcal", color=theme_colors["text"]),
                    ft.Text(f"- Protein: {adjusted_nutrition['protein']} g (Target: {round(protein_target, 2)} g)", color=theme_colors["text"]),
                    ft.Text(f"- Carbs: {adjusted_nutrition['carbs']} g (Target: {round(carbs_target, 2)} g)", color=theme_colors["text"]),
                    ft.Text(f"- Fats: {adjusted_nutrition['fats']} g (Target: {round(fats_target, 2)} g)", color=theme_colors["text"]),
                    ft.Divider(),
                    ft.Text("Ingredients:", size=20, weight="bold", color=theme_colors["text"]),
                    ingredients_list,
                    styled_button(
                        "Back to Recipes",
                        on_click=lambda _: show_recipes(None, category),
                        bgcolor=theme_colors["button_bg"],
                        text_color=theme_colors["button_text"],
                        hover_bgcolor=PALETTE["primary"],
                    ),
                ],
                scroll="adaptive",
                bgcolor=theme_colors["background"],
            )
        )
        page.update()

    # Configuração inicial
    theme_colors = get_theme_colors()
    page.bgcolor = theme_colors["background"]
    page.on_route_change = lambda _: home_page()
    page.go("/")

import os
port = int(os.environ.get("PORT", 8080))  # O Render fornece a variável PORT
ft.app(target=main, view="web_browser", host="0.0.0.0", port=port)

