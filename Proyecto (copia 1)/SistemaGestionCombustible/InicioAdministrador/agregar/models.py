# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Combustible(models.Model):
    idcombustible = models.IntegerField(primary_key=True)
    nombrec = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'combustible'
        
    def __str__(self):
        return '{}'.format(self.nombrec)


class Departamento(models.Model):
    iddepartamento = models.IntegerField(primary_key=True)
    nombred = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'departamento'
    
    def __str__(self):
        return '{}'.format(self.nombred)


class Estacion(models.Model):
    nombree = models.CharField(primary_key=True, max_length=40,)
    idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='idmunicipio')

    class Meta:
        managed = False
        db_table = 'estacion'

    def __str__(self):
        return '{}'.format(self.nombree)

class Municipio(models.Model):
    idmunicipio = models.IntegerField(primary_key=True)
    iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='iddepartamento')
    nombrem = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'municipio'

    def __str__(self):
        return '{}'.format(self.nombrem)

class Registro(models.Model):
    idregistro = models.AutoField(primary_key=True)
    nombree = models.ForeignKey(Estacion, models.DO_NOTHING, db_column='nombree')
    idcombustible = models.ForeignKey(Combustible, models.DO_NOTHING, db_column='idcombustible')
    idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='idservicio')
    fecharegistro = models.DateField()
    preciocombustible = models.DecimalField(max_digits=10, decimal_places=2)
    precioreferencia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'registro'

    def __str__(self):
        return '{}''{}''{}'.format(self.fecharegistro,self.preciocombustible,self.precioreferencia)


class Servicio(models.Model):
    idservicio = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        return '{}'.format(self.nombres)