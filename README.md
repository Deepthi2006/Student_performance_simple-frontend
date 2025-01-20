

# **Student Performance Prediction**

This is a Flask-based web application that predicts a student's performance based on various input factors such as study hours, previous scores, extracurricular activities, sleep hours, and practice question attempts. The application uses a pre-trained machine learning model (`model.pkl`) to generate predictions.

---

## **Features**
- A user-friendly interface to input student details.
- Predicts performance categories such as:
  - **VERY BAD**
  - **BELOW AVERAGE**
  - **AVERAGE**
  - **GOOD**
  - **VERY GOOD**
  - **THE BEST 🎉🎊**
- Clear results displayed on the result page.

---

## **Tech Stack**
- **Backend:** Flask
- **Frontend:** HTML
- **Machine Learning Model:** Pre-trained model saved as `model.pkl`

---

## **How to Run Locally**

### Prerequisites
1. Python 3.8 or above
2. Flask
3. Pickle (for the pre-trained model)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-performance-prediction.git
   cd student-performance-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the pre-trained model file (`model.pkl`) in the root directory of the project.
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/index
   ```

---

## **Project Structure**
```
student-performance-prediction/
├── app.py                  # Flask application code
├── model.pkl               # Pre-trained ML model
├── templates/
│   ├── index.html          # Input form page
│   ├── result.html         # Result display page
├── static/                 # (Optional) For CSS or JS files
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
```

---

## **Input Fields**
1. **Hours Studied:** (Numeric)
2. **Previous Scores:** (Numeric)
3. **Extracurricular Activities:** (Yes/No)
4. **Sleep Hours:** (Numeric)
5. **Sample Questions Attempted:** (Numeric)

---

## **Output**
The application predicts the performance and categorizes it into one of the following:
- VERY BAD
- BELOW AVERAGE
- AVERAGE
- GOOD
- VERY GOOD
- THE BEST 🎉🎊

---

## **To Do**
- Add validations for user inputs.
- Enhance the UI with CSS.
- Extend prediction logic with more features.

---

## **Contributing**
Contributions are welcome! Feel free to submit a pull request or report any issues.

---

## **License**
This project is licensed under the MIT License.

---

Let me know if you'd like any changes or specific additions!
