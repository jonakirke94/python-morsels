from shlex import split as split_shlex


def tags_equal(tag1, tag2):
    tag1_parsed = normalize_and_split(tag1)
    tag2_parsed = normalize_and_split(tag2)

    return build_set(tag1_parsed) == build_set(tag2_parsed)


#  for bonus we need to also store the tag to be able to determine uniqueness
def build_set(tag_iterable) -> set:
    parsed_set = set()
    for el in tag_iterable:
        normalized = el.lower()
        if '=' in normalized:
            tag, value = normalized.split("=")

            # the first inserted takes precedence
            if tag not in parsed_set:
                parsed_set.add(tag)
                parsed_set.add(normalized)

        else:
            parsed_set.add(normalized)

    return parsed_set


def normalize_and_split(tag):
    tag_cleansed = tag[1:-1]
    return split_shlex(tag_cleansed)