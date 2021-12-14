from Livro import Livro

class Fila:

	def __init__(self):
			self.inicio = None
			self.fim = None
			self.tamanho = 0


	def adicionar(self, id_livro, titulo, id_autor, nome):
		livro = Livro(id_livro, titulo, id_autor, nome)
		if self.tamanho == 0:
			self.inicio = livro
			self.fim = livro

		else:
			self.fim.proximo = livro
			self.fim = livro
		self.tamanho += 1
		self.imprimir()


	def imprimir(self):
		texto = ""
		if self.inicio == None :
			texto = "Fila Vazia!"
		else:
			aux = self.inicio
			while ( aux ) :
				texto = texto + str(aux.titulo ) + str( aux.autor.nome) + "  -  "
				aux = aux.proximo
		print( texto )
		print(" ---------------------------------------------------")


	def remover(self):
		if self.tamanho == 0:
			print( "Fila Vazia!")
		elif self.tamanho == 1:
			self.inicio = None
			self.fim = None
			self.tamanho = 0
		else:
			self.inicio = self.inicio.proximo
			self.tamanho -= 1
		self.imprimir()

