import requests, base64, json, re, os
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Transaction
from .forms import PaymentForm
from dotenv import load_dotenv

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .forms import LoginForm  
from django.contrib.auth import get_user_model
from .forms import EnrollmentForm
from django.core.mail import send_mail
from django.conf import settings
from myapp.models import Enrollment  
from .forms import PartnershipForm
from django.core.mail import send_mail
from .models import Partnership


# Load environment variables
load_dotenv()

# Retrieve variables from the environment
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")

MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE")
CALLBACK_URL = os.getenv("CALLBACK_URL")
MPESA_BASE_URL = os.getenv("MPESA_BASE_URL")




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def courses(request):
    return render(request, 'courses.html')

def partners(request):
    return render(request, 'partners.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    return render(request, 'contact.html')


def submit_partnership(request):
    return render(request, 'submit_partnership.html')

def team(request):
    return render(request, 'ourteam.html')

def mission(request):
    return render(request, 'mission.html')

def training_and_workshops(request):
    return render(request, 'training_and_workshops.html')

def consulting(request):
    return render(request, 'consulting.html')

def attarch(request):
    return render(request, 'attarch.html')

def intern(request):
    return render(request, 'intern.html')

def register_workshop(request):
    return render(request, 'register_workshop.html')

def workshop_detail(request):
    return render(request, 'workshop_detail.html')

# Authentication Views
User = get_user_model()

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm  # Ensure your form is correctly imported

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])  # Ensure password is hashed
            user.save()

            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")  # Redirect to login page
        else:
            messages.error(request, "Please correct the errors below.")  # Show errors if form is invalid
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})  # Return the form page with errors (if any)

User = get_user_model()

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        remember_me = request.POST.get("remember_me") == "on"

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            request.session.set_expiry(1209600 if remember_me else 0)
            return redirect("home")
        else:
            form.add_error(None, "Invalid email or password")

    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")


def forgot_password_view(request):
    return render(request, 'forgot_password.html')


