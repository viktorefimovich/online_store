from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-basic'
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs['class'] = 'form-control datepicker'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-time'
            elif isinstance(field.widget, forms.widgets.SelectMultiple):
                field.widget.attrs['class'] = 'form-control select2 select2-multiple'
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = 'form-control select2'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    BAD_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар"
    ]

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "owner", "checkbox")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return price

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in self.BAD_WORDS:
            if word in name.lower() or word in description.lower():
                raise ValidationError(f"Продукт содержит запрещенное слово {word}")
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta(ProductForm.Meta):
        model = Product
        fields = "__all__"
        exclude = ("created_at", "updated_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "checkbox":
                field.widget.attrs["readonly"] = True
