"""
Make text lower-case.

To run:
`python to_lower.py`

CLI output: 'HELLO' becomes 'hello'
"""


def to_lower_case():
    """This function makes text lower-case on the command-line."""
    text = input("Type or paste text: ")
    new_text = text.lower()
    print(new_text)
    return


to_lower_case()
