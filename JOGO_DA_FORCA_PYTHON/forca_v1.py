# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = [
"     +---+\n\
     |   |\n\
         |\n\
         |\n\
         |\n\
         |\n\
==========\n",
	
"     +---+\n\
     |   |\n\
     O   |\n\
         |\n\
         |\n\
         |\n\
==========\n",

"     +---+\n\
     |   |\n\
     O   |\n\
     |   |\n\
         |\n\
         |\n\
==========\n", 

"     +---+\n\
     |   |\n\
     O   |\n\
    /|   |\n\
         |\n\
         |\n\
==========\n",

"     +---+\n\
     |   |\n\
     O   |\n\
    /|\  |\n\
         |\n\
         |\n\
==========\n",

"     +---+\n\
     |   |\n\
     O   |\n\
    /|\  |\n\
    /    |\n\
         |\n\
==========\n", 

"     +---+\n\
     |   |\n\
     O   |\n\
    /|\  |\n\
    / \  |\n\
         |\n\
==========\n"]

# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.hidden_word = ['_' for i in range(len(word))]
		self.points = 0
		self.negative_points = 0
		self.intro = "---------- Hangman Game ----------"
		
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			print("\nBoa!!! Essa tá certa :)")
			self.hide_word(letter, 0)
		else:
			self.negative_points += 1
			print("\nHmm, não foi dessa vez...\nTente com outra letra\n")
			self.hide_word(letter)
		
	# Método para verificar se o jogador venceu
	def hangman_won(self, signal = 0):
		if signal == 0:
			return True if self.points == len(self.word) else False
		else: return True
	# Método para não mostrar a letra no board
	def hide_word(self, letter, signal=1):		
		if signal == 0:
			for i in range(len(self.hidden_word)):
				if letter == self.word[i]:
					self.hidden_word[i] = letter
					self.points += 1

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self, ng_pts):
		print(board[ng_pts])

	# Método para revelar cada ocorrencia da letra certa na string escondida
	def print_hidden_word(self):
		for i in range(len(self.hidden_word)):
			print(self.hidden_word[i], end='')
		print()

	def check_word(self, word):
		return True if self.word == word else False

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while(game.points < len(game.word) and game.negative_points < 6):

		game.print_game_status(game.negative_points)	
		print("Sua palavra é: ", end='')
		game.print_hidden_word()
		
		letter = input("\nPor favor, digite uma letra ou palavra que você ache ser a certa: ")
		
		#validando a entrada
		
		if game.check_word(letter): break
	
		while(len(letter) > 1 and letter != game.word):
			print("\nHmmm... Acho que você errou a palavra.\nTente enviar uma letra ou outra palavra que ache ser a certa")
			letter = input("")	
		
		if game.check_word(letter): break

		game.guess(letter)

		print("################################\n")

	# De acordo com o status, imprime mensagem na tela para o usuário
	game.print_game_status(game.negative_points)
	if game.check_word(letter):
		game.hangman_won(1)
		print ('\nUAU!!! Você conseguiu acertar a palavra inteira :)')
	elif game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word.upper()) 
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
