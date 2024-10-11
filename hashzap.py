# Tela inicial:
    # titulo: hashzap
    # botao: iniciar chat
        # quando clicar no botao
        # abrir um popup/modal/alerta
            # titulo: bem vindo ao hashzap
            # caixa de texto: escreva seu nome
            # botao: entrar no chat
                # clicar no botao
                # fechar popup
                # sumir titulo
                # sumir botao iniciar chat
                    # carrega chat
                    # carrega campo de enviar msg
                    # btn enviar
                        # clicar botao
                        # enviar
                        # limpar caixa de msg

# Flet
import flet as ft

# criar uma função principal para rodar o app
def main(pagina):
    titulo = ft.Text("Hashzap")

    def enviarMsgTunel(mensagem):
        # escrever tudo que é pra acontecer para todos os usuário que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviarMsgTunel)

    def enviarMsg(evento):
        nomeUsuario = caixaNome.value
        textoCampoEnviarMsg = campoEnviarMsg.value
        mensagem = f"{nomeUsuario}: {textoCampoEnviarMsg}"
        pagina.pubsub.send_all(mensagem)
        campoEnviarMsg.value = ""
        pagina.update()

    campoEnviarMsg = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviarMsg)
    botaoEnviar = ft.ElevatedButton("Enviar", on_click=enviarMsg)
    linhaEnviar = ft.Row([campoEnviarMsg, botaoEnviar])
    chat = ft.Column()

    def entrarChat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linhaEnviar)
        nomeUsuario = caixaNome.value
        mensagem = f"{nomeUsuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    # criar alerta pop up
    tituloPopup = ft.Text("Bem vindo ao Hashzap")
    caixaNome = ft.TextField(label="Digite seu nome")
    botaoPopup = ft.ElevatedButton("Entrar no Chat", on_click=entrarChat)
    popup = ft.AlertDialog(title=tituloPopup, content=caixaNome, actions=[botaoPopup])

    def abrir_popup(evento):
            pagina.dialog = popup
            popup.open = True
            pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(titulo)
    pagina.add(botao)


# executar essa função com o flet
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
