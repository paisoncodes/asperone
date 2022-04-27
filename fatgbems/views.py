import requests
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from config.settings import (
    PAYMENT_NOTIFICATION_URL,
    PAYMENT_REVERSAL_URL,
    GET_INFORMATION_URL
)


headers = {
    "Content-Type": "application/json"
}


class PaymentNotification(APIView):
    def post(self, request):
        data = {
            "data": request.data
        }
        try:
            headers["Authorization"] = request.headers["Authorization"]
        except Exception:
            return Response(
                {
                    "message": "Authorization should not be empty"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        response = requests.post(PAYMENT_NOTIFICATION_URL, data=json.dumps(data), headers=headers)
        new_response = response.json()
        if response.status_code == 401:
            return Response(new_response, status=status.HTTP_401_UNAUTHORIZED)
        elif response.status_code == 400:
            return Response(new_response, status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(new_response, status=status.HTTP_403_FORBIDDEN)
        elif response.status_code == 200:
            return Response(new_response, status=status.HTTP_200_OK)
        elif response.status_code == 403:
            return Response(
                {
                    "message": "Invalid Authorization"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        else:
            return Response(
                {
                    "message": new_response,
                    "code": response.status_code
                },
                status=status.HTTP_404_NOT_FOUND
            )


class PaymentReversal(APIView):
    def post(self, request):
        data = request.data

        
    


class GetInformation(APIView):
    def post(self, request):
        data = request.data

        try:
            headers["Authorization"] = request.headers["Authorization"]
        except Exception:
            return Response(
                {
                    "message": "Authorization should not be empty"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        if "TerminalID" not in request.headers.keys():
            return Response(
                {
                    "message": "TerminalID is empty"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        if "SerialNumber" not in request.headers.keys():
            return Response(
                {
                    "message": "SerialNumber is empty"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if (data["TerminalID"] != request.headers["TerminalID"]) or (data["SerialNumber"] != request.headers["SerialNumber"]):
            return Response(
                {
                    "message": "Terminal not found"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        response = requests.post(GET_INFORMATION_URL, data=json.dumps(data), headers=headers)
        new_response = response.json()
        if response.status_code == 401:
            return Response(new_response, status=status.HTTP_401_UNAUTHORIZED)
        elif response.status_code == 400:
            return Response(new_response, status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 200:
            return Response(new_response, status=status.HTTP_200_OK)
        elif response.status_code == 403:
            return Response(
                {
                    "message": "Invalid Authorization"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        else:
            return Response(
                {
                    "message": new_response,
                    "code": response.status_code
                },
                status=status.HTTP_404_NOT_FOUND
            )
