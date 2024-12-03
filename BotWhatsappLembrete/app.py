from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    # Verifique se a mensagem recebida é um comando para definir um lembrete
    if 'lembrete' in incoming_msg:
        # Aqui você pode adicionar o código para definir o lembrete
        # Por exemplo, salvar em um banco de dados ou agendar uma tarefa
        resposta = 'Lembrete configurado com sucesso!'
        msg.body(resposta)
        responded = True

    if not responded:
        msg.body('Desculpe, não entendi sua mensagem.')

    return str(resp)


if __name__ == '__main__':
    app.run()
