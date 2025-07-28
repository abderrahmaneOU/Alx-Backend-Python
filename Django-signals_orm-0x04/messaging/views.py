from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account and all related data have been deleted.")
        return redirect('home')
    messages.error(request, "Invalid request method.")
    return redirect('profile')
