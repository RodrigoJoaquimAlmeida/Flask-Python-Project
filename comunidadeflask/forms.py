from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeflask.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail cadastrado. Faça login ou cadastre outro e-mail')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_fazerlogin = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Imagem do Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_a = BooleanField('Módulo 0')
    curso_b = BooleanField('Módulo 1')
    curso_c = BooleanField('Módulo 2')
    curso_d = BooleanField('Módulo 3')
    curso_e = BooleanField('Módulo 4')
    curso_f = BooleanField('Módulo 5')
    curso_g = BooleanField('Módulo 6')
    curso_h = BooleanField('Módulo 7')
    curso_i = BooleanField('Módulo 8')
    curso_j = BooleanField('Módulo 9')
    curso_k = BooleanField('Módulo 10')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Usuário ja cadastrado com e-mail solicitado. Cadastre um novo e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')