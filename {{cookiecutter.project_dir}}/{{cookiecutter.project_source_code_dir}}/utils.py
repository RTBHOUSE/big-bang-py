def cowsay(msg: str, print_end="\n\n") -> None:
    """
    Print ASCII picture of a cow saying something provided by the user.

    Refers to the true and original: https://en.wikipedia.org/wiki/Cowsay
    """
    print(_get_cowsay_str(msg), end=print_end)


def _get_cowsay_str(msg: str) -> str:
    speech_bubble_border = len(msg) * "#"
    cow_speech_bubble = (
        f"\n"
        f"##{speech_bubble_border}##\n"
        f"# {msg} #\n"
        f"##{speech_bubble_border}##\n"
    )
    cow_img = "\n".join((
        r"       \                     ",
        r"        \   ^__^             ",
        r"         \  (oo)\_______     ",
        r"            (__)\       )\/\ ",
        r"                ||----w |    ",
        r"                ||     ||    ",
    ))
    return cow_speech_bubble + cow_img


INTERVALS = (
    ("minutes", 60),
    ("seconds", 1),
)


def humanize_seconds(seconds: float) -> str:
    """Seconds formatted for humans."""
    result = []
    seconds_rounded = int(round(seconds))

    if seconds_rounded == 0:
        return "less than or equal 0.5 seconds"

    for name, count in INTERVALS:
        value = seconds_rounded // count
        if value:
            seconds_rounded -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append(f"{value} {name}")

    return ", ".join(result)
