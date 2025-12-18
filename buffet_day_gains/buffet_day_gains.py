from collections import deque


def compute_day_gains(nb_seats: int, paying_guests: list[int], guest_movements: list[int]) -> int:
    """
    Calculate total restaurant gains for the day.

    - nb_seats: Number of available seats
    - paying_guests: How much each guest is willing to pay
    - guest_movements: Sequence of arrivals and departures

    Returns: Total gains of the day
    """
    gains = 0
    paid_guests = set()
    seated_guests = set()
    queue = deque()
    waiting_guests = set()

    for guest in guest_movements:
        if guest in seated_guests:  # a guest is leaving
            if guest not in paid_guests:
                gains += paying_guests[guest]
                paid_guests.add(guest)
            seated_guests.remove(guest)
        elif guest not in waiting_guests:  # a guest is arriving
            if len(seated_guests) < nb_seats:
                seated_guests.add(guest)
            else:
                queue.append(guest)
                waiting_guests.add(guest)
        else:  # the guest is in the queue and leaving
            waiting_guests.remove(guest)

        if len(seated_guests) < nb_seats and waiting_guests:
            next_guest = queue.popleft()
            while next_guest not in waiting_guests:
                next_guest = queue.popleft()

            waiting_guests.remove(next_guest)
            seated_guests.add(next_guest)

    return gains


assert compute_day_gains(nb_seats=100, paying_guests=[45, 10, 25, 30, 15, 20], guest_movements=[3, 3, 0, 4, 0, 2, 2, 4]) == 115
assert compute_day_gains(nb_seats=3, paying_guests=[45, 10, 25, 30, 15, 20], guest_movements=[3, 3, 0, 4, 2, 5, 2, 0, 4, 5]) == 135

assert compute_day_gains(nb_seats=3, paying_guests=[45, 10, 25, 30, 15, 20], guest_movements=[3, 3, 0, 4, 2, 5, 2, 0, 3, 3, 4, 5]) == 135
assert compute_day_gains(nb_seats=3, paying_guests=[45, 10, 25, 30, 15, 20], guest_movements=[3, 3, 0, 4, 2, 5, 5, 0, 2, 3, 3, 4]) == 115
assert compute_day_gains(nb_seats=3, paying_guests=[45, 10, 25, 30, 15, 20], guest_movements=[3, 3, 0, 4, 2, 5, 5, 0, 2, 3, 0, 3, 4, 0]) == 115


