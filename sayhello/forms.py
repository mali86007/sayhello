from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class HelloForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('留言', validators=[DataRequired(), Length(1, 256)])
    submit = SubmitField()