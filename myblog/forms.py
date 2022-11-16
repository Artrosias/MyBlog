from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Campo obbligatorio!")])
    password = PasswordField('Password', validators=[DataRequired("Campo obbligatorio!")])
    remember_me = BooleanField('Ricordami')
    submit = SubmitField('Login')



class PostForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired("Campo obbligatorio!"),Length(min=5, max=25, message="Il titolo deve essere compreso tra 3 e 25")])
    description = TextAreaField('Descrizione', validators=[Length(max=250, message="La descrizione può contenere massimo 250 caratteri!")])
    body = TextAreaField('Contenuto', validators=[DataRequired("Campo obbligatorio!")])
    image = FileField('Immagine di copertina', validators=[FileAllowed(['jpg', 'jpeg','png'])])
    submit = SubmitField('Salva post')

