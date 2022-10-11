from django import forms


class ScanForm(forms.Form):
    """Add a job for instant check from homepage"""
    url = forms.URLField(label='url', max_length=300)
