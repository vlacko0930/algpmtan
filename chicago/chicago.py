import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    while True:
        try:
            token = next(iterator)
            if token == '0':
                break
                
            n = int(token)
            m = int(next(iterator)) # Utcák száma
            
            # Szomszédsági mátrix
            adj = [[] for _ in range(n + 1)]
            
            for _ in range(m):
                u = int(next(iterator))
                v = int(next(iterator))
                p_int = int(next(iterator))
                
                p_decimal = p_int / 100.0
                
                adj[u].append((v, p_decimal))
                adj[v].append((u, p_decimal))
            
            # Dijkstra
            max_probs = [-1.0] * (n + 1)
            
            # Palace Hotel
            max_probs[1] = 1.0
            
            pq = [(-1.0, 1)]
            
            while pq:
                curr_p, u = heapq.heappop(pq)
                curr_p = -curr_p
                
                # Ha már van jobb út, nem foglalkozunk vele
                if curr_p < max_probs[u]:
                    continue
                
                if u == n:
                    break
                
                for v, edge_p in adj[u]:
                    new_prob = curr_p * edge_p
                    
                    if new_prob > max_probs[v]:
                        max_probs[v] = new_prob
                        heapq.heappush(pq, (-new_prob, v))
            
            result_percentage = max_probs[n] * 100.0
            print(f"{result_percentage:.6f} percent")

        except StopIteration:
            break

if __name__ == "__main__":
    solve()