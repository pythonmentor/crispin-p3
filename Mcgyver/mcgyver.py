


# -tc- attention à structurer les imports en conformité avec la PEP8

import random

import json

import pygame
from pygame.locals import *

import time


# -tc- structurer le projet avec une classe par module en séparant les classes de logique et les classes
# -tc- d'interface dans des packages séparer. Partager les classes de logique entre la version terminal 
# -tc- et la version gui du jeu.



class DrawConsole: # -tc- une classe n'est pas une action. De manière générale, attention à la PEP 8 et à la PEP 257

	"""docstring for DrawConsole""" # -tc- être plus descriptif dans ses docstrings

	def __init__(self, hero , liste_objets , sortie , mur): # -tc- passer des objets représentants le hero et le plateau de jeu

		self.liste_positions_objets = []

		for i0 in liste_objets :
			
			self.liste_positions_objets.append( i0.position )


		screen = ''

		for i0 in range( 15 + 2 ): # -tc- ne pas définir en dur la taille du labyrinthe. La déduire de la structure
			
			for i1 in range( 15 + 2 ):
				

				if hero == ( i1 , i0 ) :
					
					screen += ' M '

				elif ( i1 , i0 ) in self.liste_positions_objets :

					#screen += ' O # -tc- manque un guillemet


					if liste_objets[ self.liste_positions_objets.index( ( i1 , i0 ) ) ].nom_objet == 'aiguille' :
						
						screen += ' I '

					elif liste_objets[ self.liste_positions_objets.index( ( i1 , i0 ) ) ].nom_objet == 'tube_plastiqe' :
						
						screen += ' T '

					elif liste_objets[ self.liste_positions_objets.index( ( i1 , i0 ) ) ].nom_objet == 'ether' :
						
						screen += ' E '


				elif sortie == ( i1 , i0 ) :
					
					screen += ' S '

				elif ( i1 , i0 ) in mur :

					screen += ' X '

				#elif  ( ( i1 , i0 ) in aiguille.route_mg ) or ( ( i1 , i0 ) in tube_plastiqe.route_mg ) or ( ( i1 , i0 ) in ether.route_mg ) or ( ( i1 , i0 ) in sortie.route_mg )  :
				#
				#	screen += ' . '

				else :

					screen += '   '


			screen += '\n'



		print( screen )

                # -tc- à formater correctement. Pas très orienté objet mais fait globalement le job





