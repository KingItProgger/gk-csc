from django import forms
from .models import Recall,Review


class RecallForm(forms.ModelForm):

    class Meta:
        model=Recall
        fields=['name','phone','message']
        widgets={
            'name':forms.TextInput(
              attrs={'placeholder':'Ваше имя','class':'recall-name'}
        ),
            'phone':forms.TextInput(
              attrs={'placeholder':'номер телефона','class':'recall-phone'}
          ),
            'message':forms.Textarea(
              attrs={'placeholder':'Ваш вопрос','cols':20,'rows':15,'class':'recall-text'}
          )
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model=Review
        fields=['username','message','mark','img']
        widgets={
            'username':forms.TextInput(
              attrs={'placeholder':'Ваше имя','class':'review-name'}
        ),
            'message':forms.Textarea(
              attrs={'placeholder':'Ваш отзыв','cols':20,'rows':15,'class':'review-message'}
          ),
            'mark':forms.Textarea(
              attrs={'placeholder':'оценка','class':'review-mark'}
          )
        }
