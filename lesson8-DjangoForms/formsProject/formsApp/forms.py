from django import forms 
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField()
    description = forms.CharField(widget = forms.Textarea())

    def msg(self):
        return f"Hello {self.name}, your message has been sent"