from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import ProfileUpdateForm  # Define this in forms.py
from django.contrib.auth import update_session_auth_hash
from wishlist.models import Wishlist  # Assuming wishlist items are stored here
# from details.models import Review  # Assuming reviews are stored in a model named Review
from django.http import JsonResponse

# Create your views here.

@login_required
def show_profile(request):
    user = request.user
    # reviews = Review.objects.filter(user=user)[:10]  # Fetch recent reviews for user
    wishlist_items = Wishlist.objects.filter(user=user)[:3]  # Fetch 3 wishlist items

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        password_form = PasswordChangeForm(user=user, data=request.POST)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return JsonResponse({'success': True})
        
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Prevent logout after password change
            messages.success(request, 'Your password has been updated.')
            return JsonResponse({'success': True})
        
        else:
            errors = {**profile_form.errors, **password_form.errors}  # Collect all errors
            return JsonResponse({'success': False, 'errors': errors})
    else:
        profile_form = ProfileUpdateForm(instance=user)
        password_form = PasswordChangeForm(user=user)

    context = {
        'user': user,
        'profile_form': profile_form,
        'password_form': password_form,
        # 'reviews': reviews,
        'wishlist_items': wishlist_items,
    }
    return render(request, 'profile.html', context)