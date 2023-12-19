from flask import Blueprint, make_response
import qrcode
from io import BytesIO


pagamento_bp = Blueprint('pagamento_bp', __name__)

@pagamento_bp.route('/gerar_qrcode/<int:valor>')
def gerar_qrcode(valor):
    chave_pix = "chave-pix"  # Substitua pela sua chave Pix
    nome_titular = "Nome do Titular"  # Substitua pelo nome do titular
    descricao = "Pagamento de R$100,00"
    conta = "123123-1"
    print(valor)

    # Montar a URL PIX
    url_pix = "https://www.icegif.com/wp-content/uploads/2022/01/icegif-962.gif"

    # Criar o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_pix)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Converter a imagem para um objeto de bytes
    img_byte_array = BytesIO()
    img.save(img_byte_array, format="PNG")
    img_byte_array = img_byte_array.getvalue()

    # Criar uma resposta HTTP com a imagem
    response = make_response(img_byte_array)
    response.headers['Content-Type'] = 'image/png'

    return response
