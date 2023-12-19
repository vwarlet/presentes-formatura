from flask import Blueprint, redirect, url_for, render_template, Response, flash
from flask_login import login_required
from models import Item, ItemForm
from config import db


item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/itens')
@login_required
def itens():
    form = ItemForm()
    itens = Item.query.all()
    return render_template('itens.html', itens=itens, form=form)

@item_bp.route('/adicionar_item', methods=['GET', 'POST'])
@login_required
def adicionar_item():
    form = ItemForm()
    if form.validate_on_submit():
        nome = form.nome.data
        valor = form.valor.data
        imagem = form.imagem.data.read()
        novo_item = Item(nome=nome, valor=valor, imagem=imagem)
        db.session.add(novo_item)
        db.session.commit()
        return redirect(url_for('item_bp.itens'))
    return render_template('adicionar.html', form=form)

@item_bp.route('/editar_item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def editar_item(item_id):
    item = Item.query.get(item_id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.nome = form.nome.data
        item.valor = form.valor.data
        if form.imagem.data:
            item.imagem = form.imagem.data.read()
        db.session.commit()
        return redirect(url_for('item_bp.itens'))
    return render_template('editar.html', form=form, item=item)

@item_bp.route('/excluir_item/<int:item_id>', methods=['POST'])
@login_required
def excluir_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item excluído com sucesso', 'success')
    return redirect(url_for('item_bp.itens'))

@item_bp.route('/imagem_item/<int:item_id>')
def imagem_item(item_id):
    item = Item.query.get_or_404(item_id)
    return Response(item.imagem, content_type='image/jpeg')

@item_bp.route('/listar')
def listar_itens():
    itens = Item.query.all()
    return render_template('listar.html', itens=itens)

@item_bp.route('/carousel')
def carousel():
    itens = Item.query.all()
    return render_template('carousel.html', itens=itens)
