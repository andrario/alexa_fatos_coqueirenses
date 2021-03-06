# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

#user added
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Fatos = [
    '''Tanto a queda quanto o poço da cachoeira do itambé, pertence ao município de Cássia dos Coqueiros. Qualquer um contrário, está errado.''',
    '''Se um animal de sua criação foi encontrado devorado durante a noite, é um sinal de atividade do Loporbí.<break time="1s"/>Recomendo adiquirir balas de prata. Você gostaria de buscar por, Balas de Prata, na loja da amazon?''',
    '''Em dias de chuva é possível observar um cavalo alado pastando pelas cercanias do município.''',
    '''Caso esteja apreciando uma noite gélida na praça da matriz, cuidado com o cavaleiro que ronda a madrugada no local. Ninguém sabe ao certo como ele se parece, aparentemente quem o viu não voltou para contar.''',
    '''Nos dias pacatos quando as ruas estão vazias, pode se escutar um andarilho atravessando vagarosamente a cidade arrastando correntes. Não se sabe de onde e para onde vai. Se você estiver disposto a perguntar, alongue-se primeiro, pois mesmo correndo ninguém até hoje conseguiu alcançá-lo''',
    '''Fique atento ao retornar ao centro vindo do rio Tamanduá pela noite, caso você encontre uma mulher sozinha, usando um vestido branco, e segurando um bebê no colo. Não se apavore, é apenas um espírito local. Não se aproxime dela e continue caminhando. Ao chegar em casa, beba uma dose de cachaça para aliviar a tensão.''',
    '''Depois da demolição do coreto da praça central. Os casos de bódes dançando em círculos caíram vertiginósamente. Para a alegria dos residentes do entorno da praça da matriz, além de não ter que conviver com os olhares intimidadores dos caprinos, os fortes golpes desferidos nas janelas durante a dança, que infernizavam o sono dos moradores, Acabaram.''',
    '''Quatre meia é o horário oficial do café da tarde em diversas casas na cidade.'''
    ]

class FatosIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FatosIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = random.choice(Fatos)
        
        resposta = {
			"outputSpeech": {
				"type": "SSML",
				"ssml": "<speak>"+speak_output+"</speak>"
			},
			"reprompt": {
				"outputSpeech": {
					"type": "SSML",
					"ssml": "<speak>"+speak_output+"</speak>"
				}
			},
			"shouldEndSession": True,
			"type": "_DEFAULT_RESPONSE"
		}
        
        return resposta


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Oi tião, tudo bão? Quer ouvir um fato coqueirense? ou precisa de ajuda?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Uái, se quiser saber um fato, é só falar. Quero um fato coqueirense ou alguma coisa assim."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Té mais."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Uái tião, não entendi esse trem. Pode falar denovo?"
        reprompt = "É tião, não entendi mesmo. Tenta falar outra coisa."

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Não consegui fazer esse trem. Tenta falar outra coisa."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(FatosIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()