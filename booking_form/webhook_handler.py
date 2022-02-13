from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhooks"""
    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """ Handle generic webhook event """

        return HttpResponse(
            content = f'Webhook recieved: {event["type"]}',
            status =200)