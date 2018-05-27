import random
import time
import sys


def myChoice(selectList, x, node):
    result = []
    buf = 1
    for i in range(node, node+x):
        index = node + i
        index = index % len(selectList)
        result.append(selectList[index-buf])
        buf += 2
    return result


def sendPacket(nodes, x):
    queue_nodes = [0]
    count = 0
    for node in queue_nodes:
        count += 1
        selectList = nodes*1
        if node in selectList:
            selectList.remove(node)
        for new_node in random.sample(selectList, x):
            if new_node not in queue_nodes:
                queue_nodes.append(new_node)
        if len(queue_nodes) == len(nodes):
            return 1, count
    return 0, count


def sendPacketQueue(nodes, x):
    queue_packets = [[0]]
    scope_visited_nodes = [0]
    count = 0
    for packet in queue_packets:
        count += 1
        selectList = nodes*1
        for visited_node in packet:
            if visited_node in selectList:
                selectList.remove(visited_node)
        for new_node in random.sample(selectList, x):
            if new_node not in scope_visited_nodes:
                new_packet = [new_node]
                new_packet.extend(packet)
                queue_packets.append(new_packet)
                scope_visited_nodes.append(new_node)
        if len(scope_visited_nodes) == len(nodes):
            return 1, count
    return 0, count


def sendPacketChoice(nodes, x):
    queue_nodes = [0]
    count = 0
    for node in queue_nodes:
        count += 1
        selectList = nodes*1
        if node in selectList:
            selectList.remove(node)
        for new_node in myChoice(selectList, x, node):
            if new_node not in queue_nodes:
                queue_nodes.append(new_node)
        if len(queue_nodes) == len(nodes):
            return 1, count
    return 0, count


def run_epidemic(x, n, i, *argv):
    start = time.time()
    count_success = 0
    count_iteration = 0
    nodes = list(i for i in range(n))
    if 'with_queue' in argv:
        algo = sendPacketQueue
    elif 'with_choice' in argv:
        algo = sendPacketChoice
    else:
        algo = sendPacket
    for packet in range(i):
        result = algo(nodes, x)
        count_success += result[0]
        count_iteration += result[1]
    recived = format(count_success/i*100, ".2f")
    print('In {}% cases all nodes received the packet'.format(recived))
    print('total: {} iterations'.format(count_iteration))
    print('time: {}'.format(time.time() - start))

if __name__ == "__main__":
    if 3 <= len(sys.argv) <= 4:
        run_epidemic(4, int(sys.argv[1]), int(sys.argv[2]), str(sys.argv[-1]))
    else:
        run_epidemic(4, 20, 1000)
