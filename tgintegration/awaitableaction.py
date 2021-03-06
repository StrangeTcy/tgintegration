from typing import Callable, Dict, Iterable, Optional, Any, Awaitable

from pyrogram.client.filters.filter import Filter


class AwaitableAction:
    """
    Represents an action to be sent by the service while waiting for a response from the peer.
    """

    def __init__(
        self,
        func: Callable[[Any], Awaitable],
        args: Iterable = None,
        kwargs: Dict = None,
        filters: Filter = None,
        num_expected: int = None,
        max_wait: Optional[float] = 20,
        min_wait_consecutive: Optional[float] = None,
    ):
        self.func = func
        self.args = args or []
        self.kwargs = kwargs or {}
        self.filters = filters
        if num_expected is not None:
            if num_expected == 0:
                raise ValueError(
                    "When no response is expected (num_expected = 0), use the normal "
                    "send_* method without awaiting instead of an AwaitableAction."
                )
            elif num_expected < 0:
                raise ValueError("Negative expections make no sense.")
        self._num_expected = num_expected
        self.consecutive_wait = (
            max(0.0, min_wait_consecutive) if min_wait_consecutive else 0
        )
        self.max_wait = max_wait

    @property
    def num_expected(self):
        return self._num_expected

    @num_expected.setter
    def num_expected(self, value):
        if value is not None:
            if not isinstance(value, int) or value < 1:
                raise ValueError("`num_expected` must be an int and greater or equal 1")
            if value > 1 and not self.consecutive_wait:
                raise ValueError(
                    "If the number of expected messages greater than one, "
                    "`min_wait_consecutive` must be given."
                )
        self._num_expected = value
