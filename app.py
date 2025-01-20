import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the pre-trained model from a pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the form
        hours_studied = float(request.form.get('hours_studied'))
        previous_scores = float(request.form.get('previous_scores'))
        extracurricular = 1 if request.form.get('extracurricular').strip().lower() == 'yes' else 0
        sleep_hours = float(request.form.get('sleep_hours'))
        sample_papers = int(request.form.get('sample_papers'))

        # Prepare the input for the model
        input_data = [[hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers]]

        # Make a prediction
        prediction = model.predict(input_data)[0]

        # Define performance categories
        if prediction < 10:
            performance = "VERY BAD"
        elif 10 <= prediction < 50:
            performance = "BELOW AVERAGE"
        elif 50 <= prediction < 80:
            performance = "AVERAGE"
        elif 80 <= prediction < 90:
            performance = "GOOD"
        elif 90 <= prediction < 100:
            performance = "VERY GOOD"
        else:
            performance = "THE BEST 🎉🎊"

        # Render the result.html with the prediction
        return render_template('result.html', prediction=f"The predicted performance is: {performance}")
    except Exception as e:
        return render_template('result.html', prediction=f"Error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
