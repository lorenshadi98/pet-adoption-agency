from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Name", validators=[
                       InputRequired(message="Name is required")])
    species = SelectField('Species',
                          choices=[('cat', 'Cat'), ('dog', 'Dog'),
                                   ('porcupine', 'Porcupine')]
                          )
    photo_url = StringField("Photo", validators=[
                            Optional(), URL(require_tld=False, message="Not a valid URL")])
    age = IntegerField("Age", validators=[Optional(),
                       NumberRange(min=0, max=30, message="Invalid age range. Must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for Editing a pet's information"""
    photo_url = StringField("Photo", validators=[
        Optional(), URL(require_tld=False, message="Not a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Pet avaiable for adoption?")
