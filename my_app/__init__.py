from flask import Flask, render_template, request
import joblib 
import numpy as np
import pandas as pd


def app_factory():
    app = Flask(__name__)

    # XgBoost Model
    # model = xgboost.XGBClassifier()
    # model.load_model("project3_model.pkl")
    # filepath = os.path.join(os.getcwd(), "xgb_model.bst")
    model = joblib.load('project3_model_.pkl')
    # booster = Booster()
    # model = booster.load_model(filepath)

    # sess = model.Session()
    # sess.run(model)

    @app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            weekend = float(request.form['weekend'])
            avg_temp = float(request.form['avg_temp'])
            min_temp = float(request.form['min_temp'])
            max_temp = float(request.form['max_temp'])
            rain_fall = float(request.form['rain_fall'])
            holiday = float(request.form['holiday'])
        
        entrance_subtotal = 0

        data = np.array([weekend, avg_temp, min_temp, max_temp, rain_fall, holiday]).reshape(1, -1)
        data = pd.DataFrame(data)
        
        entrance_subtotal = model.predict(data)

        return render_template('index.html', entrance_subtotal=entrance_subtotal)

    return app

if __name__ == '__main__':
    app = app_factory()
    app.run(debug=True)

