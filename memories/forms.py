from django import forms

from .models import Memory


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ["comments", "place_name", "latitude", "longitude"]
        widgets = {
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }
