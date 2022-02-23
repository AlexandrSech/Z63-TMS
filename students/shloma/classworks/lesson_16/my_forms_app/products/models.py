from django.db import models
from django.core.validators import MinValueValidator


class Products(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Name",
                            verbose_name="Product name",
                            null=False)

    supplier = models.CharField(max_length=100,
                                help_text="Supplier",
                                verbose_name="Supplier name",
                                null=True,
                                blank=True)

    current_amont = models.IntegerField(help_text="Current amount",
                                        verbose_name="Current amount",
                                        validators=[MinValueValidator(0)])

    update_date = models.DateTimeField(auto_now_add=True,
                                       help_text="Update date",
                                       verbose_name="Date of update")

    def __str__(self):
        return f"{self.name} ({self.current_amont})"
