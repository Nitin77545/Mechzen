# auth_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OTP, User
from .utils import send_otp
from datetime import datetime

class SendOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        if not phone:
            return Response({"error": "Phone number is required"}, status=400)
        otp_obj = OTP.objects.create(phone_number=phone)
        send_otp(phone, otp_obj.otp)
        return Response({"message": "OTP sent successfully"})

class VerifyOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        otp_input = request.data.get('otp')
        try:
            otp_obj = OTP.objects.filter(phone_number=phone).latest('created_at')
        except OTP.DoesNotExist:
            return Response({"error": "OTP not found"}, status=404)

        if otp_obj.expires_at < datetime.now():
            return Response({"error": "OTP expired"}, status=400)

        if otp_obj.otp != otp_input:
            return Response({"error": "Invalid OTP"}, status=400)

        user, created = User.objects.get_or_create(phone_number=phone)
        return Response({"message": "OTP verified", "user_id": user.id})
