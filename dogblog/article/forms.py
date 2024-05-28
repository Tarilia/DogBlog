from django import forms

from dogblog.article.models import Article


class CreateArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["slug", "title", "content", "photo",
                  "is_published", "cat", "tags"]
