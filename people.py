class SuperHuman:
	name = ''
	race =''
	sex = ''
	def __init__(self, Aname,Arace,Asex):
		self.name = Aname
		self.race = Arace
		self.sex = Asex

	def card(self):
		print("Jestem pierwszym czlowiekiem, mam na imie " + self.name + " moja rase to " + self.race + ". moja plec to " + self.sex)


class Human(SuperHuman):
	parents = []
	sibling = []	
	profession = 'Bezrobotny'
	def __init__(self, Aname, Aparent1, Aparent2, Arace, Asex):
		self.name = Aname
		self.parents.append(Aparent1)
		self.parents.append(Aparent2)
		self.race = Arace
		self.sex = Asex
	def card(self):
		print("Jestem zwyklym czlowiekiem, mam na imie "+self.name)
		print("Moi rodzice: ")
		self.parents[0].card()
		self.parents[1].card()
		print("Moja rasa to: "+self.race)
		print("Moja plec to: "+self.sex)
		print("Moja profesja to: "+self.profession)

adam =  SuperHuman('adam', 'white', 'male')
ewa =  SuperHuman('ewa', 'white', 'female')

antek = Human('antek', adam, ewa, 'white', 'male')

antek.card()
print()
adam.card()



antek.profession = 'stolarz'
print('Antek dorobil sie profesji')


