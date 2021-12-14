from Autor import Autor

class Livro:

	def __init__(self, id_livro, titulo, id_autor, nome):
		self.id_livro = id_livro
		self.titulo = titulo
		self.proximo = None
		self.autor = Autor(id_autor, nome)

