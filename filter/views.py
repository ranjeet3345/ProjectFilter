import json
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .ai_classifier import classify_message
from .telegram_bot import send_telegram_message

logger = logging.getLogger(__name__)

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
            message = extract_message(payload)
            if message:
                logger.info(f"Received: {message}")
                classification = classify_message(message['text'])
                logger.info(f"Classified as: {classification}")
                if classification in ['loan query', 'repayment']:
                    send_telegram_message(f"From {message['sender']}: {message['text']}")
            return JsonResponse({"status": "success"})
        except Exception as e:
            logger.error(f"Error: {e}")
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"message": "Only POST allowed"}, status=405)

def extract_message(payload):
    try:
        entry = payload['entry'][0]
        message = entry['changes'][0]['value']['messages'][0]
        return {
            'sender': message['from'],
            'text': message['text']['body']
        }
    except:
        return None
