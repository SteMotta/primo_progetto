from django.db import models

class Giornalista(models.Model):
    """ Modello generico di un giornalisa """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + ' ' + self.cognome

class Articolo(models.Model):
    """ Modello generico di un articolo di news """
    titolo = models.CharField(max_length=20)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name='articoli')

    def __str__(self):
        return self.titolo
