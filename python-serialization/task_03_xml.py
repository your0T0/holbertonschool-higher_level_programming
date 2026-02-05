#!/usr/bin/python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def _convert_type(value):
    """Try to convert string value to int/float/bool, else keep string"""
    if value is None:
        return ""

    v = value.strip()

    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False

    try:
        return int(v)
    except Exception:
        pass

    try:
        return float(v)
    except Exception:
        pass

    return v


def deserialize_from_xml(filename):
    """Deserialize XML file to a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = _convert_type(child.text)

    return result
