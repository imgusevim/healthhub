from . models import EatingList
from django.forms import ModelForm

class EatingListForm(ModelForm):

    class Meta:
        model = EatingList
        fields = ['username','date','breakfast','lunch','dinner','snack']