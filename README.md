# Car Max Speed Prediction

A machine learning project that predicts a car's maximum speed based on its technical specifications. The project combines statistical analysis, data preprocessing, Random Forest Regression, and a Flask web application to provide speed predictions through a simple web interface.

## Project Overview

The goal is to estimate a vehicle's maximum speed using features such as engine capacity, number of cylinders, horsepower, torque, dimensions, drive type, transmission, and fuel type.

The project includes exploratory data analysis, outlier treatment, feature analysis, model training, and deployment through Flask.

## Technologies

* **Python**
* **Data Analysis:** Pandas, NumPy
* **Statistical Analysis:** Statsmodels
* **Machine Learning:** Scikit-learn, Random Forest Regressor
* **Web Framework:** Flask
* **Frontend:** HTML, CSS
* **Development:** Jupyter Notebook

## Project Structure

```text
car_max_speed_project/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── project1.ipynb
├── project1.csv
├── rf_model.pkl
├── scaler.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

## Workflow

### 1. Data Analysis

Explored the vehicle dataset to understand the available features and their relationships with maximum speed.

### 2. Data Preprocessing

* Analyzed the dataset for outliers and removed selected outlier observations.
* Examined feature relationships and statistical properties.
* Prepared numerical and categorical features for model training.

### 3. Feature Analysis

Used statistical analysis with Statsmodels to investigate feature relationships and support feature selection.

### 4. Model Training

Trained a `RandomForestRegressor` to predict maximum vehicle speed from technical specifications.

The numerical features are scaled using a fitted scaler, and the trained model and scaler are saved as serialized artifacts for use by the web application.

### 5. Model Evaluation

The model achieved the following reported results:

| Metric                    | Result |
| ------------------------- | -----: |
| Mean Absolute Error (MAE) |  1.407 |
| R² Score                  |   0.98 |

The MAE indicates an average absolute prediction error of approximately **1.407 km/h**, assuming the target variable is measured in km/h.

The R² score of 0.98 indicates that the model explains approximately 98% of the variance in maximum speed on the evaluated dataset.

### 6. Web Application

The Flask application allows users to enter vehicle specifications and receive:

* Predicted maximum speed in km/h.
* A feasibility assessment based on predefined vehicle specifications and speed thresholds.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/car_max_speed_project.git
cd car_max_speed_project
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Ensure that `rf_model.pkl` and `scaler.pkl` are present in the project root, then run:

```bash
python app.py
```

Open the local address displayed in the terminal in your browser.

## Limitations

* Predictions depend on the quality and coverage of the training dataset.
* The feasibility assessment uses predefined thresholds and should not be interpreted as a comprehensive engineering safety evaluation.
* Reported model metrics depend on the evaluation methodology and dataset split.

## Future Improvements

* Validate model performance on an independent test dataset.
* Compare Random Forest with other regression algorithms.
* Add input validation and more detailed prediction explanations.
* Improve the feasibility assessment using domain-specific vehicle specifications.
## Prediction and Feasibility Check

The application provides two main outputs:

**1. Maximum Speed Prediction**

A trained Random Forest Regressor predicts the vehicle's maximum speed based on its technical specifications, including engine capacity, horsepower, torque, dimensions, drive type, transmission, and fuel type.

**2. Feasibility Check**

In addition to predicting maximum speed, the application evaluates whether the submitted vehicle specifications and predicted speed fall within predefined thresholds.

The result is classified as:

* **Realistic** — the input specifications and predicted speed satisfy the implemented threshold checks.
* **Unrealistic** — at least one specification or the predicted speed exceeds the defined limits.

This additional validation helps flag potentially implausible inputs or predictions.

**Note:** The feasibility check uses predefined thresholds. It is a rule-based validation mechanism, not an independent engineering assessment of a vehicle's actual capabilities or safety.
