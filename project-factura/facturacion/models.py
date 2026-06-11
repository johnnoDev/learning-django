from django.db import models

# Create your models here.

# Tabla Cliente
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
   
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
    class Meta:
        db_table = 'clientes'

# Tabla Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        db_table = 'productos'
    
# Tabla Factura
class Factura(models.Model):
    """
    Esto no es un campo de la base de datos, sino una constante (una lista de tuplas) de Python. 
    Sirve para definir opciones cerradas. El primer valor de cada tupla (ej. 'pendiente') es lo que 
    se guardará internamente en la base de datos, y el segundo valor ('Pendiente') es el nombre legible 
    que verá el usuario en formularios o en el panel de administración.
    """
    ESTADOS = [('pendiente', 'Pendiente'), ('pagada', 'Pagada'), ('anulada', 'Anulada')]

    id_factura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.PROTECT
    )
    fecha = models.DateField(auto_now_add=True) # Asignar fecha automatica
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuesto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    class Meta:
        db_table = 'facturas'

# Tabla DetalleFactura (Tabla intermedia)
class DetalleFactura(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
  
    class Meta:
        db_table = 'detalle_factura'