import json

domain_sizes = [32, 64, 128, 256, 512]
class_metric = 'accuracy'
autor_metric = 'decoder_root_mean_squared_error'

def print_keys(data):
    print('Keys: [ ', end='')
    for k in data.keys():
        print(f'{k}, ', end='')
    print(']')

if __name__ == "__main__":
    suffix = '/model-classifier.json'

    for domain in domain_sizes:
        class_values = []
        autor_values = []

        filename = f'runs-{domain}{suffix}'
        
        # Opening JSON file
        with open(filename, 'r') as f:
            data = json.load(f)
            history = data['history']
            # In every three, the first element is the trace of the training, 
            # and it is ignored. The second and third elements contain
            # the metric and loss for the classifier and autoencoder,
            # respectively
            for i in range(0, len(history), 3):
                class_values.append(history[i+1][class_metric])
                autor_values.append(history[i+2][autor_metric])

        print(f'Domain size: {domain}. Metric outputs are presented next.')
        print(f'Fold\tClassification\tAutoencoder')
        for j in range(len(class_values)):
            print(f'{j}\t{class_values[j]:.3f}\t\t{autor_values[j]:.3f}')

        class_value_mean = sum(class_values) / len(class_values)
        autor_value_mean = sum(autor_values) / len(autor_values)
        print(f'\nMean accuracy value: {class_value_mean:.4f}, mean rmse value: {autor_value_mean:.4f}')
        print('\n')
