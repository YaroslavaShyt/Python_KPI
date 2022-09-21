import argparse


def count_max(cap,  weight):
    weight = [0] + weight
    items = len(weight)
    cap += 1
    matrx_weights = [[0 for _ in range(items)] for _ in range(cap)]
    for i in range(1, items):
        for j in range(1, cap):
            matrx_weights[j][i] = matrx_weights[j][i - 1]
            if weight[i] <= j:
                val = matrx_weights[j - weight[i]][i - 1] + weight[i]
                if matrx_weights[j][i] < val:
                    matrx_weights[j][i] = val
    return matrx_weights[-1][-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', dest='capacity', type=int)
    parser.add_argument('-w', dest='weights', nargs='+', type=int)
    parser.add_argument('-n', dest='bars_number', type=int)
    args = parser.parse_args()
    if len(args.weights) != args.bars_number:
        print('Error: number of bars in list is different.')
    elif args.bars_number != len(set(args.weights)):
        print('Error: all the bars must be unique.')
    elif any(weight <= 0 for weight in args.weights):
        print('Error: all the bar weights must be positive and not zero')
    else:
        print(count_max(args.capacity, args.weights))


main()