class Plateau:

	"""docstring for Plateau""" # -tc- être plus descriptif et attention à la pep8

	def __init__( self , taille_plateau ): # -tc- passer un objet représentant le plateau de jeu 

		self.plateauvide = []
		
		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				self.plateauvide.append( ( i1 , i0 ) )

		with open("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/structure.json", "r") as read_file:

			data = json.load(read_file)

		self.mur = []

		for i0 in data[ 0 ]:
		 	
		 	self.mur.append( tuple( i0 ) ) # -tc- ce qui nous nous intéresse plus que les murs , c'est les chemins. Nommer la liste au pluriel




	def initialisemur( self , taille_plateau , route1 , route2 , route3 , route4 ): # -tc- pourquoi tous ces paramètres inutiles?

		self.mur = [] # -tc- l'objectif de cette méthode n'est pas clair

		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				if ( ( i1 , i0 ) in route1 ) or ( ( i1 , i0 ) in route2 ) or ( ( i1 , i0 ) in route3 ) or ( ( i1 , i0 ) in route4 ) :

					pass

				else :

					if random.randrange( 2 ) == 0 :

						self.mur.append( ( i1 , i0 ) )

					else :

						pass


	def move_posible( self , point , champs_libres ): # -tc- inutilement compliqué et répétitif. On peut décider si un mouvement est possible en une ligne. De manière générale, si une méthode fait plus de 20 lignes: factoriser 

		mov_posible = []

		#   Les coins
		
		if point == ( 0 , 0 ) or point == ( 0 , 15 - 1 ) or point == ( 15 - 1 , 0 ) or point == ( 15 - 1 , 15 - 1 ) :
			
			#  coin bas gauche

			if point == ( 0 , 0 ) :

				if ( 1 , 0 ) in champs_libres:

					mov_posible.append( ( 1 , 0 ) )

				if ( 0 , 1 ) in champs_libres :
					
					mov_posible.append( ( 0 , 1 ) )

			# coin haut gauche

			elif point == ( 0 , 15 - 1 ) :

				if ( 0 , (15 - 1) - 1 ) in champs_libres:

					mov_posible.append( ( 0 , (15 - 1) - 1 ) )

				if ( 1 , 15 - 1 ) in champs_libres :
					
					mov_posible.append( ( 1 , 15 - 1 )  )

			# coin bas droit

			elif point == ( 15 - 1 , 0 ) :

				if ( (15 - 1) - 1 , 0 ) in champs_libres:

					mov_posible.append( ( (15 - 1) - 1 , 0 ) )

				if ( 15 - 1 , 1 ) in champs_libres:
					
					mov_posible.append( ( 15 - 1 , 1 ) )

			# coin haut droit

			elif point == ( 15 - 1 , 15 - 1 ) :

				if ( (15 - 1) - 1 , 15 - 1 ) in champs_libres:

					mov_posible.append( ( (15 - 1) - 1 , 15 - 1 ) )

				if ( 15 - 1 , (15 - 1) - 1 ) in champs_libres :
					
					mov_posible.append( ( 15 - 1 , (15 - 1) - 1 ) )

		# Les extrémités

		elif ( point[0] == 0 ) or ( point[0] == 15 - 1 ) or ( point[1] == 0 ) or ( point[1] == 15 - 1 ) :
			
			#extrémités gauches

			if  point[0] == 0 :
				
				if ( 0 , point[1] + 1 ) in champs_libres :

					mov_posible.append( ( 0 , point[1] + 1 ) );

				if ( 1 , point[1] ) in champs_libres :

					mov_posible.append( ( 1 , point[1] ) );

				if ( 0 , point[1] - 1 ) in champs_libres  :

					mov_posible.append( ( 0 , point[1] - 1 ) );

			#extrémités droits

			elif ( point[0] == 15 - 1 ) :

				if ( point[0] - 1 , point[1] ) in champs_libres :

					mov_posible.append( ( point[0] - 1 , point[1] ) )

				if ( point[0] , point[1] - 1 ) in champs_libres :

					mov_posible.append( ( point[0] , point[1] - 1 ) )

				if ( point[0] , point[1] + 1 ) in champs_libres :

					mov_posible.append( ( point[0] , point[1] + 1 ) )

			#extrémités bas

			elif ( point[1] == 0 ) :

				if ( point[0] - 1 , point[1] ) in champs_libres :

					mov_posible.append( ( point[0] - 1 , point[1] ) )

				if ( point[0] + 1 , point[1] ) in champs_libres :

					mov_posible.append( ( point[0] + 1 , point[1] ) )

				if ( point[0] , point[1] + 1 ) in champs_libres :

					mov_posible.append( ( point[0] , point[1] + 1 ) )

			#extrémités hauts

			elif ( point[1] == 15 - 1 ) :

				if ( point[0] - 1 , point[1] ) in champs_libres :

					mov_posible.append( ( point[0] - 1 , point[1] ) )

				if ( point[0] + 1 , point[1] ) in champs_libres :

					mov_posible.append( ( point[0] + 1 , point[1] ) )

				if ( point[0] , point[1] - 1 ) in champs_libres :

					mov_posible.append( ( point[0] , point[1] - 1 ) )


		# le reste

		else : 
			
			if ( point[0] - 1 , point[1] ) in champs_libres :

				mov_posible.append( ( point[0] - 1 , point[1] ) )

			if ( point[0] + 1 , point[1] ) in champs_libres :

				mov_posible.append( ( point[0] + 1 , point[1] ) )

			if ( point[0] , point[1] - 1 ) in champs_libres :

				mov_posible.append( ( point[0] , point[1] - 1 ) )

			if ( point[0] , point[1] + 1 ) in champs_libres :

				mov_posible.append( ( point[0] , point[1] + 1 ) )


		return( mov_posible )


	def mur_to_champs_libres( self , mur , position_sortie ): # -tc- avec une description complète du labyrinthe dès le départ, cela n'est normalement pas nécessaire


		champs_libres = []

		for i0 in range( 15 ): # -tc- éviter de coder la taille en dur
			
			for i1 in range( 15 ):
				
				if ( ( i1 , i0 ) not in mur ) and ( i1 , i0 ) != position_sortie  :

					champs_libres.append( ( i1 , i0 ) )

		return( champs_libres )


	def movables_in_champs_libres( self , i , movables  , champs_libres ): # -tc- quel est l'objectif?


		return( len( self.move_posible( movables[ i ] , champs_libres ) ) )



