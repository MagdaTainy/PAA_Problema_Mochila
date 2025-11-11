
# Problema da Mochila 0/1 - Versão Programação Dinâmica e Gulosa

def knapsack_dp(values, weights, capacity):
    """Solução ótima usando Programação Dinâmica"""
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


def knapsack_greedy(values, weights, capacity):
    """Solução aproximada usando abordagem Gulosa"""
    ratio = [(v / w, v, w) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)  # ordena pela razão valor/peso
    total_value = 0
    total_weight = 0

    for r, v, w in ratio:
        if total_weight + w <= capacity:
            total_weight += w
            total_value += v
    return total_value


# -------------------------------
# Dataset para teste
# -------------------------------

values = [60, 100, 120, 90, 30]   # valores dos itens
weights = [10, 20, 30, 25, 15]    # pesos correspondentes
capacity = 50                     # capacidade máxima da mochila

print("Itens disponíveis:")
for i in range(len(values)):
    print(f"Item {i+1}: valor={values[i]}, peso={weights[i]}")

print("\nCapacidade da mochila:", capacity)
print("Solução ótima (PD):", knapsack_dp(values, weights, capacity))
print("Solução gulosa:", knapsack_greedy(values, weights, capacity))
