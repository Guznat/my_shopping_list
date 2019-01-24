from django import forms


class ListForm(forms.Form):
    name = forms.CharField(max_length=180,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter your product here.',
                                      'aria-label': 'Shopping List', 'aria-describedby': 'add-btn'}))
