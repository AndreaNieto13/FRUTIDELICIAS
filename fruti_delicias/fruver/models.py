from django.db import models

class Categorias(models.Model): 
    cate_id = models.AutoField(primary_key=True)
    cate_desc = models.CharField(verbose_name="Descripcion",max_length=100)
    cate_estado = models.TextField(verbose_name="Estado", max_length=100)
    
    def __str__(self):
        fila = "Nombre: " + self.cate_desc + " - " + "Estado : " + self.cate_estado
        return fila

class Productos(models.Model): 
    prod_id = models.AutoField(primary_key=True)
    prod_desc = models.CharField(verbose_name="Descripcion",max_length=100)
    prod_vu= models.TextField(verbose_name="Valor unitario", max_length=100)
    prod_estado = models.TextField(max_length=2, verbose_name="Estado")
    cate_id = models.ForeignKey(Categorias, on_delete=models.CASCADE,verbose_name="Categoria")
   
    def __str__(self):
        fila = "Nombre: " + self.prod_desc + " - " + "Estado : " + self.prod_estado
        return fila
    

