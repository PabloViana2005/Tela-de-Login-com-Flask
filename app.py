# ==========================================
# Para Validações de Email
# Comando de Instalação no terminal:
# pip install flask
# pip install flask_wtf email_validator
# ==========================================

from flask import Flask, request, render_template, redirect

# Base de Formulários
from flask_wtf import FlaskForm

# Formatação dos campos
from wtforms import StringField, PasswordField, SubmitField

# Validação dos campos
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

# Instância Principal
app = Flask(__name__)

# Chave Secreta
app.config['SECRET_KEY'] = 'phc@123'

# Formulário de Cadastro
class RegisterForm(FlaskForm):

    first_name = StringField('Primeiro Nome', validators=[DataRequired()])
    last_name = StringField('Sobrenome')
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[InputRequired()])
    confirm = PasswordField('Confirme a senha', validators=[EqualTo('password', message='As senhas devem ser iguais.')])
    submit = SubmitField('CADASTRAR')

# Criação de Rota que respondem ao GET
@app.route('/')
def root():
    return redirect('/register')

# Rota
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Instância da classe/formulário
    form = RegisterForm()

    # Validação do envio do formulário bem-sucedido
    if form.validate_on_submit():
        return redirect('/template')
    
    # Validação do envio do formulário mal-sucedido
    return render_template('register.html', form=form)

@app.route('/template')
def template():
    return render_template('index.html', name='Flask Developer')

if __name__ == '__main__':
    app.run(debug=True, port=5152)