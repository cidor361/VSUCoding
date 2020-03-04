class Neuron:
    inputs_list = [1, 1, 0, 1, 1, 0, 1]
    weight_list = [0, 0, 0, 0, 0, 0, 0]
    desired_result = 1
    learning_rate = 0.1
    trials = 6

    def evaluate_neural_network():
        result = 0
        for i in range(len(Neuron.inputs_list)):
            layer_value = Neuron.inputs_list[i] * Neuron.weight_list[i]
            result += layer_value
        print("Оценка нейросети: " + str(result))
        print("Веса: " + str(Neuron.weight_list))
        return result

    def evaluate_error():
        error = Neuron.desired_result - Neuron.actual
        print("Оценка ошибки: " + str(error))
        return error

    def learn():
        print("обучение...")
        for i in range(len(Neuron.inputs_list)):
            if Neuron.inputs_list[i] > 0:
                Neuron.weight_list[i] += Neuron.learning_rate

    def train():
        for i in range(Neuron.trials):
            neural_net_result = Neuron.evaluate_neural_network()
            Neuron.learn()


Neuron.train()
