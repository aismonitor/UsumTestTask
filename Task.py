from collections import Counter

from prompt_toolkit import prompt, HTML
from prompt_toolkit.shortcuts import (
    message_dialog,
    button_dialog,
    input_dialog,
    set_title,
)
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import Validator


set_title("Polina test task app")


test_style = Style.from_dict(
    {
        "dialog": "bg:#88ff88",
        "dialog frame.label": "bg:#ffffff #000000",
        "dialog.body": "bg:#000000 #00ff00",
        "dialog shadow": "bg:#00aa00",
    }
)


def main():
    try:
        pick_task()
    except Exception as e:
        uhoh = message_dialog(title="Error", text="Something went wrong").run()


def reverse_sentence():
    """Write fuction, which inverts word order in given sequence"""

    text_before = input_dialog(
        "Data provider",
        text="Provide some words:",
        default="test array of words to reorder",
    ).run()

    splitted = text_before.split(" ")
    ordered = splitted[::-1]
    final = " ".join(ordered)
    result = message_dialog(
        title="Yodification done, your words REordered", text=f"{final}"
    ).run()
    pick_task()


def delete_duplicates():
    """Write fuction, which counts duplucates words in given list"""

    text_before = input_dialog(
        title="List provider",
        text="Comma-delimited list: ",
        default="one, two, two, two, three, lamp, lamp, elm, vors",
    ).run()

    input_list = text_before.split(",")
    count = dict(Counter(input_list))
    result = message_dialog(title="Calculations completed:", text=f"{count}").run()
    pick_task()

    # print("Calculations complete, your new set an other stuff: %s" % count)
    # return count


def pick_task():
    picker_dialog = button_dialog(
        title="Pick a task to check",
        text="Which one?",
        buttons=[("1", "Reverse sentence"), ("2", "Delete duplicates"), ("Exit", None)],
        style=test_style,
    ).run()
    if picker_dialog == "Reverse sentence":
        reverse_sentence()
    elif picker_dialog == "Delete duplicates":
        delete_duplicates()
    elif picker_dialog is None:
        return


if __name__ == "__main__":
    main()
