from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import re
import nltk
from nltk.stem import WordNetLemmatizer

synonyms = {
    'apples': 'apple',
    'bananas': 'banana',
    'tomatoes': 'tomato',
    'strawberries': 'strawberry',
    'blueberries': 'blueberry',
    'oranges': 'orange',
    'potatoes': 'potato',
    'carrots': 'carrot',
    'broccolis': 'broccoli',
    'grapes': 'grape',
    'peaches': 'peach',
    'mangoes': 'mango',
    'pineapples': 'pineapple',
    'watermelons': 'watermelon',
    'lemons': 'lemon',
    'limes': 'lime',
    'cherries': 'cherry',
    'pears': 'pear',
    'avocados': 'avocado',
    'cucumbers': 'cucumber',
    'bell peppers': 'pepper',
    'peppers': 'pepper',
    'mushrooms': 'mushroom',
    'zucchinis': 'zucchini',
    'onions': 'onion',
    'garlics': 'garlic',
    'eggs': 'egg',
    'breads': 'bread',
    'pizzas': 'pizza',
    'burgers': 'burger',
    'sandwiches': 'sandwich',
    'cookies': 'cookie',
    'cakes': 'cake',
    'pies': 'pie',
    'lettuces': 'lettuce',
    'cabbages': 'cabbage',
    'celeries': 'celery',
    'sausages': 'sausage',
    'steaks': 'steak',
    'noodles': 'noodle',
    'beans': 'bean',
    'lentils': 'lentil',
    'oats': 'oat',
    'cereals': 'cereal',
    'cheeses': 'cheese',
    'yogurts': 'yogurt',
    'butters': 'butter',
    'salads': 'salad',
    'soups': 'soup',
    'stews': 'stew',
    'chicken breasts': 'chicken breast',
    'chicken legs': 'chicken leg',
    'pork chops': 'pork chop',
    'beef steaks': 'beef steak'
}

def replace_synonyms(text, synonyms_dict):
    for word, replacement in synonyms_dict.items():
        text = re.sub(r'\b' + re.escape(word) + r'\b', replacement, text)
    return text

def lemmatize_text(text):
    text = text.lower()
    text = replace_synonyms(text, synonyms)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lem_tokens = [lemmatizer.lemmatize(tok) for tok in tokens]
    return ' '.join(lem_tokens)

app = Flask(__name__)

# Loading the trainged model
with open('nutrition_model.pkl', 'rb') as f:
    model = pickle.load(f)

numeric_cols = ['Calories', 'Protein', 'Fat', 'Carbs']


def predict_nutrition(product_name, model):
    default_category = "Fruits"  
    default_measure = "1 medium"
    default_grams = 100

    row = pd.DataFrame({
        'Food': [product_name],
        'Category': [default_category],
        'Measure': [default_measure],
        'name_length': [len(product_name)],
        'Grams': [default_grams]
    })

    preds = model.predict(row)
    result = dict(zip(numeric_cols, preds[0]))

    return result


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    product_name = data.get('product_name', '').strip()

    if not product_name:
        return jsonify({'error': 'No product name provided.'}), 400

    results = predict_nutrition(product_name, model)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
