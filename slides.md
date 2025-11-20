---
theme: seriph
background: https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1920
title: Elevator Rides
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Elevator Rides

CSES - Dynamic Programming


---
transition: fade-out
---

# A Probléma

<div class="text-lg">

**n ember** szeretne feljutni egy épület tetejére, de csak **egy lift** van.

<v-clicks>

- Minden embernek ismerjük a **súlyát** (w₁, w₂, ..., wₙ)
- A lift **maximális teherbírása**: x
- **Cél**: Minimális liftezések száma

</v-clicks>



</div>

<div v-click class="mt-8 grid grid-cols-2 gap-4">

<div class="p-4 bg-blue-500 bg-opacity-20 rounded">

### Korlátok
- 1 ≤ n ≤ 20
- 1 ≤ x ≤ 10⁹
- 1 ≤ wᵢ ≤ x

</div>

<div class="p-4 bg-green-500 bg-opacity-20 rounded">


- Időlimit: 1 másodperc
- Memórialimit: 512 mb

</div>

</div>

[CSES link](https://cses.fi/problemset/task/1653/)

---

# Példa

<div class="grid grid-cols-2 gap-8">

<div>

### Input

```
4 10
4 8 6 1
```

<div class="text-sm mt-4 space-y-2">
<div>4 ember</div>
<div>Max. teherbírás: 10 kg</div>
<div>Tömegek: 4, 8, 6, 1 kg</div>
</div>

</div>

<div v-click>

### Output

```
2
```

<div class="mt-6 p-4 bg-purple-500 bg-opacity-20 rounded text-sm">

**Optimális megoldás:**

**1. menet**: 4 + 6 = 10 kg  
**2. menet**: 8 + 1 = 9 kg

Összesen: **2 menet**

</div>

</div>

</div>

<div v-click class="mt-8">


</div>

---

# Bitmaszk

<v-clicks>

### Kis állapottér
- n ≤ 20 → 2²⁰ = ~1 millió állapot
- Minden állapot: mely emberek jutottak már fel

### Bitmaszk reprezentáció
```python
# Példa: 4 ember, 2. és 4. feljutott
mask = 0b1010 = 10

# Ellenőrzés: i-edik ember fenn van?
if mask & (1 << i):  # True ha fenn van
```

</v-clicks>

---

# Példa futtatás

<div class="text-sm">

Bemenet: `n=4, x=10, w=[4, 8, 6, 1]`

</div>

````md magic-move {lines: true}
```python
# Kezdőállapot
rides[0b0000] = 1   # 0 menet indult
weight[0b0000] = 0  # Üres lift
```

```python
# 1 ember fent
rides[0b0001] = 1   # 0. ember: 4 kg
weight[0b0001] = 4

rides[0b0010] = 1   # 1. ember: 8 kg  
weight[0b0010] = 8

rides[0b0100] = 1   # 2. ember: 6 kg
weight[0b0100] = 6

rides[0b1000] = 1   # 3. ember: 1 kg
weight[0b1000] = 1
```

```python
# 2 ember fent - példák
rides[0b0011] = ?
  # 0. (4kg) + 1. (8kg) = 12kg > 10 → NEM FÉR
  # rides = 2, weight = 8 (utolsó)

rides[0b0101] = ?
  # 0. (4kg) + 2. (6kg) = 10kg ≤ 10 → BELEFÉR!
  # rides = 1, weight = 10

rides[0b1001] = ?
  # 0. (4kg) + 3. (1kg) = 5kg ≤ 10 → BELEFÉR!
  # rides = 1, weight = 5
```

```python
# Végállapot: mind a 4 ember fent
rides[0b1111] = 2
weight[0b1111] = 9

# Visszakövetés:
# 1. menet: 0. (4kg) + 2. (6kg) = 10kg
# 2. menet: 1. (8kg) + 3. (1kg) = 9kg
```
````

---
layout: two-cols
---



# Komplexitás

<div class="grid grid-cols-2 gap-8">

<div>

### Időigény

<v-clicks>

- **Állapotok száma**: 2ⁿ
- **Minden állapotnál**: n ember kipróbálása
- **Összesen**: O(2ⁿ · n)

**n = 20 esetén:**
```
2²⁰ · 20 = 1,048,576 · 20
         ≈ 21 millió művelet
```

</v-clicks>

</div>

<div v-click>

### Tárigény

- **Két tömb**: rides[] és weight[]
- **Méret**: 2ⁿ elem
- **Elemenkénti méret**: 
  - rides: int (8 byte)
  - weight: int (8 byte)

**n = 20 esetén:**
```
2²⁰ · 2 · 8 byte = 16 MB
```


</div>

</div>


---

# Teljes Kód

```python{*}{maxHeight:'400px'}
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
```

---
layout: center
class: text-center
---

# Köszönöm a figyelmet! 🎉

