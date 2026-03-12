N = int(input())

route_count = 1
room_count = 1

while room_count < N:
    room_count += 6 * route_count
    route_count += 1

print(route_count)