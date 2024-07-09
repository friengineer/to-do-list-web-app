from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

# form for marking a task as finished
class CompleteForm(Form):
    number = IntegerField('Number', validators=[DataRequired()])

# form for creating a new task
class TaskForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
