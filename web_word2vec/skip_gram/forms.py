from django import forms

CHOICES = (
    (5, "Five"),
    (10, "Ten"),
    (15, "Fifteen"),
    (20, "Twenty")
)


class WordForm(forms.Form):
    word = forms.CharField(required=True, label='Enter word')
    num_word = forms.ChoiceField(required=True, label='Choose number of most similar words', choices=CHOICES)
