#!/usr/bin/python3

""" Interview preparation - determines if all boxes 
in a group can be unlocked"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): a list of lists, where each inner list contains
            the keys that unlock other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unopened_boxes = set(range(1, len(boxes)))

    opened_boxes = set([0])


    while unopened_boxes:
        found_new_key = False

        for key in boxes[opened_boxes.pop()]:
            if key in unopened_boxes:
                opened_boxes.add(key)
                unopened_boxes.remove(key)
            found_new_key = True

        if not found_new_key:
            break

    return len(unopened_boxes) == 0
