from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import *

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_true = [form.cleaned_data.get('is_main') for form in self.forms].count(True)
        if count_true < 1:
            raise ValidationError('Укажите основной раздел')
        elif count_true > 1:
            raise ValidationError('Основным может быть только один раздел !!!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass