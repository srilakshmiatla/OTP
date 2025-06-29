# views.py

import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            otp = str(random.randint(100000, 999999))
            subject = 'Your OTP Code'
            message = f'Your OTP code is: {otp}'
            from_email = 'youremail@gmail.com'
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list)
                request.session['email'] = email
                request.session['otp'] = otp
                return redirect('verify_otp')
            except Exception as e:
                messages.error(request, f"Email failed: {e}")
        else:
            messages.error(request, "Please enter an email.")
    return render(request, 'app/login.html')


def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if user_otp == session_otp:
            messages.success(request, "OTP Verified Successfully!")
            return redirect('home')  # Replace with your success page
        else:
            messages.error(request, "You have entered incorrect OTP.")
            return render(request, 'app/verify_otp.html', {'resend': True})
    
    return render(request, 'app/verify_otp.html')


def resend_otp(request):
    email = request.session.get('email')
    if email:
        otp = str(random.randint(100000, 999999))
        subject = 'Your Resent OTP Code'
        message = f'Your new OTP is: {otp}'
        from_email = 'youremail@gmail.com'
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            request.session['otp'] = otp
            messages.success(request, "A new OTP has been sent to your email.")
        except Exception as e:
            messages.error(request, f"Failed to resend OTP: {e}")
        return redirect('verify_otp')
    else:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('login')
