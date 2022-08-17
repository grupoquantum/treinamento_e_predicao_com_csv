<div align="justify">
<p align="justify">
Todo algoritmo de inteligência Artificial trabalha com duas fases principais que são treinamento e predição, em alguns casos poderá haver ainda uma terceira fase intermediária que acontece entre essas duas que é o teste. No Neuraline você tem o método “fit” para treinar na fase de treinamento e o método “predict” para predizer na fase de predição/execução. Também é possível testar o seu resultado antes da predição com o método “test”.
</p>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors() # algoritmo K-Nearest Neighbors que faz a predição com base na distância euclidiana

inputs = [[1, 2], [10, 20], [100, 200], [3, 4], [30, 40], [300, 400]]
outputs = [['unidades'], ['dezenas'], ['centenas'], ['unidades'], ['dezenas'], ['centenas']]
k_nearest_neighbors.fit( # fase de treinamento
	inputs=inputs, # entradas de exemplo para a aprendizagem
	outputs=outputs, # saídas de exemplo para a aprendizagem
)
inputs_test = [[2, 3], [20, 30], [200, 300]] # entradas diferentes para testar a aprendizagem
outputs_test = [['unidades'], ['dezenas'], ['centenas']] # saídas esperadas para o resultado desejado
result_test = k_nearest_neighbors.test(inputs=inputs_test, outputs=outputs_test) # fase de teste
print(result_test) # printa o resultado estatístico com valores entre 0 (0%) e 1 (100%).
k_nearest_neighbors.saveModel('modelo_de_machine_learning') # salva o modelo de ml 
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
{'assertiveness': 1, 'error': 0}
  </code>
</pre>
<br>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors() # algoritmo K-Nearest Neighbors que faz a predição com base na distância euclidiana

k_nearest_neighbors.loadModel('modelo_de_machine_learning') # carrega o modelo de ml
inputs_predict = [[4, 5], [40, 50], [400, 500]] # entradas para resultados desconhecidos
outputs_predict = k_nearest_neighbors.predict(inputs=inputs_predict) # fase de predição/execução, retorna os resultados previstos
print(outputs_predict) # printa os resultados possíveis encontrados com base na aprendizagem da fase de treinamento que foi salva no modelo
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
[['unidades'], ['dezenas'], ['centenas']]
  </code>
</pre>
<br>
<p align="justify">
Existe ainda uma outra alternativa para agilizar o desenvolvimento que é o método “fitPredict” que treina e executa ao mesma tempo para que você possa conferir o resultado do seu treinamento enquanto treina.
</p>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors() # algoritmo K-Nearest Neighbors que faz a predição com base na distância euclidiana

inputs_fit = [[1, 2], [10, 20], [100, 200], [3, 4], [30, 40], [300, 400]] # entradas de exemplo para o algoritmo aprender
outputs_fit = [['unidades'], ['dezenas'], ['centenas'], ['unidades'], ['dezenas'], ['centenas']] # saídas de exemplo para o algoritmo aprender
inputs_predict = [[2, 3], [20, 30], [200, 300]] # entradas da predição para o algoritmo prever
outputs_predict = k_nearest_neighbors.fitPredict( # fase de treinamento e execução juntas
	inputs=inputs_fit, # atribuição das entradas de exemplo para a aprendizagem
	outputs=outputs_fit, # atribuição das saídas de exemplo para a aprendizagem
	inputs_predict=inputs_predict # atribuição das entradas que deverão ser previstas
)
print(outputs_predict) # printa o resultado previsto com base nas entradas e saídas de exemplo
k_nearest_neighbors.saveModel('modelo_salvo_com_treinamento_e_predicao')
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
[['unidades'], ['dezenas'], ['centenas']]
  </code>
</pre>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors()

