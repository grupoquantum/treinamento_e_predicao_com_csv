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