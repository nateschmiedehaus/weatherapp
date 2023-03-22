import pandas as pd
import numpy as np
import requests
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for, flash
from flask import Flask, render_template


def get_shopify_data(api_key, password, store_name):
    shopify_url = f'https://{store_name}.myshopify.com/admin/api/2021-09/orders.json'
    shopify_headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': f'{api_key}:{password}'}
    shopify_response = requests.get(shopify_url, headers=shopify_headers)
    return shopify_response.json()

def get_weather_data(api_key, lat, lon):
    weather_url = f'https://api.weather.gov/points/{lat},{lon}/forecast/hourly'
    weather_headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json', 'Authorization': f'{api_key}'}
    weather_response = requests.get(weather_url, headers=weather_headers)
    return weather_response.json()

def get_facebook_data(access_token, account_id):
    facebook_url = f'https://graph.facebook.com/v13.0/{account_id}/insights?fields=cost_per_inline_post_engagement,cost_per_inline_link_click,cost_per_unique_click,cost_per_action_type,actions,cpc,cpm,cpp&access_token={access_token}'
    facebook_response = requests.get(facebook_url)
    return facebook_response.json()

def create_state_regression_models(combined_data):
    # Create regression models for each state and the top 20 metro areas
    # This function should be implemented based on the structure of the preprocessed data
    pass


def combine_data(shopify_data, weather_data, facebook_data):
    combined_data = pd.DataFrame() # Create an empty DataFrame to store the combined data

    # Extract relevant data from the Shopify, Weather, and Facebook data and add it to the combined_data DataFrame
    # This process may vary depending on the structure of the data returned by the APIs

    return combined_data

def authenticate(email, password):
    return email == 'user@example.com' and password == 'password'


def create_regression_model(combined_data):
    # Prepare the input and output data for the regression model
    X = combined_data.drop("target_variable", axis=1) # Replace "target_variable" with the name of the variable you want to predict
    y = combined_data["target_variable"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Test the model on the test data
    y_pred = model.predict(X_test)

    # Evaluate the performance of the model (e.g., using R-squared, mean squared error, etc.)

    return model


def generate_state_outputs(state_models):
    # Generate a CSV and graphical representation for each state
    # This function should be implemented using appropriate libraries (e.g., matplotlib for graphs)
    pass

def predict_outcomes(state_models, ad_spend_allocation):
    # Predict conversion rates and total orders based on the recommended Facebook ad spend allocation
    # This function should be implemented based on the structure of the state regression models
    pass


def analyze_seasonality(state_models):
    # Analyze seasonality and identify bad times to advertise in each state
    # This function should be implemented based on the structure of the state regression models
    pass

#step9
def preprocess_data(shopify_data, weather_data, facebook_data):
    # Preprocess the data: combine by state, factor out weather, and incorporate Facebook ad data
    # This function should be implemented based on the structure of the data returned by the APIs
    pass

def adjust_ad_spend(state_models, increase_pct, decrease_pct):
    # Automatically increase, decrease, or stop ad spend for a given state's ad set based on weather information
    # Implement this function based on the structure of the state regression models and the provided percentages
    pass

#step #8
app = Flask(__name__)

@app.route("/")
def home():
    # Render the home page with options to view state models, manage Facebook ad accounts, and handle third-party payments
    pass


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if authenticate(email, password):
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid email or password')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    # Here, you can display relevant models/accounts for the logged-in user
    
    @app.route('/dashboard')
def dashboard():
    # Replace these values with your actual data
    model_accuracy = 90
    mean_squared_error = 0.05
    rmse = 0.1
    predicted_value = 100
    actual_value = 105

    return render_template('dashboard.html', model_accuracy=model_accuracy, mean_squared_error=mean_squared_error, rmse=rmse, predicted_value=predicted_value, actual_value=actual_value)

    
    pass


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect user inputs (e.g., API keys, location,
        # Collect user inputs (e.g., API keys, location, etc.) from the form on the web page
        # Replace "form_field_name" with the actual names of the form fields
        api_key_shopify = request.form["form_field_name_shopify_api_key"]
        password_shopify = request.form["form_field_name_shopify_password"]
        store_name_shopify = request.form["form_field_name_shopify_store_name"]
        api_key_weather = request.form["form_field_name_weather_api_key"]
        lat_weather = request.form["form_field_name_weather_lat"]
        lon_weather = request.form["form_field_name_weather_lon"]
        access_token_facebook = request.form["form_field_name_facebook_access_token"]
        account_id_facebook = request.form["form_field_name_facebook_account_id"]

        # Get data from Shopify, Weather.gov, and Facebook using the provided API keys and other inputs
        shopify_data = get_shopify_data(api_key_shopify, password_shopify, store_name_shopify)
        weather_data = get_weather_data(api_key_weather, lat_weather, lon_weather)
        facebook_data = get_facebook_data(access_token_facebook, account_id_facebook)

        # Combine the data and create a regression model
        combined_data = combine_data(shopify_data, weather_data, facebook_data)
        model = create_regression_model(combined_data)

        # Use the model to make predictions (if necessary)

        # Pass the data and/or predictions to the web page template to display them
        return render_template("index.html", data=combined_data)  # Replace "index.html" with the name of your template file and "data" with the variable(s) you want to pass

    # Render the initial web page with the input form
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        new_user = User(username=username, email=email, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/api/metrics')
def metrics():
    return {'mse': mse, 'rmse': rmse, 'r2': r2}


# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key' # Replace 'your-secret-key' with a strong secret key

# Initialize the database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Create a User model for the database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create the database tables
db.create_all()


