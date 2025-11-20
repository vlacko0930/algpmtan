n, x = map(int, input().split())
w = list(map(int, input().split()))

size = 1 << n
rides = [21] * size  
weight = [0] * size

rides[0] = 1


for mask in range(1, size):
    i = 0
    while i < n:
        if mask >> i & 1:
            prev = mask ^ (1 << i)
            prev_rides = rides[prev]
            prev_weight = weight[prev]
            wi = w[i]
            
            if prev_weight + wi <= x:
                if prev_rides < rides[mask]:
                    rides[mask] = prev_rides
                    weight[mask] = prev_weight + wi
                elif prev_rides == rides[mask] and prev_weight + wi < weight[mask]:
                    weight[mask] = prev_weight + wi
            else:
                new_rides = prev_rides + 1
                if new_rides < rides[mask]:
                    rides[mask] = new_rides
                    weight[mask] = wi
                elif new_rides == rides[mask] and wi < weight[mask]:
                    weight[mask] = wi
        i += 1

print(rides[size - 1])
