from time import time, sleep
from collections import deque


class RateLimiter:
    def __init__(self, limit: int, window_sec: int):
        self.limit = limit
        self.window_sec = window_sec

        self.user_requests = {}

    def try_add_request(self, user_id, timestamp):
        if user_id not in self.user_requests:
            self.user_requests[user_id] = deque(maxlen=self.limit)

        now = time()
        request_queue = self.user_requests[user_id]
        while request_queue and (now - request_queue[0] > self.window_sec):
            request_queue.popleft()

        if len(request_queue) > self.limit:
            return False

        request_queue.append(timestamp)
        return True





if __name__ == '__main__':
    rate_limiter = RateLimiter(3, 1)
    for _ in range(5):
        assert rate_limiter.try_add_request('foo', time()) is True

    # assert rate_limiter.try_add_request('foo', time()) is False
    sleep(3)
    # assert not rate_limiter.user_requests['foo']
    assert rate_limiter.try_add_request('foo', time()) is True

