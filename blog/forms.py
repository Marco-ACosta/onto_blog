from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(label="Comentário:", widget=forms.Textarea )
    post_id = forms.IntegerField(widget=forms.HiddenInput)