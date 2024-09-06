from flask_wtf import FlaskForm

from wtforms import (
    SelectField,
    FloatField,
    IntegerField,
    SubmitField
)

from wtforms.validators import DataRequired

import pandas as pd

data_zomato = pd.read_csv("zomato.csv")

class InputForm(FlaskForm):
    online_order = SelectField(
        "Online Order",
        choices=data_zomato["online_order"].unique().tolist(),
        validators=[DataRequired()]
    )
    book_table = SelectField(
        "Book Table",
        choices=data_zomato["book_table"].unique().tolist(),
        validators=[DataRequired()]
    )
    rate = FloatField(
        "Rating",
        validators=[DataRequired()]
    )
    votes = IntegerField(
        "Votes",
        validators=[DataRequired()]
    )
    rest_type = SelectField(
        "Rest_Type",
        choices=data_zomato["rest_type"].unique().tolist(),
        validators=[DataRequired()]
    )
    type = SelectField(
        "Type",
        choices=data_zomato["type"].unique().tolist(),
        validators=[DataRequired()]
    )
    location = SelectField(
        "Location",
        choices=data_zomato["location"].unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")