k_nearest_neighbors.loadModel('modelo_salvo_com_treinamento_e_predicao')
inputs_predict = [[4, 5], [40, 50], [400, 500]] # entradas para resultados desconhecidos
outputs_predict = k_nearest_neighbors.predict(inputs=inputs_predict) # fase de predição, retorna os resultados previstos
print(outputs_predict) # printa os resultados possíveis encontrados com base na aprendizagem da fase de treinamento e predição que foi salva no modelo
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
[['unidades'], ['dezenas'], ['centenas']]
  </code>
</pre>
<br>
<p align="justify">
Os algoritmos de Inteligência Artificial para Ciência de Dados usam como padrão arquivos no formato CSV (Comma-Separated Values/Valores Separados por Virgula) que são arquivos texto estruturadas como uma tabela que contém linhas e colunas, as células das colunas costumam ser separadas pelo caractere de vírgula ou qualquer outro caractere separador onde na maioria dos casos as células da primeira linha correspondem aos títulos das colunas. Bem semelhante ao que acontece em uma tabela do Excel. Veja a seguir como visualizar um arquivo CSV:
</p>
<br>
<pre>
  <code>
from Neuraline.Utilities.data import DataTable # importação da classe DataTable no algoritmo data contido no módulo Utilities da biblioteca Neuraline
data_table = DataTable() # instanciação da classe dentro da variável data_table que será usada como objeto para acessar os métodos da classe

data_table.visualization_csv_inline( # método para visualização de arquivos de tabelas no formato CSV
	url_path='arquivo_de_treinamento.csv', # endereço do arquivo
	title=True, # especifica que o arquivo possui uma primeira linha de títulos
	titles=['INPUT_1', 'INPUT_2', 'OUTPUT_1'], # títulos das colunas que você deseja visualizar, você poderá visualizar colunas específicas ou todas elas se não definir esse parâmetro
	separator=',', # caractere separador de células do arquivo, geralmente "," ou ";" mas pode ser qualquer um
	limit=6 # limite de linhas na visualização, se o parâmetro não for definido todas as linhas serão exibidas, cuidado pois alguns arquivos possuem bilhões de linhas que poderão travar a sua máquina na visualização se você não definir um limite
)
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
╒═══════════╤═══════════╤════════════╕
│   INPUT_1 │   INPUT_2 │ OUTPUT_1   │
╞═══════════╪═══════════╪════════════╡
│       300 │       400 │ centenas   │
├───────────┼───────────┼────────────┤
│        30 │        40 │ dezenas    │
├───────────┼───────────┼────────────┤
│         3 │         4 │ unidades   │
├───────────┼───────────┼────────────┤
│       100 │       200 │ centenas   │
├───────────┼───────────┼────────────┤
│        10 │        20 │ dezenas    │
├───────────┼───────────┼────────────┤
│         1 │         2 │ unidades   │
╘═══════════╧═══════════╧════════════╛
  </code>
</pre>
<br>
<pre>
  <code>
from Neuraline.Utilities.data import DataTable # importação da classe DataTable no algoritmo data contido no módulo Utilities da biblioteca Neuraline
data_table = DataTable() # instanciação da classe dentro da variável data_table que será usada como objeto para acessar os métodos da classe

data_table.visualization_csv( # para visualizar de forma gráfica com a possibilidade de ordenação das colunas clicando nos títulos use o método "visualization_csv"
	url_path='arquivo_de_treinamento.csv', # endereço do arquivo
	title=True, # especifica que o arquivo possui uma primeira linha de títulos
	titles=['INPUT_1', 'INPUT_2', 'OUTPUT_1'], # títulos das colunas que você deseja visualizar, você poderá visualizar colunas específicas ou todas elas se não definir esse parâmetro
	separator=',', # caractere separador de células do arquivo, geralmente "," ou ";" mas pode ser qualquer um
	limit=6 # limite de linhas na visualização, se o parâmetro não for definido todas as linhas serão exibidas, cuidado pois alguns arquivos possuem bilhões de linhas que poderão travar a sua máquina na visualização se você não definir um limite
) # se a tabela não for carregada de primeira pode ser por lentidão da sua placa gráfica, neste caso basta fechar a janela e executar o código novamente
  </code>
