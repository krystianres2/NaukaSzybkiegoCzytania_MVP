from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError # type: ignore
from fastReading.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Istnieje już taka nazwa użytkownika! Spróbuj innnej.')
        
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Istnieje już konto z podanym adresem e-mail.')
        
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Niepoprawny adres e-mail.')])
    password = PasswordField('Hasło', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Powtórz hasło', validators=[DataRequired(), EqualTo('password', 'Hasła muszą być takie same.')])
    submit = SubmitField('Zarejestruj się')

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')