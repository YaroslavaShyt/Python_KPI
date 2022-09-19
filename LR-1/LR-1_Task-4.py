import argparse


def count_weight(W,  w):
    w = [0] + w
    items = len(w)
    capacity = W + 1
    weights = [[0 for _ in range(items)] for _ in range(capacity)]
    for i in range(1, items):
        for j in range(1, capacity):
            weights[j][i] = weights[j][i - 1]
            if w[i] <= j:
                val = weights[j - w[i]][i - 1] + w[i]
                if weights[j][i] < val:
                    weights[j][i] = val
    return weights[-1][-1]


def main():
    parser = argparse.ArgumentParser(exit_on_error=False)
    parser.add_argument('-W', '--capacity', type=int, required=True)
    parser.add_argument('-w', '--weights', nargs='+', type=int, required=True)
    parser.add_argument('-n', '--bars_number', type=int, required=True)
    try:
        args = parser.parse_args()
        if len(args.weights) != args.bars_number != len(set(args.weights)):
            print('Wrong data!')
        else:
            print(count_weight(args.capacity, args.weights))
    except ValueError:
        raise ValueError('Wrong values!')
    except TypeError:
        raise TypeError('TypeError here')
    except Exception as ex:
        print('You did something wrong: ', ex)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print('Error: ', ex)





