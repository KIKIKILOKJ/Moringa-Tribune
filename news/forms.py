from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email=forms.EmailField(label='Email')
    
class NewsArticleForm(forms.ModelForm):
    class meta:
        model=Article
        exclude=['editor','pub_date']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }