import sys
input = sys.stdin.readline

# 첫째 줄에는 컴퓨터의 수가 주어진다.
num_computer = int(input())

# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다
num_connections = int(input())

connections = []
for _ in range(num_connections):
    connections.append(list(map(int, input().split())))

# We're looking for number of unique computers connected to computer 1 via Network
unique_computers = set()

# BFS
not_checked = [1]
while not_checked:
    checking = not_checked.pop()
    #print(f'Infecting computers connected to # {checking}')

    # Check for connected computer
    for connection in connections[:]:
        # if there are connected computer
        if checking in connection:
            # add the connected computer only to set and not_checked
            for computer in connection:
                if computer != checking:
                    unique_computers.add(computer)
                    not_checked.append(computer)
            # Remove the connection as it is already been processed
            connections.remove(connection)
            #print(f'Removed {connection}')

    #print(unique_computers)
    #print(connections)


print(len(unique_computers))