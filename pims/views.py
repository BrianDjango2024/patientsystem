from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls.base import reverse_lazy
from .forms import RecordForm, ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Record
from django.views.generic.edit import FormView


class IndexView(TemplateView):

    template_name = 'index.html'

@method_decorator(login_required, name='dispatch')
class CreateRecordView(CreateView):
    form_class = RecordForm
    template_name = "record.html"
    success_url = reverse_lazy('pims:record_done')

    def form_valid(self, form):
        recorddata = form.save(commit=False)
        recorddata.user = self.request.user
        recorddata.save()
        return super().form_valid(form)
    
class RecordSuccessView(TemplateView):
    template_name = 'record_success.html'

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Record.objects.order_by('-record_at')
    paginate_by = 3

class UserView(ListView):
    template_name='index.html'
    paginate_by = 3

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = Record.objects.filter(
            user=user_id).order_by('-record_at')
        return user_list

class DetailView(DetailView):
    template_name = 'detail.html'
    model = Record

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = Record.objects.filter(
            user=self.request.user).order_by('-record_at')
        return queryset

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("pims:contact_result")

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            username = user.username
            email = user.email
        else:
            username = "Anonymous"
            email = form.cleaned_data.get("email", "anonymous@example.com")
        
        form.send_email(username=username, email=form.cleaned_data["email"])
        return super().form_valid(form)

class ContactResultView(TemplateView):
    template_name = 'contact_result.html'
