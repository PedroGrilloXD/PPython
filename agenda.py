### CODIGO AINDA EM PRODUÇÃO MÓ PREGUIÇA DE TERMINAR XDDDDDDDDDDDDDDD
AGENDA = {}

def mostrar_contatos():
	if AGENDA:
		for contato in AGENDA:
			buscar_contato(contato)
			print('-----------------')
	else:
		print('>>> Agenda Vazia')


def buscar_contato(contato):
	print('NOME:',contato)
	print('TELEFONE:',AGENDA[contato]['telefone'])
	print('EMAIL:',AGENDA[contato]['email'])
	print('ENDEREÇO:',AGENDA[contato]['endereco'])

def ler_detalhes_contato():
	telefone = input('Digite o nome do telefone: ')
	email = input('Digite o nome do email: ')
	endereco = input('Digite o nome do endereco: ')
	return telefone, email, endereco
	
def incluir_editar_contato(contato, telefone, email, endereco):
	
	AGENDA[contato] = {
	'telefone': telefone,
	'email': email,
	'endereco': endereco,
	}
	salvar()
	print()
	print (">>>> contato {} adicionado/editado com sucesso".format(contato))
	print()

def	excluir_contato(contato):
	try:
		AGENDA.pop(contato)
		salvar()
		print (">>>> contato {} excluido com sucesso".format(contato))
	except:
		print('Contato inexistente')

def exportar_contatos(nome_do_arquivo):
	try:
		with open(nome_do_arquivo, 'w') as arquivo:
			arquivo.write('nome,telefone,email,endereco\n')
			for contato in AGENDA:
				telefone = AGENDA[contato]['telefone']
				email = AGENDA[contato]['email']
				endereco = AGENDA[contato]['endereco']
				arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereco))
		print('>>>> Agenda exportada com sucesso')
	except:
		print('>>>> Algum erro ocorreu ao exportar os contatos')

def importar_contatos(nome_do_arquivo):
	try:
		with open(nome_do_arquivo, 'r') as arquivo:
			linhas = arquivo.readlines()
			for linha in linhas:
				detalhes = linha.strip().split(',')
				
				nome = detalhes[0]
				telefone = detalhes[1]
				email = detalhes[2]
				endereco = detalhes[3]
			
			incluir_editar_contato(nome,telefone,email,endereco)
			
	except FileNotFoundError:
		print('>>>> Arquivo não encontrado')
	except Exception as error:
		print('>>>> Algum erro inesperado ocorreu')
def salvar():
	exportar_contatos('database.csv')

def	carregar():
	try:
		with open('database', 'r') as arquivo:
			linhas = arquivo.readlines()
			for linha in linhas:
				detalhes = linha.strip().split(',')
				
				nome = detalhes[0]
				telefone = detalhes[1]
				email = detalhes[2]
				endereco = detalhes[3]
			AGENDA[nome] = {
			'telefone': telefone,
			'email': email,
			'endereco': endereco,
			}		
	except FileNotFoundError:
		print('>>>> Arquivo não encontrado')
	except Exception as error:
		print('>>>> Algum erro inesperado ocorreu')

def imprimir_menu():
	print('---------------------')
	print('1 - Mostrar todos os contatos da agenda')
	print('2 - Buscar contatos')
	print('3 - Incluir contato')
	print('4 - Editar contato')
	print('5 - Mostrar todos os contatos da agenda')
	print('6 - Exportar contatos para CSV')
	print('7 - Importar contatos CSV')
	print('0 - Fechar agenda')
	print('---------------------')

	carregar()
while True:
	imprimir_menu()

	opcao = input('Escolha uma opcao ')

	print(opcao)

	if opcao == '1':
		mostrar_contatos()
	elif opcao == '2':
		contato = input('Digite o nome do contato: ')
		buscar_contato(contato)
	elif opcao == '3':		
		contato = input('Digite o nome do contato: ')
			
		try:
			AGENDA[contato]
			print('>>>> Contato ja existente')
		except KeyError:
			telefone, email, endereco = ler_detalhes_contato()
			incluir_editar_contato(contato, telefone, email, endereco)
	elif opcao == '4':
		contato = input('Digite o nome do contato: ')
			
		try:
			AGENDA[contato]
			print('>>>> Editando contato ja existente:', contato)
			telefone, email, endereco = ler_detalhes_contato()
			incluir_editar_contato(contato, telefone, email, endereco)
			incluir_editar_contato(contato)
		except KeyError:
				print('>>>> Contato inexistente')
		
	elif opcao == '5':
		contato = input('Digite o nome do contato: ')
		excluir_contato(contato)
	
	elif opcao == '6':
		nome_do_arquivo = input ('Digite o nome do arquivo a ser exportado: ')
		exportar_contatos(nome_do_arquivo)
	elif opcao	== '7':
		nome_do_arquivo = input ('Digite o nome do arquivo a ser importado: ')
		importar_contatos(nome_do_arquivo)
	elif opcao == '0':
		print('>>>> Fechando programa')
		break
	else:
		print('>>>> Opção Invalida')

### CODIGO AINDA EM PRODUÇÃO MÓ PREGUIÇA DE TERMINAR XDDDDDDDDDDDDDDD
		
