import string
import random
from django.shortcuts import render, redirect

from .models import PANTSGame as PANTS
from .forms import PANTSForm


def home(request):
    # current_session = request._cookies['sessionid']
    # answers = PANTS.objects.filter(session_id=current_session)
    # letter = random.choice(string.ascii_uppercase)

    if request.POST:
        pants = PANTSForm(request.POST)
        if pants.is_valid():
            form = pants.save(commit=False)
            # form.session_id = current_session
            form.save()
        return redirect('home')
    return render(request, 'games/pants.html', {
        # 'answers': answers,
        'PANTS_form': PANTSForm,
        # 'letter': letter,
    })