</pre>
<br>
Resultado:
<p align="center"><img src="https://github.com/grupoquantum/treinamento_e_predicao_com_csv/blob/main/arquivo_de_treinamento_csv.png"></p>
<br>
<p align="justify">
Com o Neuraline você pode treinar o seu algoritmo usando dados de um arquivo CSV de forma muito simples através do método “fitCSV”. Com este método você poderá referenciar as colunas que serão os dados de entrada e as colunas que serão os dados de saída de maneira rápida e prática, veja um exemplo disso no código abaixo:
</p>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors()
''' os algoritmos de IA que correspondem a mesma classe de aprendizado possuem os mesmos métodos correspondentes '''
k_nearest_neighbors.fitCSV( # fase de treinamento com o arquivo CSV, estamos usando o K-Nearest Neighbors de exemplo mas o mesmo vale para os demais algoritmos de IA com aprendizado supervisionado
	url_path='arquivo_de_treinamento.csv', # endereço do arquivo CSV
	title=True, # a primeira linha é de títulos e por tanto deve ser ignorada
	separator=',', # caractere separador de célunas do arquivo
	list_inputs=['INPUT_1', 'INPUT_2'], # lista com os títulos das colunas que corresponderão as entradas
	list_outputs=['OUTPUT_1'] # lista com os títulos das colunas que corresponderão as saídas
)
inputs_test = [[2, 3], [20, 30], [200, 300]] # entradas diferentes para testar a aprendizagem
outputs_test = [['unidades'], ['dezenas'], ['centenas']] # saídas esperadas para o resultado desejado
result_test = k_nearest_neighbors.test(inputs=inputs_test, outputs=outputs_test) # fase de teste
print(result_test) # printa o resultado estatístico com valores entre 0 (0%) e 1 (100%).
k_nearest_neighbors.saveModel('modelo_salvo_com_treinamento_por_csv') # salva o modelo de ml
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
{'assertiveness': 1, 'error': 0}
  </code>
</pre>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors()
''' lembre-se que para algoritmos de supervised learning os mesmos métodos poderão ser utilizados, os algoritmos com outros tipos de apredizagem também possuem métodos correspondentes entre eles '''
k_nearest_neighbors.loadModel('modelo_salvo_com_treinamento_por_csv')
inputs_predict = [[4, 5], [40, 50], [400, 500]] # entradas para resultados desconhecidos
outputs_predict = k_nearest_neighbors.predict(inputs=inputs_predict) # fase de execução, retorna os resultados previstos
print(outputs_predict) # printa os resultados possíveis encontrados com base na aprendizagem do arquivo CSV que foi salva no modelo
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
[['unidades'], ['dezenas'], ['centenas']]
  </code>
</pre>
<br>
<p align="justify">
O mesmo pode ser feito com outros algoritmos que possuam valores de entrada e saída no treinamento, confira abaixo um exemplo do mesmo método com uma rede neural artificial:
</p>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.DeepLearning.neural_network import NeuralNetwork # importação da rede neural artificial
from Neuraline.Utilities.data import DataTable # importação do recurso para manipulação de tabelas
neural_network = NeuralNetwork() # instanciação da rede neural artificial

