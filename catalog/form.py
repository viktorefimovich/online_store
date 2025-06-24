from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


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
        exclude = ("created_at", "updated_at",)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name in self.fields.keys():

            if field_name == "description":
                self.fields[field_name].widget.attrs.update({
                    "class": "form-control",
                    "rows": 3
                })

            else:
                self.fields[field_name].widget.attrs.update({
                    "class": "form-control"
                })

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
