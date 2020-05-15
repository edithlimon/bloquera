# Generated by Django 3.0.4 on 2020-05-14 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_M_Inventario',
            fields=[
                ('IDProducto', models.CharField(help_text='Ingrese su Clave de Producto', max_length=30, primary_key=True, serialize=False)),
                ('IDTipoProducto', models.CharField(default='PRODUCTO TERMINADO', max_length=30)),
                ('NombreProducto', models.CharField(max_length=150)),
                ('IDFoto', models.ImageField(max_length=110, null=True, upload_to='Pictures')),
                ('FechaAlta', models.DateTimeField(default=django.utils.timezone.now)),
                ('UnidadMedida', models.CharField(max_length=10)),
                ('ExistenciaActual', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11)),
                ('ExistenciaMaxima', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11)),
                ('ExistenciaMinima', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11)),
                ('Observaciones', models.CharField(max_length=150)),
                ('DiasPromedioResurtimiento', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('Produccionmaxdia', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('CostoUnitarioultimaProducción', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('Preciocostoultimacompra', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('Preciovtaultimaproduccion', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('Preciovtaunitarioultimaproduccion', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('Status', models.CharField(default='VIGENTE', max_length=20)),
                ('ctlusuario', models.CharField(max_length=30)),
                ('ctlFecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_M_MovtosInventario',
            fields=[
                ('IDPeriodo', models.IntegerField(help_text='Ingrese 99-mes-99anio')),
                ('IDMovimiento', models.IntegerField(help_text='Consecutivo numerico')),
                ('IDProducto', models.CharField(help_text='Ingrese su Clave de Producto', max_length=30, primary_key=True, serialize=False)),
                ('IDPlanProducción', models.CharField(help_text='Ingrese su Clave dePlan produccion recomendacion ddmmaa', max_length=30)),
                ('IDVentaIDMovimiento', models.IntegerField(help_text='Consecutivo del maestro de ventas')),
                ('IDCompra', models.IntegerField(help_text='Consecutivo del maestro de compras')),
                ('IDTipoMovimiento', models.IntegerField(help_text='SOLO ELIGE TIPO MOVIMIENTO')),
                ('FechaMovto', models.DateTimeField(default=django.utils.timezone.now)),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2)),
                ('Observaciones', models.CharField(max_length=150)),
                ('IdEmpleado', models.CharField(max_length=30)),
                ('ctlusuario', models.CharField(max_length=30)),
                ('ctlfecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]