from django import forms
from .models import Post, Profile, Comment
from django.contrib.auth.models import User



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
            'restrict_comment',
        )






class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
            'restrict_comment',
        )


class ContactForm(forms.Form):
    # first_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs = {'placeholder': 'First Name*'}))
    # last_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs = {'placeholder': 'Last Name*'}))
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs = {'placeholder': 'Your Name*'}))
    email = forms.EmailField(required=True, max_length=250, widget=forms.TextInput(attrs = {'placeholder': 'Your Email*'}))
    subject = forms.CharField(required=True, max_length=450, widget=forms.TextInput(attrs = {'placeholder': 'Subject*'}))
    message = forms.CharField(widget=forms.Textarea(attrs = {'placeholder': 'Your Message*'}), required=True)


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs = {'placeholder':'Enter Username Here'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs ={'placeholder':'Enter Password Here'} ))


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(widget = forms.EmailInput(attrs = {'placeholder':'Unchangeable Email'}))
    username= forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Unchangeable Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)



class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'row': '4', 'cols': '50'}))
    class Meta:
        model = Comment
        fields = ('content',)