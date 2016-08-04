from django import forms

from easy_select2.widgets import Select2Mixin

class Select2TextInput(Select2Mixin, forms.TextInput):
    """
    A Select2-enabled combo box for non-choice fields which can
    provide a list of pre-set choices, or can accept arbitrary input.
    To use this, do NOT set a *choices* attribute on the model field,
    but DO supply a *data* attribute to select2attrs that contains a
    list of dictionaries each having at least an *id* and *text*
    terms like so::
      form.fields['myfield'].widget = Select2TextInput(
          select2attrs={
              'data': [ {'id': 'your data', 'text': 'your data'}, ... ],
          },
      )
    """
    pass
