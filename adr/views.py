from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, View
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login, LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import AdrCheck
from .forms import AdrCheckForm





class LoginPageView(LoginView):
    template_name = 'user/login.html'
    fields = '__all_'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('adr_list')


class HomeView(TemplateView):
    template_name = 'html/index.html'


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(),
                                     self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/list')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class AdrCreateView(LoginRequiredMixin,  CreateView):
    model = AdrCheck
    template_name = 'adr/adr_check.html'
    form_class = AdrCheckForm
    success_url = '/list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdrCreateView, self).form_valid(form)


class AdrUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'adr.change_adrcheck'
    permission_denied_message = ""
    login_url = 'home'

    model = AdrCheck
    template_name = 'adr/adr_check.html'
    form_class = AdrCheckForm
    success_url = reverse_lazy('adr_list')


class AdrDeleteView(DeleteView):
    model = AdrCheck
    context_object_name = 'adr'
    template_name = 'adr/adr_delete.html'
    success_url = reverse_lazy('adr_list')


class AdrListView(LoginRequiredMixin, ListView):
    model = AdrCheck
    context_object_name = 'adr'
    template_name = 'adr/adr_list.html'
    paginate_by = 20

    def get_queryset(self):
        return AdrCheck.objects.filter(user=self.request.user)

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['adr'] = context['adr'].filter(user=self.request.user)
        # context['count'] = context['adr'].filter(complete=False).count()
        # return context



class AdrDetailView(LoginRequiredMixin, DetailView):
    model = AdrCheck
    template_name = 'adr/adr_detail.html'
    context_object_name = 'adr'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adr = AdrCheck.objects.filter(id=self.kwargs.get('pk'))
        return context


# FormView to send PDF as Email to Saexinger. Or making a Kontakt form.


# Create your views here.
