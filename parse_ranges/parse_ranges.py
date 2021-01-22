def parse_ranges(ranges):
    for r in ranges.split(','):
        start, stop = r.split("-") if len(r) > 2 else (r, r)
        yield from range(int(start), int(stop) + 1)
