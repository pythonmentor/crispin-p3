




import random



class Plateau:

	"""docstring for Plateau"""

	def __init__( self , taille_plateau ):

		self.plateauvide = []
		
		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				self.plateauvide.append( ( i1 , i0 ) )


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


		





class ObjetsRamasses:

	"""docstring for Objets"""

	def __init__( self , taille_plateau ):

		self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.route_mg = []

		#print( self.position )
		



	



class Gardien:

	"""docstring for Gardien"""
	
	def __init__( self ):

		self.position = ( 0 , 0)

		#print( self.position )





class Sortie:

	"""docstring for Sortie"""

	def __init__( self , taille_plateau ):

		self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.route_mg = []
		
		




class Ligne(object):

	"""docstring for Ligne"""

	pass



class Heros:

	"""docstring for Heros"""

	def __init__( self , taille_plateau ):

		self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.objet_ramasse = [] ;

		#print( self.position )






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




#def test_initialise( position , tableau ):
	







def main():

	pas = Pas();

	plateau = Plateau(15)

	position_initialisee = []

	mg = Heros(15)

	position_initialisee.append( mg.position )





	aiguille = ObjetsRamasses( 15 )

	# Test si la position de l'aiguille est déjà occupée

	while aiguille.position in position_initialisee :
		
		aiguille = ObjetsRamasses( 15 )

	# Ajout de la position de l'aiguille dans la liste des positions occupées

	position_initialisee.append( aiguille.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	aiguille.route_mg.append( lepas )

	while lepas != aiguille.position :

		lepas = pas.make_pas( lepas , aiguille.position )

		aiguille.route_mg.append( lepas )

	print( aiguille.route_mg )





	tube_plastiqe = ObjetsRamasses( 15 )

	# Test si la position du tube en plastiqe est déjà occupée

	while tube_plastiqe.position in position_initialisee :
		
		tube_plastiqe = ObjetsRamasses( 15 )

	# Ajout de la position du tube en plastiqe dans la liste des positions occupées

	position_initialisee.append( tube_plastiqe.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	tube_plastiqe.route_mg.append( lepas )

	while lepas != tube_plastiqe.position :

		lepas = pas.make_pas( lepas , tube_plastiqe.position )

		tube_plastiqe.route_mg.append( lepas )

	print( tube_plastiqe.route_mg )





	ether = ObjetsRamasses( 15 )

	# Test si la position de l'ether est déjà occupée

	while ether.position in position_initialisee :
		
		ether = ObjetsRamasses( 15 )

	# Ajout de la position de l'ether dans la liste des positions occupées

	position_initialisee.append( ether.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	ether.route_mg.append( lepas )

	while lepas != ether.position :

		lepas = pas.make_pas( lepas , ether.position )

		ether.route_mg.append( lepas )

	print( ether.route_mg )





	sortie = Sortie(15)

	# Test si la position de la sortie est déjà occupée

	while ( sortie.position in aiguille.route_mg ) or ( sortie.position in tube_plastiqe.route_mg ) or ( sortie.position in ether.route_mg ) :
		
		sortie = Sortie( 15 )

	# Ajout de la position de la sortie dans la liste des positions occupées

	position_initialisee.append( sortie.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	sortie.route_mg.append( lepas )

	while lepas != sortie.position :

		lepas = pas.make_pas( lepas , sortie.position )

		sortie.route_mg.append( lepas )

	print( 'sortie ' , sortie.route_mg )



	plateau.initialisemur( 15 , aiguille.route_mg , tube_plastiqe.route_mg , ether.route_mg , sortie.route_mg  )




	gardien = Gardien()

	gardien.position = sortie.position




	"""	
	print( 'position mg :' , mg.position )
	print( 'position de laiguille :' , aiguille.position )
	print( 'position du tube en plastiqe :' , tube_plastiqe.position )
	print( 'position de lether :' , ether.position )
	
	print( 'position sortie avant le pas :' , sortie.position )

	mg.position = pas.make_pas( mg.position , sortie.position )

	print( 'position mg apres le pas :' , mg.position )
	print( 'position sortie apres le pas :' , sortie.position )

	"""


	screen = ''

	for i0 in range( 15 ):
		
		for i1 in range( 15  ):

			if mg.position == ( i1 , i0 ) :
				
				screen += ' M '

			elif aiguille.position == ( i1 , i0 ) :
				
				screen += ' I '

			elif tube_plastiqe.position == ( i1 , i0 ) :
				
				screen += ' T '

			elif ether.position == ( i1 , i0 ) :
				
				screen += ' E '

			elif sortie.position == ( i1 , i0 ) :
				
				screen += ' S '

			elif ( i1 , i0 ) in plateau.mur :

				screen += ' X '

			elif  ( ( i1 , i0 ) in aiguille.route_mg ) or ( ( i1 , i0 ) in tube_plastiqe.route_mg ) or ( ( i1 , i0 ) in ether.route_mg ) or ( ( i1 , i0 ) in sortie.route_mg )  :

				screen += ' . '

			else :

				screen += '   '


		screen += '\n'



	print( screen )
		


main()


