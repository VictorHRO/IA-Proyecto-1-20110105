colores = input('Introduce un color:\n')
tupla_colores = ('rojo', 'azul', 'mangenta', 'verde')

if colores in tupla_colores[0]:   
	print('El color rojo está admitido')
elif colores in tupla_colores[1]:
	print('El color azul está admitido')
elif colores in tupla_colores[2]:
	print('El color mangenta está admitido')
elif colores in tupla_colores[-1]:
	print('El color verde está admitido')
else:
	print('Color no existe ')