DataTable().visualization_csv_inline(url_path='arquivo_de_treinamento_para_a_rede_neural.csv') # exibe o conteúdo do arquivo CSV chamando o método diretamente da classe instanciada
neural_network.fitCSV( # fase de treinamento com o arquivo CSV
	url_path='arquivo_de_treinamento_para_a_rede_neural.csv', # endereço do arquivo CSV
	title=True, # a primeira linha é de títulos e por tanto deve ser ignorada
	separator=',', # caractere separador de célunas do arquivo
	list_inputs=['INPUT_1', 'INPUT_2'], # lista com os títulos das colunas que corresponderão as entradas
	list_outputs=['OUTPUT_1'], # lista com os títulos das colunas que corresponderão as saídas, -1 para unidades, 0 para dezenas e 1 para centenas
	epochs=5, # número de repetições para fixar o conhecimento
	activation_function='nonlinear', # função genérica sem formatação de resultado
	show_error=True # exibição da diminuição da taxa de perda
)
entries = [[2, 3], [20, 30], [200, 300]] # entradas para teste de predição
result = neural_network.predict(inputs=entries) # predição
from math import trunc # importação da função trunc da classe math para desconsiderar a parte decimal no resultado
outputs = [[trunc(output[0])] for output in result] # percorre a lista de respostas truncando os elementos das listas de saída
print(outputs) # exibe os resultados formatados entre -1, 0 e 1
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
╒═══════════╤═══════════╤════════════╕
│   INPUT_1 │   INPUT_2 │   OUTPUT_1 │
╞═══════════╪═══════════╪════════════╡
│       300 │       400 │          1 │
├───────────┼───────────┼────────────┤
│        30 │        30 │          0 │
├───────────┼───────────┼────────────┤
│         3 │         4 │         -1 │
├───────────┼───────────┼────────────┤
│       100 │       200 │          1 │
├───────────┼───────────┼────────────┤
│        10 │        20 │          0 │
├───────────┼───────────┼────────────┤
│         1 │         2 │         -1 │
╘═══════════╧═══════════╧════════════╛
epoch...............................: 1 - loss: 0.80000000
epoch...............................: 2 - loss: 0.60000000
epoch...............................: 3 - loss: 0.40000000
epoch...............................: 4 - loss: 0.20000000
epoch...............................: 5 - loss: 0.00000000
[[-1], [0], [1]]
  </code>
</pre>
<br>
<p align="justify">
Também é possível salvar a sua predição diretamente em um arquivo CSV. Treinar e executar o seu algoritmo diretamente com uma base de dados no formato CSV facilita muito o trabalho de quem precisa realizar análises de dados em bases extensas com milhares ou até milhões de linhas, para Cientistas de Dados isso tornará o desenvolvimento muito mais rápido e produtivo para você se focar no que realmente importa.
</p>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
from Neuraline.Utilities.data import DataTable
k_nearest_neighbors = KNearestNeighbors()
data_table = DataTable()

k_nearest_neighbors.loadModel('modelo_salvo_com_treinamento_por_csv')
inputs_predict = [[4, 5], [40, 50], [400, 500]] # entradas para resultados desconhecidos
k_nearest_neighbors.predictCSV( # com o método "predictCSV" é possível salvar os resultados da predição em uma tabela CSV para análise posterior
	inputs=inputs_predict, # entradas que deverão ser previstas
	titles=['INPUT_1', 'INPUT_2', 'OUTPUT_1'], # lista com os títulos que serão gerados na primeira linha do arquivo de predição
	separator=',', # caractere que será usado para separar as células do arquivo gerado
	url_path='arquivo_da_predicao.csv' # endereço e nome do arquivo que será gerado com os dados da predição
)

data_table.visualization_csv_inline(url_path='arquivo_da_predicao.csv') # visualiza o arquivo CSV da predição
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
╒═══════════╤═══════════╤════════════╕
│   INPUT_1 │   INPUT_2 │ OUTPUT_1   │
╞═══════════╪═══════════╪════════════╡
│       400 │       500 │ centenas   │
├───────────┼───────────┼────────────┤
│        40 │        50 │ dezenas    │
├───────────┼───────────┼────────────┤
│         4 │         5 │ unidades   │
╘═══════════╧═══════════╧════════════╛
  </code>
