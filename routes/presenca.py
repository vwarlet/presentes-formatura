from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required
from models import Presenca, PresencaForm
from config import db 


presenca_bp = Blueprint('presenca_bp', __name__)

@presenca_bp.route('/presenca')
@login_required
def presenca():
    form = PresencaForm()
    presencas = Presenca.query.all()
    return render_template('presenca.html', presencas=presencas, form=form)

@presenca_bp.route('/confirmar', methods=['GET', 'POST'])
def confirmar():
    form = PresencaForm()
    if request.method == 'POST':
        nomes = []
        for item in request.form.getlist('nome'):
            nome = item.strip()
            if nome:
                nomes.append(nome)
        for nome in nomes:
            nova_presenca = Presenca(nome=nome)
            db.session.add(nova_presenca)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('confirmar.html', form=form)
