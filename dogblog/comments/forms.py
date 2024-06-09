from django import forms

from dogblog.comments.models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]
