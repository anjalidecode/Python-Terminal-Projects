import json
import os

FILE = "recipes.json"

# Load recipes
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        recipes = json.load(f)
else:
    recipes = {}

def save_recipes():
    with open(FILE, "w") as f:
        json.dump(recipes, f)

while True:
    print("\n🍲 Recipe Book")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. View Recipe Details")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ")
        steps = input("Enter cooking steps: ")

        recipes[name] = {
            "ingredients": ingredients,
            "steps": steps
        }

        save_recipes()
        print("✅ Recipe added")

    elif choice == "2":
        if not recipes:
            print("No recipes found")
        else:
            for recipe in recipes:
                print("-", recipe)

    elif choice == "3":
        name = input("Enter recipe name: ")
        if name in recipes:
            print("\nIngredients:", recipes[name]["ingredients"])
            print("Steps:", recipes[name]["steps"])
        else:
            print("❌ Recipe not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
