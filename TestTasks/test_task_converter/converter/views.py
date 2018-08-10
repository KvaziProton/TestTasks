import datetime

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseBadRequest

from .forms import ConvertForm
from .utils import get_usd_rub_rate

class ConvertView(FormView):
    '''Get the exchange rate and convert usd to rubles'''

    template_name = 'index.html'
    form_class = ConvertForm
    sucsess_url = ''

    def form_valid(self, form):
        usd_ammount = form.cleaned_data['usd']
        try:
            rate = get_usd_rub_rate()
        except (KeyError, ConnectionError):
            return HttpResponseBadRequest(
                'Something goes wrong, pease, try again later'
                )
        rub_ammount = round((usd_ammount * rate), 2)
        return render(
            self.request,
            self.template_name,
            {'rub': rub_ammount,
            'usd': usd_ammount,
            'date': datetime.datetime.now(),
            'form': self.form_class}
            )
