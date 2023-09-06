# https://docs.djangoproject.com/en/4.2/ref/class-based-views/

from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, FormView
from django.urls import reverse_lazy

from .forms import EmailForm




from .models import Email


class EmailListView(ListView):
    model = Email
    paginate_by = 10  # if pagination is desired
    template_name = "generic/list.html" # default location `polls/email_list.html`

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EmailDetailView(DetailView):
    model = Email
    template_name = "generic/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time"] = timezone.now()
        return context


class EmailUpdateView(UpdateView):
    model = Email
    fields = '__all__'
    template_name = "generic/edit.html"
    success_url = reverse_lazy("polls:generic-email-list")


class EmailCreateView(CreateView):
    model = Email
    fields = "__all__"
    template_name = "generic/create.html"
    success_url = reverse_lazy("polls:generic-email-list")


class EmailFormView(FormView):
    template_name = "generic/form.html"
    form_class = EmailForm
    success_url = reverse_lazy("polls:generic-email-list")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # import ipdb;ipdb.set_trace()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



