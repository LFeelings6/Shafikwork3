from django.db import migrations,models

class Migration(migrations.Migration):
    initial = True
    dependences = [

    ]

    Operations = [
       migrations.CreateModel(
           name ='EquipmentCategory',
           fields = [
               ('id', models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
               ('name',models.CharField(max_length=50)),
               ('description',models.CharField(max_length=10)),
               ('date_created',models.DateField()),
           ],
       ),
       
   ] 

