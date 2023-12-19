from wtforms import StringField, FileField, HiddenField, PasswordField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_login import UserMixin
from config import db


# Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    csrf = HiddenField('CSRF Token')

# Lista de presentes
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    valor = db.Column(db.String(50))
    imagem = db.Column(db.LargeBinary)

class ItemForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    valor = StringField('Valor', validators=[DataRequired()])
    imagem = FileField('Imagem (JPEG ou PNG)')

# Lista de Confirmados
class Presenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

class PresencaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])

# Presente comprado e mensagem deixada
class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    item = db.Column(db.String(50))
    mensagem = db.Column(db.String(1000))

class CompraForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    item = StringField('Item', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem')
