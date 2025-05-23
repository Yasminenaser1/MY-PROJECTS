🧪 Reggie's Linear Regression
Reggie is a mad scientist hired to optimize a fast food restaurant's ball pit. He's experimenting with how the size of a bouncy ball affects how high it bounces, and needs help analyzing the data. This project implements a simple linear regression model in Python to find the line of best fit for Reggie’s data.

📌 Project Summary
This project walks through the process of:

Defining a linear equation of the form y = mx + b

Calculating how far off a data point is from the predicted value (error)

Iterating through many possible lines to find the one with the smallest total error

Using the best-fitting line to make predictions

📊 Dataset
The dataset is a list of 2D points representing ball width and bounce height:

python
Copy
Edit
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
Each tuple represents a ball's:

x: width in centimeters

y: bounce height in meters

🚀 What I Built
get_y(m, b, x): Returns the predicted y-value from a given line.

calculate_error(m, b, point): Returns the vertical error between the point and the line.

calculate_all_error(m, b, points): Calculates the total error of a line across all data points.

Brute-force Search: Tries multiple slope (m) and intercept (b) combinations to find the best-fitting line with the lowest total error.

Prediction: Uses the best-fitting line to predict the bounce height for a ball of width 6 cm.

✅ Final Result
Best fit line: y = 0.4x + 1.6

Total error: 5.0

Prediction for a 6cm ball: 4.0m bounce height

🛠️ Tech Used
Python 3

Jupyter Notebook (optional)

No external libraries—pure Python

📚 What I Learned
Fundamentals of linear regression

How to implement basic machine learning logic manually

Brute-force optimization techniques

Using loops, conditionals, and functions effectively

🔍 How to Run
Download the project files or copy the code into a Python IDE or Jupyter Notebook.

Run the script to see the best-fitting line and prediction output.

