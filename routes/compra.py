from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required
from models import Item, Compra, CompraForm
from config import db


compra_bp = Blueprint('compra_bp', __name__)

# Página de compra
@compra_bp.route('/payment/<int:item_id>', methods=['GET', 'POST'])
def compra(item_id=None):
    form = CompraForm()
    if item_id is not None:
        item = Item.query.get(item_id)
        form.item.data = item.nome  # Preenche o campo 'item' com o nome do item
    if form.validate_on_submit():
        nome = form.nome.data
        mensagem = form.mensagem.data
        item_nome = form.item.data  # O nome do item selecionado
        nova_compra = Compra(nome=nome, item=item_nome, mensagem=mensagem)
        db.session.add(nova_compra)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('payment.html', item=item, form=form)

# Lista de itens comprados e mensagens
@compra_bp.route('/compras')
@login_required
def compras():
    compras = Compra.query.all()
    return render_template('compras.html', compras=compras)
