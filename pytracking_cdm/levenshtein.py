def weighted_levenshtein():
    """
    Compute the absolute Levenshtein distance between the two sequences.
    The Levenshtein distance is the minimum number of edit operations necessary
    for transforming one sequence into the other. The edit operations allowed are:

        * deletion:     ABC -> BC, AC, AB
        * insertion:    ABC -> ABCD, EABC, AEBC..
        * substitution: ABC -> ABE, ADC, FBC..

    https://en.wikipedia.org/wiki/Levenshtein_distance
    TODO: https://gist.github.com/kylebgorman/1081951/9b38b7743a3cb5167ab2c6608ac8eea7fc629dca
    """

    def __init__(
        self,
        qval: int = 1,
        test_func: TestFunc | None = None,
        external: bool = True,
    ) -> None:
        self.qval = qval
        self.test_func = test_func or self._ident
        self.external = external

    def _recursive(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        # TODO: more than 2 sequences support
        if not s1 or not s2:
            return len(s1) + len(s2)

        if self.test_func(s1[-1], s2[-1]):
            return self(s1[:-1], s2[:-1])

        # deletion/insertion
        d = min(
            self(s1[:-1], s2),
            self(s1, s2[:-1]),
        )
        # substitution
        s = self(s1[:-1], s2[:-1])
        return min(d, s) + 1

    def _cycled(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        """
        source:
        https://github.com/jamesturk/jellyfish/blob/master/jellyfish/_jellyfish.py#L18
        """
        rows = len(s1) + 1
        cols = len(s2) + 1
        prev = None
        cur: Any
        if numpy:
            cur = numpy.arange(cols)
        else:
            cur = range(cols)

        for r in range(1, rows):
            prev, cur = cur, [r] + [0] * (cols - 1)
            for c in range(1, cols):
                deletion = prev[c] + 1
                insertion = cur[c - 1] + 1
                dist = self.test_func(s1[r - 1], s2[c - 1])
                edit = prev[c - 1] + (not dist)
                cur[c] = min(edit, deletion, insertion)
        return cur[-1]

    def __call__(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        s1, s2 = self._get_sequences(s1, s2)

        result = self.quick_answer(s1, s2)
        if result is not None:
            assert isinstance(result, int)
            return result

        return self._cycled(s1, s2)