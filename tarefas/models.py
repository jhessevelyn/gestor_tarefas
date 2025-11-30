from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
        ('atrasada', 'Atrasada'),])
    prioridade = models.CharField(max_length=10, choices=[
        ('minima', 'Mínima'),
        ('baixa', 'Baixa'),
        ('normal', 'Normal'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),])
    data_limite = models.DateField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo