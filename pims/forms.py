from django.forms import ModelForm
from .models import Record

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['user', 'specialist', 'patient_name', 'birthday', 'gender', 'tel_number', 'address', 'condition', 'image1', 'image2', 'image3']


from django import forms
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class ContactForm(forms.Form):
    subject = forms.CharField(
        label="件名",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "件名",
            }
        )
    )
    email = forms.EmailField(
        label="メールアドレス",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@example.com",
            }
        )
    )
    message = forms.CharField(
        label="問い合わせ内容",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "問い合わせ内容"
            }
        )
    )

    def send_email(self, username, email):
        subject = "【お問い合わせ】" + self.cleaned_data["subject"]
        message = (
            f"問い合わせ内容:\n{self.cleaned_data['message']}\n\n"
            f"送信者情報:\n"
            f"ユーザー名: {username}\n"
            f"フォームで入力したメールアドレス: {self.cleaned_data['email']}"
        )
        email_from = self.cleaned_data["email"]
        recipient_list = ["briandjangotesting@gmail.com"]

        try:
            send_mail(subject, message, email_from, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")


