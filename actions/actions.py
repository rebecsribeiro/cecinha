# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from tkinter import Button
from typing import Any, Text, Dict, List
from typing_extensions import Self
import webbrowser
from matplotlib.pyplot import text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionEncaminharAberturaChamado():

    def name(self) -> Text:
        return "action_encaminhar_otrs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(buttons= Button(text="Abrir chamado:", command=lambda: webbrowser.open("https://correio.sefin.fortaleza.ce.gov.br/"), text ="\n Para: '\033[1m'chamados@sefin.fortaleza.ce.gov.br'\033[0m' \n Cc: 'Imagem ou documento que auxilie no chamado' \n Assunto: 'Assunto do chamado' \n Anexar: 'Insira uma imagem ou documento que mostre seu erro ou dúvida' *opcional \n Caixa de texto: 'Insira na caixa de texto abaixo a descrição do seu erro juntamento com seu: setor, número de contato e matrícula \n\n Após enviar é só aguardar a resposta do seu chamado por e-mail ou telefone da equipe COGETI."))

        return []