class Sortie:

	"""docstring for Sortie"""

	def __init__( self , taille_plateau ):

		#self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.route_mg = []

		with open( "/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/structure.json" , "r") as read_file:

			data = json.load(read_file)

		self.position = tuple( data[ 2 ] )
		


class Heros: # -tc- le nom d'une classe est généralement au singulier

	"""docstring for Heros"""

	def __init__( self , taille_plateau ):

		#self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		with open( "/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/structure.json" , "r") as read_file:

			data = json.load(read_file) # -tc- pourquoi on lit une seconde fois le fichier

		self.position = tuple( data[ 1 ] )

		self.objet_ramasse = [] ;

		#print( self.position )

	def pas_mcgyver( self , direction ):

		if direction == 'j' :

			self.new_pos = ( self.position[0] - 1 , self.position[1] )
		
		elif direction == 'l' :

			self.new_pos = ( self.position[0] + 1 , self.position[1] )

		elif direction == 'k' :

			self.new_pos = ( self.position[0] , self.position[1] + 1 )

		elif direction == 'i' :

			self.new_pos = ( self.position[0] , self.position[1] - 1 )

		else:

			self.new_pos = ( self.position[0] , self.position[1] )

			print( 'Sélectionner une direction valide !!' ) # -tc- éviter les print dans une classe de logique

		return( self.new_pos )



class Gardien:

	"""docstring for Gardien"""
	
	def __init__( self , taille_plateau ):

		#self.position = ( 0 , 0)

		with open( "/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/structure.json" , "r") as read_file:

			data = json.load(read_file) # -tc- inutile de lire plusieurs fois le fichier alors qu'une lecture en une seule passe suffit

		self.position = tuple( data[ 2 ] )



# -tc- ne pas mettre de code au niveau global du module. Utiliser des classes + une fonction main() pour démarrer le jeu
		
plateau0 = Plateau( 15 )

mg0 = Heros(15)

sortie0 = Sortie(15)

gardien0 = Gardien(15)

position_objets_ramasse = []





class ObjetsRamasses: # -tc- essaie

	"""docstring for Objets"""

	def __init__( self , taille_plateau , nom_de_lobjet ):


		champs_libres = plateau0.mur_to_champs_libres( plateau0.mur , sortie0.position )

		champs_libres0 = list( champs_libres )

		movables = [ mg0.position ]


		#print( ' les movables avant ' , movables )

		#print( ' champs libre avant ' , champs_libres0 )

		
		i0 = 0 ;

		while i0 < len( movables ) :

			for i1 in plateau0.move_posible( movables[ i0 ] , champs_libres0 ) :

				movables.append( i1 )

				champs_libres0.remove( i1 )

			i0 += 1

		champs_accessibles = list( movables )

		champs_accessibles.remove( mg0.position )

		random.shuffle( champs_accessibles )


		if len( champs_accessibles ) < 3 :

			self.position = ( -1 , -1 )
			
			print( 'ce tableau ne permet pas de placer 3 objets accessible par McGyver !!' )

		else :

			#print( ' champs libre apres ' , champs_libres0 )

			#print( ' les movables apres ' , movables )

			while ( champs_accessibles[0] in position_objets_ramasse ):

				random.shuffle( champs_accessibles )

			self.position = champs_accessibles[ 0 ]

			position_objets_ramasse.append( champs_accessibles[ 0 ] )


			#self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )


		self.route_mg = []

		self.nom_objet = nom_de_lobjet

		print( ' champs_accessibles : ' ,  champs_accessibles )
		print( ' position de mcgyver : ' , mg0.position )
		print( ' position de ' + self.nom_objet + ' : ' , self.position )

	def ramassage( self ):
		
		self.position = ( -1 , -1 )
		
	