def enroll(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment successful!")
            return redirect("courses")  # Redirect to courses page after enrollment
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = EnrollmentForm()
    
    return render(request, "enroll.html", {"form": form})


def enroll(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save()

            # Send Confirmation Email
            subject = "Enrollment Confirmation "
            message = f"Hello {enrollment.name},\n\nThank you for enrolling in {enrollment.course}!\nWe will reach out soon with further details.\n\nBest,\nTechAkili Technologies"
            recipient = [enrollment.email]

            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient, fail_silently=False)

            messages.success(request, "Enrollment successful! Check your email for confirmation.")
            return redirect("courses")  
        else:
            messages.error(request, "There was an error with your submission.")
    
    else:
        form = EnrollmentForm()
    
    return render(request, "enroll.html", {"form": form})



def submit_partnership(request):
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            partnership = form.save()

            # Send email notification
            subject = f"New Partnership Application from {partnership.organization_name}"
            message = f"""
            Organization Name: {partnership.organization_name}
            Contact Person: {partnership.contact_person}
            Email: {partnership.email}
            Phone: {partnership.phone}
            Partnership Type: {partnership.get_partnership_type_display()}
            Message: {partnership.message}
            """
            send_mail(subject, message, 'your_email@gmail.com', ['ramspheldonyango@gmail.com'])


            messages.success(request, "Your partnership request has been submitted successfully!")
            return redirect('partners')
        else:
            messages.error(request, "There was an error submitting your request.")
    
    else:
        form = PartnershipForm()
    
    return render(request, 'partners.html', {'form': form})


from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

def contact_form_submission(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Send an email
        send_mail(
            subject=f"New Contact Form Submission from {fullname}",
            message=f"Name: {fullname}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['ramspheldonyango@gmail.com'],  # Change to your email
            fail_silently=False,
        )

    
        return JsonResponse({'success': True, 'message': 'Your message has been sent!'})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


# views.py

from django.shortcuts import render, redirect
from paypalrestsdk import Payment
import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # "sandbox" or "live"
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def paypal_donate(request):
    if request.method == "POST":
        amount = request.POST.get("amount")

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://127.0.0.1:8000/donate/success/",
                "cancel_url": "http://127.0.0.1:8000/donate/cancel/"
            },
            "transactions": [{
                "amount": {
                    "total": amount,
                    "currency": "USD"
                },
                "description": "Donation to support our cause."
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)  # Redirect user to PayPal

        return render(request, "donate3.html", {"error": "Error processing payment"})

    return render(request, "donate3.html")


def donate_success(request):
    return render(request, "success.html")


def donate_cancel(request):
    return render(request, "cancel.html")

from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import render

def paypall_donate(request):
    return render(request, 'donate_paypal.html')

def donate(request):
    return render(request, 'donate.html')


# Phone number formatting and validation
def format_phone_number(phone):
    phone = phone.replace("+", "")
    if re.match(r"^254\d{9}$", phone):
        return phone
    elif phone.startswith("0") and len(phone) == 10:
        return "254" + phone[1:]
    else:
        raise ValueError("Invalid phone number format")

# Generate M-Pesa access token
def generate_access_token():
    try:
        credentials = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json",
        }
        response = requests.get(
            f"{MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials",
            headers=headers,
        ).json()

        if "access_token" in response:
            return response["access_token"]
        else:
            raise Exception("Access token missing in response.")

    except requests.RequestException as e:
        raise Exception(f"Failed to connect to M-Pesa: {str(e)}")

# Initiate STK Push and handle response
def initiate_stk_push(phone, amount):
    try:
        token = generate_access_token()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        stk_password = base64.b64encode(
            (MPESA_SHORTCODE + MPESA_PASSKEY + timestamp).encode()
        ).decode()

        request_body = {
            "BusinessShortCode": MPESA_SHORTCODE,
            "Password": stk_password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": MPESA_SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": CALLBACK_URL,
            "AccountReference": "account",
            "TransactionDesc": "Payment for goods",
        }

        response = requests.post(
            f"{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest",
            json=request_body,
            headers=headers,
        ).json()

        return response

    except Exception as e:
        print(f"Failed to initiate STK Push: {str(e)}")
        return e

# Payment View
def payment_view(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                phone = format_phone_number(form.cleaned_data["phone_number"])
                amount = form.cleaned_data["amount"]
                response = initiate_stk_push(phone, amount)
                print(response)

                if response.get("ResponseCode") == "0":
                    checkout_request_id = response["CheckoutRequestID"]
                    return render(request, "pending.html", {"checkout_request_id": checkout_request_id})
                else:
                    error_message = response.get("errorMessage", "Failed to send STK push. Please try again.")
                    return render(request, "payment_form.html", {"form": form, "error_message": error_message})

            except ValueError as e:
                return render(request, "payment_form.html", {"form": form, "error_message": str(e)})
            except Exception as e:
                return render(request, "payment_form.html", {"form": form, "error_message": f"An unexpected error occurred: {str(e)}"})

    else:
        form = PaymentForm()

    return render(request, "payment_form.html", {"form": form})

# Query STK Push status
def query_stk_push(checkout_request_id):
    print("Quering...")
    try:
        token = generate_access_token()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(
            (MPESA_SHORTCODE + MPESA_PASSKEY + timestamp).encode()
        ).decode()

        request_body = {
            "BusinessShortCode": MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "CheckoutRequestID": checkout_request_id
        }

        response = requests.post(
            f"{MPESA_BASE_URL}/mpesa/stkpushquery/v1/query",
            json=request_body,
            headers=headers,
        )
        print(response.json())
        return response.json()

    except requests.RequestException as e:
        print(f"Error querying STK status: {str(e)}")
        return {"error": str(e)}

# View to query the STK status and return it to the frontend
def stk_status_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            checkout_request_id = data.get('checkout_request_id')
            print("CheckoutRequestID:", checkout_request_id)

            # Query the STK push status using your backend function
            status = query_stk_push(checkout_request_id)

            # Return the status as a JSON response
            return JsonResponse({"status": status})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt  # To allow POST requests from external sources like M-Pesa
def payment_callback(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST requests are allowed")

    try:
        callback_data = json.loads(request.body)  # Parse the request body
        result_code = callback_data["Body"]["stkCallback"]["ResultCode"]

        if result_code == 0:
            # Successful transaction
            checkout_id = callback_data["Body"]["stkCallback"]["CheckoutRequestID"]
            metadata = callback_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"]

            amount = next(item["Value"] for item in metadata if item["Name"] == "Amount")
            mpesa_code = next(item["Value"] for item in metadata if item["Name"] == "MpesaReceiptNumber")
            phone = next(item["Value"] for item in metadata if item["Name"] == "PhoneNumber")

            # Save transaction to the database
            Transaction.objects.create(
                amount=amount, 
                checkout_id=checkout_id, 
                mpesa_code=mpesa_code, 
                phone_number=phone, 
                status="Success"
            )
            return JsonResponse({"ResultCode": 0, "ResultDesc": "Payment successful"})

        # Payment failed
        return JsonResponse({"ResultCode": result_code, "ResultDesc": "Payment failed"})

    except (json.JSONDecodeError, KeyError) as e:
        return HttpResponseBadRequest(f"Invalid request data: {str(e)}")