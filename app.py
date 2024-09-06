from flask import (
    Flask,
    render_template,
    flash
)

from form import InputForm

import pandas as pd
import joblib


app = Flask(__name__)
app.config["SECRET_KEY"] = "restaurant_price_prediction"

model = joblib.load("model1.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET","POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        new_x = pd.DataFrame(dict(
            online_order = [form.online_order.data],
            book_table = [form.book_table.data],
            rate = [form.rate.data],
            votes = [form.votes.data],
            rest_type = [form.rest_type.data],
            type = [form.type.data],
            location = [form.location.data]
        ))

        prediction = model.predict(new_x)[0]
        message = f"The predicted price is {prediction.round(2)} INR"
    else:
        message = "Please give valid inputs"

    return render_template("predict.html", title="Prediction", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)