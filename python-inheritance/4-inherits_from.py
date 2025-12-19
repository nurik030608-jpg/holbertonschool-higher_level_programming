#!/usr/bin/python3
"""
Bu modul obyektin varislik zəncirini yoxlayan 
funksiyanı ehtiva edir.
"""


def inherits_from(obj, a_class):
    """
    Obyektin göstərilən sinifdən törəyən bir sinfin nümayəndəsi 
    olub-olmadığını yoxlayır (birbaşa həmin sinif deyilsə).

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        True əgər obyekt a_class-dan törəyibsə, əks halda False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
