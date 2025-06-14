def countGroups(related):
    n = len(related)
    visited = [False] * n

    def dfs(person):
        visited[person] = True
        for other in range(n):
            if related[person][other] == '1' and not visited[other]:
                dfs(other)

    groups = 0
    for person in range(n):
        if not visited[person]:
            dfs(person)
            groups += 1

    return groups


# Example usage:
if __name__ == "__main__":
    related = [
        "110",
        "110",
        "001"
    ]
    result = countGroups(related)
    print(result)  # Output should be 2
