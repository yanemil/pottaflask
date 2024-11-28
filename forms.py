from flask_wtf import FlaskForm
from wtforms import SelectField

# CATEGORY = [('Animals', 'Animals'), ('Films', 'Films'), ('Music', 'Music'), ('History', 'History')]
# QUIZ_TYPE = [('True / False', 'True / False'), ('Multiple Choice', 'Multiple Choice')]
# QUANTITY = [('10', '10'), ('5', '5'), ('15', '15')]
DECISION = [('TRYB VOLDEMORT', 'TRYB VOLDEMORT'), ('ŁATWIZNA', 'ŁATWIZNA')]


class MyForm(FlaskForm):
    decision = SelectField('Wybierz poziom trudności:', choices=DECISION)
    #category = SelectField('Choose Questions Category:', choices=CATEGORY)
    # quiz_type = SelectField('Define Quiz Type:', choices=QUIZ_TYPE)
    # quantity = SelectField('Define Questions Quantity:', choices=QUANTITY)
