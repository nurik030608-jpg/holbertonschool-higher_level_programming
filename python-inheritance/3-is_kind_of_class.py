#!/usr/bin/python3
"""
Bu modul obyektlərin sinif mənsubiyyətini yoxlayan
funksiyanı ehtiva edir.
"""


def is_kind_of_class(obj, a_class):
    """
    Obyektin göstərilən sinfin özü və ya ondan törəyən 
    siniflərin nümayəndəsi olub-olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        True əgər obyekt həmin sinifdən və ya törəməsindəndirsə, 
        əks halda False.
    """
    return isinstance(obj, a_class)
