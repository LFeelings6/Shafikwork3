from django.forms import ModelForm

from inventory.models import EquipmentCategory, Product,Transaction


class EquipmentCategoryForm(ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'        