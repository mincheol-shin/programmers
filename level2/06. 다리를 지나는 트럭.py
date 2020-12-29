from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    truck_on_bridge = deque()
    current_weight = 0
    time = 1
    passing_truck = 0
    while passing_truck != len(truck_weights):
        if len(trucks) and current_weight + trucks[0] <= weight:
            current_weight += trucks[0]
            truck_on_bridge.append({trucks.popleft(): 0})

        for i in range(0, len(truck_on_bridge)):
            key = list(truck_on_bridge[i].keys())[0]
            if truck_on_bridge[i][key] == -1:
                continue

            else:
                truck_on_bridge[i][key] += 1

                if truck_on_bridge[i][key] == bridge_length:
                    truck_on_bridge[i][key] = -1
                    current_weight -= key
                    passing_truck += 1

        time += 1

    return time
