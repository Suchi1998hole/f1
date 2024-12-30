# from flask import Flask, render_template, request
# import pandas as pd
# from f1 import process_predictions  # Import your function from f1.py

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get inputs from the form
#         round_input = int(request.form['round'])
#         year_input = int(request.form['year'])

#         # Call the process_predictions function
#         predictions_df = process_predictions(round_input, year_input)

#         # Convert the DataFrame to HTML for display
#         predictions_html = predictions_df.to_html(classes='table table-striped')
#         return render_template('result.html', table=predictions_html)
#     except Exception as e:
#         return f"An error occurred: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import pandas as pd
from f1 import process_predictions  # Import your function from f1.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from the form
        round_input = int(request.form['round'])
        year_input = int(request.form['year'])

        # Call the process_predictions function
        predictions_df = process_predictions(round_input, year_input)

        # Filter to show only top 3 podium finishers with selected columns
        podium_df = predictions_df[predictions_df['Top_3_Finish_Prediction'] == 1]
        podium_df = podium_df[['driverId', 'year', 'round', 'constructorId']].head(3)
        podium_df.rename(columns={
            'driverId': 'Driver Name',
            'year': 'Year',
            'round': 'Round',
            'constructorId': 'Constructor Name'
        }, inplace=True)

        # Convert the DataFrame to HTML for display
        predictions_html = podium_df.to_html(classes='table table-striped', index=False)
        return render_template('result.html', table=predictions_html)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)

