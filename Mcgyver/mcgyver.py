




import random

import json








class DrawConsole:

	"""docstring for DrawConsole"""

	def __init__(self, hero , liste_objets , sortie , mur):

		self.liste_positions_objets = []

		for i0 in liste_objets :
			
			self.liste_positions_objets.append( i0.position )


		screen = ''

		for i0 in range( 15 + 2 ):
			
			for i1 in range( 15 + 2 ):
				

				if hero == ( i1 , i0 ) :
					
					screen += ' M '

				elif ( i1 , i0 ) in self.liste_positions_objets :

					#screen += ' O 


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
		





class Plateau:

	"""docstring for Plateau"""

	def __init__( self , taille_plateau ):

		self.plateauvide = []
		
		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				self.plateauvide.append( ( i1 , i0 ) )

		with open("structure.json", "r") as read_file:

			data = json.load(read_file)

		self.mur = []

		for i0 in data[ 0 ]:
		 	
		 	self.mur.append( tuple( i0 ) )




	def initialisemur( self , taille_plateau , route1 , route2 , route3 , route4 ):

		self.mur = []

		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				if ( ( i1 , i0 ) in route1 ) or ( ( i1 , i0 ) in route2 ) or ( ( i1 , i0 ) in route3 ) or ( ( i1 , i0 ) in route4 ) :

					pass

				else :

					if random.randrange( 2 ) == 0 :

						self.mur.append( ( i1 , i0 ) )

					else :

						pass


	def move_posible( self , point , champs_libres ):

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


	def mur_to_champs_libres( self , mur , position_sortie ):

		champs_libres = []

		for i0 in range( 15 ):
			
			for i1 in range( 15 ):
				
				if ( ( i1 , i0 ) not in mur ) and ( i1 , i0 ) != position_sortie  :

					champs_libres.append( ( i1 , i0 ) )

		return( champs_libres )


	def movables_in_champs_libres( self , i , movables  , champs_libres ):


		return( len( self.move_posible( movables[ i ] , champs_libres ) ) )



class Sortie:

	"""docstring for Sortie"""

	def __init__( self , taille_plateau ):

		#self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.route_mg = []

		with open("structure.json", "r") as read_file:

			data = json.load(read_file)

		self.position = tuple( data[ 2 ] )
		


class Heros:

	"""docstring for Heros"""

	def __init__( self , taille_plateau ):

		#self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		with open("structure.json", "r") as read_file:

			data = json.load(read_file)

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

			print( 'Sélectionner une direction valide !!' )

		return( self.new_pos )



class Gardien:

	"""docstring for Gardien"""
	
	def __init__( self ):

		#self.position = ( 0 , 0)

		with open("structure.json", "r") as read_file:

			data = json.load(read_file)

		self.position = tuple( data[ 2 ] )




		
plateau0 = Plateau( 15 )

mg0 = Heros(15)

sortie0 = Sortie(15)

position_objets_ramasse = []





class ObjetsRamasses:

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

		random.shuffle( champs_accessibles )


				

		#print( ' champs libre apres ' , champs_libres0 )

		#print( ' les movables apres ' , movables )

		while ( champs_accessibles[0] in position_objets_ramasse ):

			random.shuffle( champs_accessibles )

		self.position = champs_accessibles[ 0 ]

		position_objets_ramasse.append( champs_accessibles[ 0 ] )


		#self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )


		self.route_mg = []

		self.nom_objet = nom_de_lobjet

		#print( self.position )

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






		 

		


main()


