from django.db import models

# Create your models here.


class Mago(models.Model):

    Name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    id = models.CharField(max_length=10, primary_key=True)
    magic_aff = models.CharField(max_length=255)
    age = models.IntegerField()
    estado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"""id: {self.id},Name:{self.Name}, Lastname: {self.lastname},
          age: {self.age}, Magic_affinity: {self.magic_aff}"""


class Grimorio(models.Model):
    grimo = models.CharField(max_length=255)
    front = models.CharField(max_length=255)
    mago_id = models.ForeignKey(
        Mago, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"""id: {self.mago_id },Grimo: {self.grimo},Front: {self.front}
        """
