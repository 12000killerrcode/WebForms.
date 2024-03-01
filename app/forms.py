from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,SelectField

from wtforms.validators import DataRequired,Length, EqualTo


class LoginForm(FlaskForm):

    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    
    """Product Form"""
    name_of_product = StringField('Name of product', validators=[DataRequired(), Length(1, 64)])
    description = StringField('Description', validators=[DataRequired(), Length(1, 64)])
    stock = SelectField('Stock', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4','4')])
    submit = SubmitField('Add Product')    

