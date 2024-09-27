"""
Make text upper-case.

To run:
`python to_upper.py`

CLI output example: 'hello' becomes 'HELLO'
"""


def to_upper_case():
    """This function makes text upper-case on the command-line."""
    text = input("Type or paste text: ")
    new_text = text.upper()
    print(new_text)
    return


to_upper_case()
