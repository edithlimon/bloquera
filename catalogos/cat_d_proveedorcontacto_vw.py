from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .cat_d_proveedorcontacto_forms import frmCat_D_ProveedorContacto as base_form
from .models import Cat_D_ProveedorContacto as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from zend_django.parametros_models import ParametroUsuario

def template_base_path(file):
    return 'catalogos/cat_d_proveedorcontacto/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Proveedores_contactos"
    titulo_descripcion = "Contactos Proveedores"
    main_data_model = main_model
    model_name = "cat_d_proveedorcontacto"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDProveedor__icontains=search_value) | Q(NombreContacto__icontains=search_value)))
    def get(self, request, pkcliente):
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
            return self.base_render(
                request, self.get_data(pkcliente, search_value), search_value)

    def post(self, request, pkcliente):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pkcliente, search_value), search_value)

class Read(GenericRead):
    titulo_descripcion = "Proveedor_contacto"
    model_name = "cat_d_proveedorcontacto"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Proveedores_contactos"
    model_name = 'cat_d_proveedorcontacto'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Proveedores_contactos"
    model_name = "cat_d_proveedorcontacto"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_d_proveedorcontacto"
    main_data_model = main_model