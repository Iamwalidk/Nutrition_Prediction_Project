# Nutrition_Prediction_Project
This repo has a machine learning model and a Flask app that predicts Calories, Protein, Carbs, and Fat for foods. It uses data cleaning, text preprocessing (lemmatization), and either RandomForest or XGBoost. The user can enter a food name in the web interface to view estimated nutritional values.

File structue:
my_nutrition_app/
├── text_utils.py           
├── best_model_rf.ipynb     
├── nutrition_model.pkl     
├── app.py                 
├── templates/
│   └── index.html          
└── static/
    ├── css/style.css      
    └── js/main.js          


How to use:
1. Download or Clone this repository to your computer.
2. Install Python (if not already installed).
3. Open a Terminal (or Command Prompt) in the project folder and run:

pip install -r requirements.txt

4. Start the App by typing:

python app.py
5.Open Your Browser and go to http://127.0.0.1:5000.
6.Enter a Food Name (like “apple”) and click “Predict” to see estimated Calories, Protein, Carbs, and Fat.
