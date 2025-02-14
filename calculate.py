import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''Принимает на вход название фигуры fig, функцию func, которую необходимо использовать для данной фигуры и размеры фигуры size'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		'''Цикл продолжается до тех пор, пока пользователь не введет корректные данные для figs'''
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		'''Аналогично первому циклу, но для funcs'''
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		'''программа пытается получить из словаря sizes количество аргументов, необходимых для вычисления указанной функции для данной фигуры. 
		По умолчанию, если в словаре нет информации, берётся значение 1'''
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



