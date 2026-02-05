#!/usr/bin/python3
"""Serialize/deserialize a Python dict to/from XML."""

import xml.etree.ElementTree as ET


def _type_name(value):
    """Return a simple type name for XML storage."""
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    return "str"


def _cast(value_str, tname):
    """Cast string back to the stored type."""
    if tname == "bool":
        return value_str == "True"
    if tname == "int":
        return int(value_str)
    if tname == "float":
        return float(value_str)
    return value_str


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save it to filename."""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.set("type", _type_name(value))
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Read XML from filename and return a deserialized dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            tname = child.get("type", "str")
            text = child.text if child.text is not None else ""
            data[child.tag] = _cast(text, tname)

        return data
    except Exception:
        return None
