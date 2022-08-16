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