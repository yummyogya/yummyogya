from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import ProfileUpdateForm  # Define this in forms.py
from django.contrib.auth import update_session_auth_hash
from wishlist.models import Wishlist  # Assuming wishlist items are stored here
# from details.models import Review  # Assuming reviews are stored in a model named Review
from django.http import JsonResponse
from .models import Profile

# Create your views here.

@login_required
def show_profile(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user)[:3]  # Asumsi ada wishlist model
    profile, created = Profile.objects.get_or_create(user=user)  # Buat profil jika belum ada

    context = {
        'user': user,
        'profile_form': ProfileUpdateForm(instance=profile),
        'wishlist_items': wishlist_items,
    }
    return render(request, 'profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        delete_photo = request.POST.get('delete_photo', False)

        if profile_form.is_valid():
            if delete_photo:
                profile.profile_photo.delete()
            profile_form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': profile_form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})