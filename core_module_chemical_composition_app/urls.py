""" Url router for the chemical composition module
"""

from django.urls import re_path

from core_module_chemical_composition_app.views import ChemicalCompositionModule

urlpatterns = [
    re_path(
        r"module-chemical-composition",
        ChemicalCompositionModule.as_view(),
        name="core_module_chemical_composition",
    ),
]
