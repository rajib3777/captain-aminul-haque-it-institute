import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import StudentProfile

@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)

    name = (data.get("name") or "").strip()
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    plan = (data.get("plan") or "").strip()

    is_dhaka16 = data.get("isDhaka16")   
    area = (data.get("dhaka16Area") or "").strip()

    if not all([name, phone, email, plan , is_dhaka16, area]):
        return JsonResponse({"error": "Missing fields"}, status=400)

    
    if is_dhaka16 != "yes":
        return JsonResponse({"error": "Only Dhaka-16 voters can register."}, status=403)

    if not phone.isdigit() or len(phone) != 11:
        return JsonResponse({"error": "Invalid phone number"}, status=400)
    
    if "@" not in email or "." not in email:
        return JsonResponse({"error": "Invalid email address"}, status=400)
    
    if not area:
        return JsonResponse({"error": "Dhaka-16 area is required."}, status=400)

    if User.objects.filter(username=email).exists():
        return JsonResponse({"error": "User already exists"}, status=409)

    user = User.objects.create_user(
        username=email,
        email=email,
        password=None
    )
    user.first_name = name
    user.save()

    StudentProfile.objects.create(
        user=user,
        phone=phone,
        plan=plan,
        is_dhaka16_voter=True,
        dhaka16_area=area
    )

    return JsonResponse({"success": True})



def health(request):
    return JsonResponse({"ok": True})