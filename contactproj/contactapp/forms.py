from django import forms

# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=30)
#     mobile=forms.IntegerField()
#     email=forms.EmailField(max_length=30)
#     location=forms.CharField(max_length=30)
#     course=forms.CharField(max_length=30)


class ContactForm(forms.Form):
    name  = forms.CharField(label="Enter the Name",max_length=20, widget=forms.TextInput(attrs = {'placeholder': 'Name','class':'form-control'}))
    mobile= forms.IntegerField(label="Enter the mobile no",widget=forms.TextInput(attrs = {'placeholder': 'Mobile Number','class':'form-control'}))
    email= forms.EmailField(label="Enter the Email",max_length=20, widget=forms.EmailInput(attrs = {'placeholder': 'email','class':'form-control'}))
    location= forms.CharField(label="Enter the Location",max_length=75, widget=forms.TextInput(attrs = {'placeholder': 'location','class':'form-control'}))
    course= forms.CharField(label="Enter the course",max_length=75, widget=forms.TextInput(attrs = {'placeholder': 'course','class':'form-control'}))
    