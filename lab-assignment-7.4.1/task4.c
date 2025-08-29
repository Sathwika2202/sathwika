# Corrected version of the code
def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(len(values)):
            if i != j:
                denominator = values[j] - values[i]
                if denominator != 0:
                    ratio = values[i] / denominator
                    results.append((i, j, ratio))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
