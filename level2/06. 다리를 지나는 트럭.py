from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    bridge_weight = 0

    while bridge:
        bridge_weight -= bridge[0]
        bridge.pop(0)
        if len(truck_weights) > 0 and bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        elif truck_weights:
            bridge.append(0)
        time += 1
    return time


