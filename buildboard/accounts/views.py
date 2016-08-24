from django.shortcuts import render
from models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

@login_required
def profile(request):
  student = Account.objects.get(user__email=request.user.email)
  memberships = student.membership_set.all()
  projects = []
  for membership in memberships:
    projects.append(membership.project)

  return render(request, 'profile.html', {
     'semester_nav_links': get_semester_nav_links(),
     'projects': projects,
  })