from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.db.models import Sum
from .forms import EntrepriseForm,UserEntrepriseForm
from .models import Entreprise
from django.urls import reverse_lazy
from django.db import transaction

class create(CreateView):
    model = Entreprise
    form_class=EntrepriseForm
    success_url = reverse_lazy('entreprise-index')
    template_name = "entreprise/create.html"

    def form_invalid(self, form):
        invalid_fields = [field for field in form if field.errors]
        invalid_field_names = [field.name for field in invalid_fields]  
        print("Champs invalides par nom :", invalid_field_names)
        return self.render_to_response(
            self.get_context_data(form=form, invalid_fields=invalid_fields)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context["form"] =  EntrepriseForm()
        else:
            context["form"] =  UserEntrepriseForm()
        return context

    @transaction.atomic
    def form_valid(self, form):
        return super().form_valid(form)
    


class index(ListView):
    model = Entreprise
    template_name = "entreprise/index.html"
    context_object_name = "entreprises"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context["entreprises"] =Entreprise.objects.all().order_by('-id') 
        return context
    

class edit(UpdateView):
    model = Entreprise
    template_name = "entreprise/edit.html"
    form_class = EntrepriseForm
    success_url = reverse_lazy('entreprise-index')

    def get_form_class(self):
        if self.request.user.is_staff:
            return EntrepriseForm
        else:
            return UserEntrepriseForm
        
class delete(DeleteView):
    model = Entreprise
    template_name = "entreprise/edit.html"
    form_class = EntrepriseForm
    success_url = reverse_lazy('entreprise-index')


