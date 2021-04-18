from django.shortcuts import render

# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

# def update_user(request, user_id):
def update_profile(request):
    # users = User.objects.all().select_related('profile')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

