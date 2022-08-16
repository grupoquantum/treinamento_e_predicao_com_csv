from Neuraline.Utilities.data import DataTable # importação da classe DataTable no algoritmo data contido no módulo Utilities da biblioteca Neuraline
data_table = DataTable() # instanciação da classe dentro da variável data_table que será usada como objeto para acessar os métodos da classe

data_table.visualization_csv( # para visualizar de forma gráfica com a possibilidade de ordenação das colunas clicando nos títulos use o método "visualization_csv"
	url_path='arquivo_de_treinamento.csv', # endereço do arquivo
	title=True, # especifica que o arquivo possui uma primeira linha de títulos
	titles=['INPUT_1', 'INPUT_2', 'OUTPUT_1'], # títulos das colunas que você deseja visualizar, você poderá visualizar colunas específicas ou todas elas se não definir esse parâmetro
	separator=',', # caractere separador de células do arquivo, geralmente "," ou ";" mas pode ser qualquer um
	limit=6 # limite de linhas na visualização, se o parâmetro não for definido todas as linhas serão exibidas, cuidado pois alguns arquivos possuem bilhões de linhas que poderão travar a sua máquina na visualização se você não definir um limite
) # se a tabela não for carregada de primeira pode ser por lentidão da sua placa gráfica, neste caso basta fechar a janela e executar o código novamente