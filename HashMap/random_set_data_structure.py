import random


class RandomSet:
    """
    A data structure supporting O(1) add, delete, and get_random_element operations.

    Uses a combination of:
    - A list to store elements (for O(1) random access)
    - A dictionary to map elements to their indices (for O(1) lookup)
    """

    def __init__(self):
        self.elements = []  # List to store elements
        self.indices = {}  # Map element -> index in list

    def add(self, val):
        if val in self.indices:
            return False

        self.indices[val] = len(self.elements)
        self.elements.append(val)
        return val

    def delete(self, val):
        if val not in self.indices:
            return False

        idx = self.indices[val]
        last_element = self.elements[-1]
        self.elements[idx] = last_element
        self.indices[last_element] = idx

        self.elements.pop()
        del self.indices[val]
        return val

    def get_random_element(self):
        if not self.elements:
            return None

        idx = random.randint(0, len(self.elements) - 1)
        return self.elements[idx]

    def __len__(self):
        return len(self.elements)

    def __contains__(self, val):
        return val in self.indices

    def __repr__(self):
        return f"RandomSet({self.elements})"


# Example usage
if __name__ == "__main__":
    rs = RandomSet()

    # Add elements
    print("Adding 1, 2, 3:")
    rs.add(1)
    rs.add(2)
    rs.add(3)
    print(rs)

    # Get random elements
    print("\nGetting 5 random elements:")
    for _ in range(5):
        print(rs.get_random_element())

    # Delete an element
    print("\nDeleting 2:")
    rs.delete(2)
    print(rs)

    # Try to add duplicate
    print("\nTrying to add 1 (duplicate):", rs.add(1))

    # Add more elements
    print("\nAdding 4, 5, 6:")
    rs.add(4)
    rs.add(5)
    rs.add(6)
    print(rs)

    # Delete and get random
    print("\nDeleting 1:")
    rs.delete(1)
    print(rs)
    print("Random element:", rs.get_random_element())