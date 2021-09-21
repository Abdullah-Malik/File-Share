"""
contains the views of user app
"""

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import UpdateView

from .forms import ProfileCreationForm, ProfileUpdateForm
from .models import User

# Create your views here.


def signup(request):
    """
    signup view takes the UserForm and renders it using users/signup.html template

    Parameters:
        request: contains information regarding request

    Returns:
        calls the render function using request object, template and context object
    """
    form = ProfileCreationForm()

    if request.method == "POST":
        form = ProfileCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "users/signup.html", context)


class ProfileUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    ProfileUpdateView Extends Update View
    """

    model = User
    form_class = ProfileUpdateForm
    template_name = "users/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    success_message = "Profile Updated"

    def get_success_url(self):
        """
        Function redirects user to a specific page after succesful
        comment submission

        Return
            reverse: returns actual url against the url name provided as
            the first argument
        """
        return reverse("profile", kwargs={"username": self.object.username})

    def test_func(self):
        """
        test_func in the UserPassesTestMixin is overridden to check if the
        profile that the user is trying to acess is his own profile.

        If the profile is not logged in user's profile then he will not be
        allowed to access the profile page

        Parameters:
            self
        """
        profile = self.get_object()
        if profile == self.request.user:
            return True
        return False
