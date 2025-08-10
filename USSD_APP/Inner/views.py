from django.http import HttpResponse
from Inner.models import PrimaryUser, Transactions
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ussd_endpoint(request):
    if request.method == 'POST':
        session_id = request.POST.get("sessionId", None)
        service_code  = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text         = request.POST.get("text", '')

        if text == '':
            response = 'CON Welcome to Ian USSD Service\n'
            response += '1. Register\n'
            response += '2. Check my transactions\n'
            response += '3. Send Kash\n'
            response += '4. Change PIN\n'
            response += '5. Access my prize balance'

        elif text == '1':
            response = 'END Register Under Construction'
        
        elif text == '2':
            response = 'END Check my transactions Under Construction'
        
        elif text == '3':
            response = 'END Send Kash Under Construction'
        
        elif text == '4':
            response = 'END Change PIN Under Construction'

        elif text == '5':
            response = 'END Access my prize balance Under Construction'

        else:
            response = 'END Wrong choice'

        return HttpResponse(response, content_type='text/plain')

    return HttpResponse('Method Not Allowed', status=405)