</pre>
<br>
<p align="justify">
Além dos métodos mencionados ainda podemos utilizar um método de nome “fitPredictCSV” que irá treinar o seu algoritmo com as linhas que possuem valores em uma ou mais colunas de saída e predizer o resultado nas células de saída que estiverem vazias.
</p>
<br>
<pre>
  <code>
from Neuraline.Utilities.data import DataTable
''' também é possível chamar os métodos direto da classe '''
DataTable().visualization_csv_inline(url_path='arquivo_para_treinamento_e_predicao.csv') # visualiza o arquivo que será usado para treinamento e predição
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
╒═══════════╤═══════════╤════════════╕
│   INPUT_1 │   INPUT_2 │ OUTPUT_1   │
╞═══════════╪═══════════╪════════════╡
│       200 │       300 │            │
├───────────┼───────────┼────────────┤
│       300 │       400 │            │
├───────────┼───────────┼────────────┤
│       100 │       200 │ centenas   │
├───────────┼───────────┼────────────┤
│        20 │        30 │            │
├───────────┼───────────┼────────────┤
│        30 │        40 │            │
├───────────┼───────────┼────────────┤
│        10 │        20 │ dezenas    │
├───────────┼───────────┼────────────┤
│         2 │         3 │            │
├───────────┼───────────┼────────────┤
│         3 │         4 │            │
├───────────┼───────────┼────────────┤
│         1 │         2 │ unidades   │
╘═══════════╧═══════════╧════════════╛
  </code>
</pre>
<br>
<pre>
  <code>
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
from Neuraline.Utilities.data import DataTable
k_nearest_neighbors = KNearestNeighbors()

k_nearest_neighbors.loadModel('modelo_salvo_com_treinamento_por_csv') # poderia ser qualquer modelo
outputs_predict = k_nearest_neighbors.fitPredictCSV( # treina e prediz no mesmo arquivo
	url_path='arquivo_para_treinamento_e_predicao.csv', # endereço e nome do arquivo CSV para treinamento e predição, o arquivo original será sobrescrito então se for importante salve um backup antes de executar
	list_inputs=['INPUT_1', 'INPUT_2'], # lista com os nomes das colunas de entrada
	list_outputs=['OUTPUT_1'], # lista com os nomes das colunas de saída
	separator=',', # caractere separador do arquivo
)

DataTable().visualization_csv_inline(url_path='arquivo_para_treinamento_e_predicao.csv') # visualiza o arquivo depois de atualizado com as predições
  </code>
</pre>
<br>
Resultado:
<pre>
  <code>
╒═══════════╤═══════════╤════════════╕
│   INPUT_1 │   INPUT_2 │ OUTPUT_1   │
╞═══════════╪═══════════╪════════════╡
│       200 │       300 │ centenas   │
├───────────┼───────────┼────────────┤
│       300 │       400 │ centenas   │
├───────────┼───────────┼────────────┤
│       100 │       200 │ centenas   │
├───────────┼───────────┼────────────┤
│        20 │        30 │ dezenas    │
├───────────┼───────────┼────────────┤
│        30 │        40 │ dezenas    │
├───────────┼───────────┼────────────┤
│        10 │        20 │ dezenas    │
├───────────┼───────────┼────────────┤
│         2 │         3 │ unidades   │
├───────────┼───────────┼────────────┤
│         3 │         4 │ unidades   │
├───────────┼───────────┼────────────┤
│         1 │         2 │ unidades   │
╘═══════════╧═══════════╧════════════╛
  </code>
</pre>
<br>
<p align="justify">
Viu só como é tudo mais fácil com o Neuraline? Sem usar o Pandas, sem ter que ler o arquivo e manipular os dados para transformá-los em listas, sem códigos gigantes e grotescos. Nada disso seria possível se você estivesse utilizando outras bibliotecas que exigem codificação extensa e complexa como o SciPy, o TensorFlow, o PyTorch e outras bibliotecas “menos profissionais”. Nos vemos na próxima!
</p>
</div>