aiguille0 = ObjetsRamasses( 15 , 'aiguille' )

tube_plastiqe0 = ObjetsRamasses( 15 , 'tube_plastiqe' )

ether0 = ObjetsRamasses( 15 , 'ether' )







	


class Ligne(object):

	"""docstring for Ligne"""

	pass









class Pas:

	"""docstring for Pas"""

	def __init__( self ):
		
		pass


	def make_pas( self , curseur , cible ):
		
		#curseur_intermediaire = ( curseur[0] + 2 , curseur[1] + 2 )

		

		curseur_intermediaire = curseur

		
		if curseur == cible :
			
			print( 'le curseur est sur la cible' )

		elif curseur[0] == cible[0] :

			if cible[1] > curseur[1] :

				curseur_intermediaire = ( curseur[0] , curseur[1] + 1 )


			elif cible[1] < curseur[1] :

				curseur_intermediaire = ( curseur[0] , curseur[1] - 1 )



		elif curseur[1] == cible[1] :

			if cible[0] > curseur[0] :

				curseur_intermediaire = ( curseur[0] + 1 , curseur[1] )
				 

			elif cible[0] < curseur[0] :

				curseur_intermediaire = ( curseur[0] - 1 , curseur[1] )
				 



		else :


			if random.randrange( 2 ) == 0 :
				
				if cible[0] > curseur[0] :

					curseur_intermediaire = ( curseur[0] + 1 , curseur[1] )
					 

				elif cible[0] < curseur[0] :

					curseur_intermediaire = ( curseur[0] - 1 , curseur[1] )
					 

			else :

				if cible[1] > curseur[1] :

					curseur_intermediaire = ( curseur[0] , curseur[1] + 1 )
					 

				elif cible[1] < curseur[1] :

					curseur_intermediaire = ( curseur[0] , curseur[1] - 1 )
					 

		
		return ( curseur_intermediaire )	



	def make_pas_with_mur( self , curseur , cible  ):
		pass


#def test_initialise( position , tableau ):
	














