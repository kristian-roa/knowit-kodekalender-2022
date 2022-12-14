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

    def get_deers(shift, w, deers_in_sled, active_deers):
        if shift == 99:
            return deers_in_sled + active_deers

        # print(f'{shift = } {deers_in_sled = } {active_deers = } {w = }')

        w_shift = w + w_gift_shift + weight['deer'] * deers_in_sled
        deers_in_sled += active_deers
        active_deers = ceil(w_shift / capacity)
        # print(f'{active_deers = }')

        return get_deers(shift + 1, w_shift, deers_in_sled, active_deers)

    deers = get_deers(0, weight['santa'] + weight['sled'], 0, 0)

    print(deers)


if __name__ == '__main__':
    main()
