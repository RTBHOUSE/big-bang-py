def cowsay(msg: str) -> str:
    """
    Generate ASCII picture of a cow saying something provided by the user.

    Refers to the true and original: https://en.wikipedia.org/wiki/Cowsay
    """
    speech_bubble_border = len(msg) * '#'
    cow_speech_bubble = (
        f'\n'
        f'##{speech_bubble_border}##\n'
        f'# {msg} #\n'
        f'##{speech_bubble_border}##\n'
    )
    cow_img = '\n'.join((
        r'       \                     ',
        r'        \   ^__^             ',
        r'         \  (oo)\_______     ',
        r'            (__)\       )\/\ ',
        r'                ||----w |    ',
        r'                ||     ||    ',
    ))
    return cow_speech_bubble + cow_img