def generate_structure():
	
	pas = Pas();

	plateau = Plateau(15)

	position_initialisee = []

	mg = Heros(15)

	position_initialisee.append( mg.position )





	aiguille = ObjetsRamasses( 15 , 'aiguille' )

	# Test si la position de l'aiguille est déjà occupée

	while aiguille.position in position_initialisee :
		
		aiguille = ObjetsRamasses( 15 , 'aiguille' )

	# Ajout de la position de l'aiguille dans la liste des positions occupées

	position_initialisee.append( aiguille.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	aiguille.route_mg.append( lepas )

	while lepas != aiguille.position :

		lepas = pas.make_pas( lepas , aiguille.position )

		aiguille.route_mg.append( lepas )

	#print( aiguille.route_mg )





	tube_plastiqe = ObjetsRamasses( 15 , 'tube_plastiqe' )

	# Test si la position du tube en plastiqe est déjà occupée

	while tube_plastiqe.position in position_initialisee :
		
		tube_plastiqe = ObjetsRamasses( 15 , 'tube_plastiqe' )

	# Ajout de la position du tube en plastiqe dans la liste des positions occupées

	position_initialisee.append( tube_plastiqe.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	tube_plastiqe.route_mg.append( lepas )

	while lepas != tube_plastiqe.position :

		lepas = pas.make_pas( lepas , tube_plastiqe.position )

		tube_plastiqe.route_mg.append( lepas )

	#print( tube_plastiqe.route_mg )





	ether = ObjetsRamasses( 15 , 'ether' )

	# Test si la position de l'ether est déjà occupée

	while ether.position in position_initialisee :
		
		ether = ObjetsRamasses( 15 , 'ether' )

	# Ajout de la position de l'ether dans la liste des positions occupées

	position_initialisee.append( ether.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	ether.route_mg.append( lepas )

	while lepas != ether.position :

		lepas = pas.make_pas( lepas , ether.position )

		ether.route_mg.append( lepas )

	#print( ether.route_mg )





	sortie = Sortie(15)

	# Test si la position de la sortie est déjà occupée

	while ( sortie.position in aiguille.route_mg ) or ( sortie.position in tube_plastiqe.route_mg ) or ( sortie.position in ether.route_mg ) :
		
		sortie = Sortie( 15 )

	# Ajout de la position de la sortie dans la liste des positions occupées

	position_initialisee.append( sortie.position )

	# Définition de la route que mcgyver emprunte pour atteindre la sorite

	lepas = mg.position

	sortie.route_mg.append( lepas )

	while lepas != sortie.position :

		lepas = pas.make_pas( lepas , sortie.position )

		sortie.route_mg.append( lepas )

	#print( 'sortie ' , sortie.route_mg )



	plateau.initialisemur( 15 , aiguille.route_mg , tube_plastiqe.route_mg , ether.route_mg , sortie.route_mg  )




	gardien = Gardien()

	gardien.position = sortie.position


	plateaujson = []

	for i0 in plateau.mur :
		
		plateaujson.append( list( i0 ) )

	#print( 'structure json : ' , plateaujson , list( mg.position ) , list(sortie.position) )

	return( [ plateau , mg , sortie , [ aiguille , tube_plastiqe , ether ] ] )
	






"""

	champs_libres = plateau.mur_to_champs_libres( plateau.mur , sortie.position )

	champs_libres0 = list( champs_libres )

	movables = [ mg.position ]

	print( plateau.movables_in_champs_libres( 0 , movables  , champs_libres0 ) )



"""

	
	





def jeu_console():
	

	while mg0.position != sortie0.position :

		DrawConsole( mg0.position , [ aiguille0 , tube_plastiqe0 , ether0 ] , sortie0.position , plateau0.mur)

		direction_input = input("Déplacer McGyver !! \n\n j : vers la gauche\n l : vers la droite\n k : vers le bas\n i : vers le haut\n\n ")

		if ( mg0.pas_mcgyver( direction_input ) not in plateau0.mur ) and ( mg0.pas_mcgyver( direction_input ) in plateau0.plateauvide ) :
			
			mg0.position = mg0.pas_mcgyver( direction_input )

			if mg0.position == aiguille0.position :

				mg0.objet_ramasse.append( aiguille0.nom_objet )

				aiguille0.ramassage()

			elif mg0.position == tube_plastiqe0.position :

				mg0.objet_ramasse.append( tube_plastiqe0.nom_objet )

				tube_plastiqe0.ramassage()

			elif mg0.position == ether0.position :

				mg0.objet_ramasse.append( ether0.nom_objet )

				ether0.ramassage()


	DrawConsole( mg0.position , [ aiguille0 , tube_plastiqe0 , ether0 ] , sortie0.position , plateau0.mur)

	if len( mg0.objet_ramasse ) == 3 :
		
		print('\n\n Gagné ')

	else:

		print('\n\n Perdu ')








def jeu_pygame():

	
	pygame.init()

	fenetre = pygame.display.set_mode((600,600), RESIZABLE )



	pygame_wall = []



	fond = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/fbc1.png").convert()
	fenetre.blit(fond, (0,0))



	#  Placement des murs

	for i0 in plateau0.mur :
		
		pygame_wall.append( pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/brique.png").convert() )

	#print( pygame_wall )

	for i1  in pygame_wall:
		
		fenetre.blit( i1 , ( plateau0.mur[ pygame_wall.index( i1 )][0] * 40 , plateau0.mur[ pygame_wall.index( i1 )][1] * 40 ) )
	



	#  Placement de McGyver et du gardien

	# McGyver
	py_mcgyver = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/mcgyver0.png").convert_alpha()
	fenetre.blit( py_mcgyver , ( mg0.position[0] * 40 , mg0.position[1] * 40 ) )

	# Gardien

	py_gardien = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/gardien1.png").convert_alpha()

	anneau_sortie = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/anneaurouge.png").convert_alpha()

	fenetre.blit( py_gardien , ( (gardien0.position[0] * 40) + 7.5 , ( gardien0.position[1] * 40 ) + 7.5 ) )	

	fenetre.blit( anneau_sortie , ( gardien0.position[0] * 40 , gardien0.position[1] * 40 ) )	

	

	# Placement des objets à ramasser

	anneau_objets = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()

	# aiguille
	py_aiguille0 = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/aiguille1.png").convert_alpha()
	fenetre.blit( py_aiguille0 , ( ( aiguille0.position[0] * 40 ) + 7.5 , ( aiguille0.position[1] * 40) + 7.5 ) )	
	fenetre.blit( anneau_objets , ( aiguille0.position[0] * 40 , aiguille0.position[1] * 40 ) )	

	# tube plastique
	py_tube_plastique0 = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/tube_plastique1.png").convert()
	fenetre.blit( py_tube_plastique0 , ( ( tube_plastiqe0.position[0] * 40 ) + 7.5 , ( tube_plastiqe0.position[1] * 40 ) + 7.5 ) )	
	fenetre.blit( anneau_objets , ( tube_plastiqe0.position[0] * 40 , tube_plastiqe0.position[1] * 40 ) )	

	# ether
	py_ether0 = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/ether1.png")
	fenetre.blit( py_ether0 , ( ( ether0.position[0] * 40 ) + 7.5 , ( ether0.position[1] * 40 ) + 7.5 ) )	
	fenetre.blit( anneau_objets , ( ether0.position[0] * 40 , ether0.position[1] * 40 ) )	





	pygame.display.flip()


	#while mg0.position != sortie0.position :

	#print( mg0.position )

	quitter = ''

	while mg0.position != gardien0.position :

		

		for event in pygame.event.get():

			if event.type == QUIT:

				quitter = 'q'

			if event.type == KEYDOWN:

				if event.key == 276:

					direction_input = 'j'

				elif event.key == 273:

					direction_input = 'i'

				elif event.key == 275:

					direction_input = 'l'

				elif event.key == 274:

					direction_input = 'k'

				else:

					direction_input = 'a'


				if ( mg0.pas_mcgyver( direction_input ) not in plateau0.mur ) and ( mg0.pas_mcgyver( direction_input ) in plateau0.plateauvide ) :
			
					mg0.position = mg0.pas_mcgyver( direction_input )

					if mg0.position == aiguille0.position :

						mg0.objet_ramasse.append( aiguille0.nom_objet )

						aiguille0.ramassage()

					elif mg0.position == tube_plastiqe0.position :

						mg0.objet_ramasse.append( tube_plastiqe0.nom_objet )

						tube_plastiqe0.ramassage()

					elif mg0.position == ether0.position :

						mg0.objet_ramasse.append( ether0.nom_objet )

						ether0.ramassage()



				#  Déplacement de McGyver et du gardien

				print( mg0.position[0] )





				fenetre.blit(fond, (0,0))

				for i1  in pygame_wall:
						
						fenetre.blit( i1 , ( plateau0.mur[ pygame_wall.index( i1 )][0] * 40 , plateau0.mur[ pygame_wall.index( i1 )][1] * 40 ) )

				fenetre.blit( py_aiguille0 , ( ( aiguille0.position[0] * 40 ) + 7.5 , ( aiguille0.position[1] * 40 ) + 7.5 ) )	
				fenetre.blit( anneau_objets , ( aiguille0.position[0] * 40 , aiguille0.position[1] * 40 ) )	

				fenetre.blit( py_tube_plastique0 , ( ( tube_plastiqe0.position[0] * 40 ) + 7.5 , ( tube_plastiqe0.position[1] * 40 ) + 7.5 ) )
				fenetre.blit( anneau_objets , ( tube_plastiqe0.position[0] * 40 , tube_plastiqe0.position[1] * 40 ) )

				fenetre.blit( py_ether0 , ( ( ether0.position[0] * 40 ) + 7.5 , ( ether0.position[1] * 40 ) + 7.5 ) )	
				fenetre.blit( anneau_objets , ( ether0.position[0] * 40 , ether0.position[1] * 40 ) )




				fenetre.blit( py_mcgyver , ( mg0.position[0] * 40 , mg0.position[1] * 40 ) )



				if mg0.position == gardien0.position :

					if len( mg0.objet_ramasse ) == 3 :

						image_fin = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/gagne.png").convert()

					else:

						image_fin = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/perdu.png").convert()

					fenetre.blit( image_fin , ( 100 , 200 ) )

				else:

					if len( mg0.objet_ramasse ) == 3 :

						anneau_sortie = pygame.image.load("/home/crispin/Documents/OC/P3/Mcgyver/Mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()
						

					fenetre.blit( py_gardien , ( ( gardien0.position[0] * 40 ) + 7.5 , ( gardien0.position[1] * 40 ) + 7.5 ) )

					fenetre.blit( anneau_sortie , ( gardien0.position[0] * 40 , gardien0.position[1] * 40 ) )





				pygame.display.flip()


				if mg0.position == gardien0.position :

					time.sleep( 5 )




					











def main():



	"""structure = generate_structure()

	mg = structure[1]
	plateau = structure[0]
	sortie = structure[2]
	aiguille = structure[3][0]
	tube_plastiqe = structure[3][0]
	ether = structure[3][0]


	with open("structure.json", "r") as read_file:

		data = json.load(read_file)


	print( len(data) )

	

	



	champs_libres = plateau0.mur_to_champs_libres( plateau0.mur , sortie0.position )

	champs_libres0 = list( champs_libres )

	movables = [ mg0.position ]


	#print( ' les movables avant ' , movables )

	#print( ' champs libre avant ' , champs_libres0 )


	
	i0 = 0 ;

	while i0 < len( movables ) :

		for i1 in plateau0.move_posible( movables[ i0 ] , champs_libres0 ) :

			movables.append( i1 )

			#del champs_libres0[ champs_libres0.index( i1 ) ]
			champs_libres0.remove( i1 )

		i0 += 1

	champs_accessibles = list( movables )

	random.shuffle( champs_accessibles )


			

	#print( ' champs libre apres ' , champs_libres0 )

	#print( ' les movables apres ' , movables )

	"""


	#jeu_console()


	input_demarrage = input( " Bienvenu dans McGyver Labyrinthe game \n Entre 'c' pour jouer en mode console\n Entrez 'p' pour jouer en mode pygame ( recommandé ) \n Entrez 'q' pour quitter\n" )

	while ( input_demarrage not in [ 'c' , 'p' , 'q' ] ):
		
		input_demarrage = input( " Bienvenu dans McGyver Labyrinthe game \n Entre 'c' pour jouer en mode console\n Entrez 'p' pour jouer en mode pygame ( recommandé ) \n Entrez 'q' pour quitter\n " )

	if input_demarrage == 'c' :

		jeu_console()
	
	elif input_demarrage == 'p' :

		jeu_pygame()

	elif input_demarrage == 'q' :

		pass


	
	


	





	






		 

		


main()


