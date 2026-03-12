from collections import deque


class KProduct:
    def __init__(self, k):
        """
        Initialize KProduct with size k.

        Args:
            k (int): The size of the sliding window
        """
        if k <= 0:
            raise ValueError("k must be a positive integer")

        self.k = k
        self.window = deque(maxlen=k)  # Automatically maintains size k
        self.product = 1
        self.zero_count = 0  # Track number of zeros in the window

    def insert(self, value):
        """
        Insert a new integer value into the sliding window.

        Args:
            value (int): The integer to insert
        """
        # If window is full, we need to remove the oldest element
        if len(self.window) == self.k:
            old_value = self.window[0]  # Get the value that will be removed

            # Update zero count for the removed element
            if old_value == 0:
                self.zero_count -= 1
            else:
                # Remove the old value from product if no zeros remain
                if self.zero_count == 0:
                    self.product //= old_value

        # Add the new value
        self.window.append(value)

        # Update product and zero count for new value
        if value == 0:
            self.zero_count += 1
        else:
            if self.zero_count == 0:
                self.product *= value

    def get_product(self):
        """
        Get the product of the last k integers inserted.

        Returns:
            int: The product of integers in the current window
        """
        if self.zero_count > 0:
            return 0
        return self.product

    def get_window(self):
        """
        Get the current window contents (for debugging).

        Returns:
            list: Current window contents
        """
        return list(self.window)


# Example usage and testing
if __name__ == "__main__":
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality")
    kp = KProduct(3)

    kp.insert(2)
    print(f"After inserting 2: window={kp.get_window()}, product={kp.get_product()}")

    kp.insert(3)
    print(f"After inserting 3: window={kp.get_window()}, product={kp.get_product()}")

    kp.insert(4)
    print(f"After inserting 4: window={kp.get_window()}, product={kp.get_product()}")

    kp.insert(5)  # This should remove 2 and add 5
    print(f"After inserting 5: window={kp.get_window()}, product={kp.get_product()}")

    print()

    # Test case 2: Handling zeros
    print("Test 2: Handling zeros")
    kp2 = KProduct(3)

    kp2.insert(2)
    kp2.insert(0)
    kp2.insert(3)
    print(f"With zero: window={kp2.get_window()}, product={kp2.get_product()}")

    kp2.insert(4)  # Remove 2, should still have zero
    print(f"After removing 2: window={kp2.get_window()}, product={kp2.get_product()}")

    kp2.insert(5)  # Remove 0, should now have product
    print(f"After removing 0: window={kp2.get_window()}, product={kp2.get_product()}")

    print()

    # Test case 3: Edge case with k=1
    print("Test 3: k=1")
    kp3 = KProduct(1)

    kp3.insert(7)
    print(f"Single element: window={kp3.get_window()}, product={kp3.get_product()}")

    kp3.insert(8)
    print(f"Replace element: window={kp3.get_window()}, product={kp3.get_product()}")