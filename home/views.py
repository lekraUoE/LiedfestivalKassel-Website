from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import timezone

from django.template import Context, Template

from .models import Artist, MailTemplate, Sponsor, Concert
from .forms import TicketReservationForm


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    artists = Artist.objects.all()
    concerts = Concert.objects.order_by("performance_date")
    sponsors = Sponsor.objects.order_by("rang")

    return render(
        request,
        'home/base.html',
        {
            'concerts': concerts,
            'artists': artists,
            'sponsors': sponsors,
        }
    )


@login_required(login_url='/login/')
def letmesee(request, tag):

    return redirect('/#{}'.format(tag))


@login_required(login_url='/login/')
def karten(request):

    if request.method == "POST":
        form = TicketReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.request_date = timezone.now()
            reservation.save()

            temp = MailTemplate.objects.get(name='karten_bestaetigung')
            t = Template(temp.text)
            c = Context({"r":reservation})

            res = send_mail(
                temp.subject,
                t.render(c),
                "f.werthschulte@gmail.com",
                [reservation.email]
            )

            return render(request, 'home/karten.html', {'order_okay': True})
    else:
        form = TicketReservationForm()

    return render(request, 'home/karten.html', {'form': form})
