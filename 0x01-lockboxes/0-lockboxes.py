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

    # Create a set containing all box indices except for the first one
    locked_boxes = set(range(1, len(boxes)))
    # Create a set containing the keys for the first box
    keys = set(boxes[0])

    # Loop until there are no more keys to try
    while keys:
        # Pop a key from the set of keys
        key = keys.pop()
        # If the key opens a locked box, add the keys from the unlocked box to the set of keys
        if key in locked_boxes:
            keys.update(boxes[key])
            # Remove the opened box from the set of locked boxes
            locked_boxes.remove(key)

    # If there are no more locked boxes, return True
    return len(locked_boxes) == 0
