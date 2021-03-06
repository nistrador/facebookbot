import os
import sys
import json

import requests
from flask import Flask, request

app = Flask(__name__)

os.environ["VERIFY_TOKEN"] = "qualquer_coisa"
os.environ["PAGE_ACCESS_TOKEN"] = "EAAGIxS2E41EBAAXXl9zR9wp9eOlahLXRQNo0jbN3OUpB8kAIq5nwAzDAlO5RjJ3sHKSieDHmwK5ORW3s351iACjexCfPPQmjPPlDoCiMucZBG4MbquYc89VPvwydyrHI6UQR4h1xIPlgHVln0JOYqNRJ99a0JYmBH44K3VgZDZD"

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must
    # return the 'hub.challenge' value in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    
                    message_ascii = message_text.encode('ascii', 'ignore')

                    send_message(sender_id, message_ascii)

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
		"recipient": {
			"id": recipient_id
		},
		"message": {
			"text": "got it, thanks!"
		}
	}, ensure_ascii=False).encode('utf-8')

    newMessage = message_text.lower()
    if newMessage.find("economia") != -1:
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type" : "template",
                    "payload": {
                        "template_type": "generic",
                        "elements":[{
                            "title": "Uruguai diz que Serra tentou comprar voto no Mercosul",
                            "image_url": "http://og.infg.com.br/economia/19725775-2a3-821/FT1086A/420/201607142256204353_RTS.jpg",
                            "subtitle": "Objetivo seria suspender transferencia da presidencia do grupo para a Venezuela",
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"http://oglobo.globo.com/economia/uruguai-diz-que-serra-tentou-comprar-voto-no-mercosul-19933386",
                                    "title":"Leia a noticia"
                                },
                                {
                                    "type":"postback",
                                    "title":"Start Chatting",
                                    "payload":"USER_DEFINED_PAYLOAD"
                                }
                            ]
                          },
                          {
                            "title": "Fazenda confirma que crescimento de 2017 sera revisto para 1,6%",
                            "image_url": "http://og.infg.com.br/economia/19618885-016-bfc/FT1086A/420/INFOCHPDPICT000058158919-767.jpg",
                            "subtitle": "Expectativa para inflacao sera mantida em 4,8%, diz secretario de Politica Economica",
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"http://oglobo.globo.com/economia/fazenda-confirma-que-crescimento-de-2017-sera-revisto-para-16-19943139",
                                    "title":"Leia a noticia"
                                },
                                {
                                    "type":"postback",
                                    "title":"Start Chatting",
                                    "payload":"USER_DEFINED_PAYLOAD"
                                }
                            ]
                          }
                        ]
                    }
                }
            }
        }, ensure_ascii=False).encode('utf-8')
    elif newMessage.find("brasil") != -1:
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type" : "template",
                    "payload": {
                        "template_type": "generic",
                        "elements":[
                          {
                            "title": "STF abre inquerito contra Dilma e Lula por tentativa de obstrucao da Justica",
                            "image_url": "http://og.infg.com.br/in/19936117-7d7-158/FT1086A/420/2016_908888271-201605121459541318.jpg_20160512.jpg",
                            "subtitle": "Cardozo e Mercadante tambem sao alvo de apuracao",
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"http://oglobo.globo.com/economia/uruguai-diz-que-serra-tentou-comprar-voto-no-mercosul-19933386",
                                    "title":"Leia a noticia"
                                },
                                {
                                    "type":"postback",
                                    "title":"Start Chatting",
                                    "payload":"USER_DEFINED_PAYLOAD"
                                }
                            ]
                          }
                        ]
                    }
                }
            }
        }, ensure_ascii=False).encode('utf-8')
    elif newMessage.find("rio") != -1:
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type" : "template",
                    "payload": {
                        "template_type": "generic",
                        "elements":[
                          {
                            "title": "Socio da fabrica do Biscoito Globo diz que apoio de cariocas supera critica no 'NYT'",
                            "image_url": "http://og.infg.com.br/in/19923793-52b-4f7/FT1500A/550/globo.jpg",
                            "subtitle": "Jornalista afirmou que iguaria e sem gosto e foi bombardeado nas redes",
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"http://oglobo.globo.com/rio/socio-da-fabrica-do-biscoito-globo-diz-que-apoio-de-cariocas-supera-critica-no-nyt-19930926",
                                    "title":"Leia a noticia"
                                },
                                {
                                    "type":"postback",
                                    "title":"Start Chatting",
                                    "payload":"USER_DEFINED_PAYLOAD"
                                }
                            ]
                          }
                        ]
                    }
                }
            }
        }, ensure_ascii=False).encode('utf-8')

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
