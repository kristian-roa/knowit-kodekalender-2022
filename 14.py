from math import ceil


def main():
    gifts = 10**6
    trip = 10**5

    shift_distance = 10**3
    shifts = trip // shift_distance
    gifts_per_shift = gifts // shifts

    weight = {'gift': 0.1, 'deer': 100, 'santa': 100, 'sled': 900}
    capacity = 200

    w_gift_shift = int(gifts_per_shift * weight['gift'])
    w = weight['santa'] + weight['sled']
    deers = 0
    for _ in range(shifts):
        w += w_gift_shift
        shift_weight = w + weight['deer'] * deers
        new_deers = ceil(shift_weight / capacity)
        deers += new_deers
        print(deers)

    print(round(deers))


if __name__ == '__main__':
    main()
