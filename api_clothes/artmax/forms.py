from django.core.exceptions import ValidationError

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill

    def clean(self):
        cleaned_data = super(BillForm, self).clean()
        if cleaned_data.get('card') and cleaned_data.get('survey'):
            raise ValidationError(u'Нужно выбрать что-то одно')
        return cleaned_data


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    form = BillForm