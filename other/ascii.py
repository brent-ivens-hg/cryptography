"""
Other
"""

"""
SYMMETRIC ASCII CIPHERS - ASCII range: 0..255
"""


def complement_cipher(string: str) -> str:  # <=> xor bin-ascii
    r"""
    >>> complement_cipher('''According to the caption on the bronze marker placed by
    ... the Multnomah Chapter of the Daughters of the American
    ... Revolution on May 12, 1939, "College Hall (is) the oldest
    ... building in continuous use for Educational purposes west
    ... of the Rocky Mountains. Here were educated men and women
    ... who have won recognition throughout the world in all the
    ... learned professions.''')
    '¾ßßßßßßßßßõß²ß¼ßßß»ßßß¾õ­ßß²ßÎÍÓßÎÆÌÆÓßÝ¼ß·ß×Ößßõßßßßßºßßõßß­ß²Ñß·ßßßßßõßßßßßßßßßõßÑ'
    >>> complement_cipher('¾ßßßßßßßßßõß²ß¼ßßß»ßßß¾õ­ßß²ßÎÍÓßÎÆÌÆÓßÝ¼ß·ß×Ößßõßßßßßºßßõßß­ß²Ñß·ßßßßßõßßßßßßßßßõßÑ')
    'According to the caption on the bronze marker placed by\nthe Multnomah Chapter of the Daughters of the American\nRevolution on May 12, 1939, "College Hall (is) the oldest\nbuilding in continuous use for Educational purposes west\nof the Rocky Mountains. Here were educated men and women\nwho have won recognition throughout the world in all the\nlearned professions.'
    """
    return ''.join(chr(255 - ord(c)) for c in string)


def rba_cipher(string: str) -> str:  # reverse bin-ascii
    r"""
    >>> rba_cipher('''According to the caption on the bronze marker placed by
    ... the Multnomah Chapter of the Daughters of the American
    ... Revolution on May 12, 1939, "College Hall (is) the oldest
    ... building in continuous use for Educational purposes west
    ... of the Rocky Mountains. Here were educated men and women
    ... who have won recognition throughout the world in all the
    ... learned professions.''')
    '\x82ÆÆöN&\x96væ\x04.ö\x04.\x16¦\x04Æ\x86\x0e.\x96öv\x04öv\x04.\x16¦\x04FNöv^¦\x04¶\x86NÖ¦N\x04\x0e6\x86Æ¦&\x04F\x9eP.\x16¦\x04²®6.vö¶\x86\x16\x04Â\x16\x86\x0e.¦N\x04öf\x04.\x16¦\x04"\x86®æ\x16.¦NÎ\x04öf\x04.\x16¦\x04\x82¶¦N\x96Æ\x86vPJ¦nö6®.\x96öv\x04öv\x04²\x86\x9e\x04\x8cL4\x04\x8c\x9cÌ\x9c4\x04DÂö66¦æ¦\x04\x12\x8666\x04\x14\x96Î\x94\x04.\x16¦\x04ö6&¦Î.PF®\x966&\x96væ\x04\x96v\x04Æöv.\x96v®ö®Î\x04®Î¦\x04föN\x04¢&®Æ\x86.\x96öv\x866\x04\x0e®N\x0eöÎ¦Î\x04î¦Î.Pöf\x04.\x16¦\x04JöÆÖ\x9e\x04²ö®v.\x86\x96vÎt\x04\x12¦N¦\x04î¦N¦\x04¦&®Æ\x86.¦&\x04¶¦v\x04\x86v&\x04îö¶¦vPî\x16ö\x04\x16\x86n¦\x04îöv\x04N¦Æöæv\x96.\x96öv\x04.\x16Nö®æ\x16ö®.\x04.\x16¦\x04îöN6&\x04\x96v\x04\x8666\x04.\x16¦P6¦\x86Nv¦&\x04\x0eNöf¦ÎÎ\x96övÎt'
    >>> rba_cipher('ÆÆöN&væ.ö.¦Æ.övöv.¦FNöv^¦¶NÖ¦N6Æ¦&FP.¦²®6.vö¶Â.¦Nöf.¦"®æ.¦NÎöf.¦¶¦NÆvPJ¦nö6®.övöv²L4Ì4DÂö66¦æ¦66Î.¦ö6&¦Î.PF®6&vævÆöv.v®ö®Î®Î¦föN¢&®Æ.öv6®NöÎ¦Îî¦Î.Pöf.¦JöÆÖ²ö®v.vÎt¦N¦î¦N¦¦&®Æ.¦&¶¦vv&îö¶¦vPîön¦îövN¦Æöæv.öv.Nö®æö®..¦îöN6&v66.¦P6¦Nv¦&Nöf¦ÎÎövÎt')
    'According to the caption on the bronze marker placed by\nthe Multnomah Chapter of the Daughters of the American\nRevolution on May 12, 1939, "College Hall (is) the oldest\nbuilding in continuous use for Educational purposes west\nof the Rocky Mountains. Here were educated men and women\nwho have won recognition throughout the world in all the\nlearned professions.'
    """
    return ''.join(chr(int(f'{ord(c):08b}'[::-1], 2)) for c in string)


def roa_cipher(string: str) -> str:  # reverse octal-ascii
    r"""
    >>> roa_cipher('''According to the caption on the bronze marker placed by
    ... the Multnomah Chapter of the Daughters of the American
    ... Revolution on May 12, 1939, "College Hall (is) the oldest
    ... building in continuous use for Educational purposes west
    ... of the Rocky Mountains. Here were educated men and women
    ... who have won recognition throughout the world in all the
    ... learned professions.''')
    'Ȉ܈܈཈ֈई͈ൈ༈Āঈ཈ĀঈňଈĀ܈̈ƈঈ͈཈ൈĀ཈ൈĀঈňଈĀԈֈ཈ൈ׈ଈĀୈ̈ֈ݈ଈֈĀƈै̈܈ଈईĀԈψрঈňଈĀੈஈैঈൈ཈ୈ̈ňĀ؈ň̈ƈঈଈֈĀ཈ഈĀঈňଈĀࠈ̈ஈ༈ňঈଈֈވĀ཈ഈĀঈňଈĀȈୈଈֈ͈܈̈ൈр҈ଈඈ཈ैஈঈ͈཈ൈĀ཈ൈĀੈ̈ψĀ΀րीĀ΀πހπीĀԀ؈཈ैैଈ༈ଈĀḦैैĀŀ͈ވ̀ĀঈňଈĀ཈ैईଈވঈрԈஈ͈ैई͈ൈ༈Ā͈ൈĀ܈཈ൈঈ͈ൈஈ཈ஈވĀஈވଈĀഈ཈ֈĀਈईஈ܈̈ঈ͈཈ൈ̈ैĀƈஈֈƈ཈ވଈވĀྈଈވঈр཈ഈĀঈňଈĀ҈཈܈݈ψĀੈ཈ஈൈঈ͈̈ൈވീĀHଈֈଈĀྈଈֈଈĀଈईஈ܈̈ঈଈईĀୈଈൈĀ̈ൈईĀྈ཈ୈଈൈрྈň཈Āň̈ඈଈĀྈ཈ൈĀֈଈ܈཈༈ൈ͈ঈ͈཈ൈĀঈňֈ཈ஈ༈ň཈ஈঈĀঈňଈĀྈ཈ֈैईĀ͈ൈĀ̈ैैĀঈňଈрैଈ̈ֈൈଈईĀƈֈ཈ഈଈވވ͈཈ൈވീ'
    >>> roa_cipher('Ȉ܈܈཈ֈई͈ൈ༈Āঈ཈ĀঈňଈĀ܈̈ƈঈ͈཈ൈĀ཈ൈĀঈňଈĀԈֈ཈ൈ׈ଈĀୈ̈ֈ݈ଈֈĀƈै̈܈ଈईĀԈψрঈňଈĀੈஈैঈൈ཈ୈ̈ňĀ؈ň̈ƈঈଈֈĀ཈ഈĀঈňଈĀࠈ̈ஈ༈ňঈଈֈވĀ཈ഈĀঈňଈĀȈୈଈֈ͈܈̈ൈр҈ଈඈ཈ैஈঈ͈཈ൈĀ཈ൈĀੈ̈ψĀ΀րीĀ΀πހπीĀԀ؈཈ैैଈ༈ଈĀḦैैĀŀ͈ވ̀ĀঈňଈĀ཈ैईଈވঈрԈஈ͈ैई͈ൈ༈Ā͈ൈĀ܈཈ൈঈ͈ൈஈ཈ஈވĀஈވଈĀഈ཈ֈĀਈईஈ܈̈ঈ͈཈ൈ̈ैĀƈஈֈƈ཈ވଈވĀྈଈވঈр཈ഈĀঈňଈĀ҈཈܈݈ψĀੈ཈ஈൈঈ͈̈ൈވീĀHଈֈଈĀྈଈֈଈĀଈईஈ܈̈ঈଈईĀୈଈൈĀ̈ൈईĀྈ཈ୈଈൈрྈň཈Āň̈ඈଈĀྈ཈ൈĀֈଈ܈཈༈ൈ͈ঈ͈཈ൈĀঈňֈ཈ஈ༈ň཈ஈঈĀঈňଈĀྈ཈ֈैईĀ͈ൈĀ̈ैैĀঈňଈрैଈ̈ֈൈଈईĀƈֈ཈ഈଈވވ͈཈ൈވീ')
    'According to the caption on the bronze marker placed by\nthe Multnomah Chapter of the Daughters of the American\nRevolution on May 12, 1939, "College Hall (is) the oldest\nbuilding in continuous use for Educational purposes west\nof the Rocky Mountains. Here were educated men and women\nwho have won recognition throughout the world in all the\nlearned professions.'
    """
    return ''.join(chr(int(f'{ord(c):04o}'[::-1], 8)) for c in string)


def rha_cipher(string: str) -> str:  # reverse hex-ascii
    r"""
    >>> rha_cipher('''According to the caption on the bronze marker placed by
    ... the Multnomah Chapter of the Daughters of the American
    ... Revolution on May 12, 1939, "College Hall (is) the oldest
    ... building in continuous use for Educational purposes west
    ... of the Rocky Mountains. Here were educated men and women
    ... who have won recognition throughout the world in all the
    ... learned professions.''')
    '\x1466ö\'F\x96æv\x02Gö\x02G\x86V\x026\x16\x07G\x96öæ\x02öæ\x02G\x86V\x02&\'öæ§V\x02Ö\x16\'¶V\'\x02\x07Æ\x166VF\x02&\x97\xa0G\x86V\x02ÔWÆGæöÖ\x16\x86\x024\x86\x16\x07GV\'\x02öf\x02G\x86V\x02D\x16Wv\x86GV\'7\x02öf\x02G\x86V\x02\x14ÖV\'\x966\x16æ\xa0%VgöÆWG\x96öæ\x02öæ\x02Ô\x16\x97\x02\x13#Â\x02\x13\x933\x93Â\x02"4öÆÆVvV\x02\x84\x16ÆÆ\x02\x82\x967\x92\x02G\x86V\x02öÆFV7G\xa0&W\x96ÆF\x96æv\x02\x96æ\x026öæG\x96æWöW7\x02W7V\x02fö\'\x02TFW6\x16G\x96öæ\x16Æ\x02\x07W\'\x07ö7V7\x02wV7G\xa0öf\x02G\x86V\x02%ö6¶\x97\x02ÔöWæG\x16\x96æ7â\x02\x84V\'V\x02wV\'V\x02VFW6\x16GVF\x02ÖVæ\x02\x16æF\x02wöÖVæ\xa0w\x86ö\x02\x86\x16gV\x02wöæ\x02\'V6övæ\x96G\x96öæ\x02G\x86\'öWv\x86öWG\x02G\x86V\x02wö\'ÆF\x02\x96æ\x02\x16ÆÆ\x02G\x86V\xa0ÆV\x16\'æVF\x02\x07\'öfV77\x96öæ7â'
    >>> rha_cipher("66ö'FævGöGV6GöæöæGV&'öæ§VÖ'¶V'Æ6VF& GVÔWÆGæöÖ4GV'öfGVDWvGV'7öfGVÖV'6æ %VgöÆWGöæöæÔ#Â3Â\"4öÆÆVvVÆÆ7GVöÆFV7G &WÆFævæ6öæGæWöW7W7Vfö'TFW6GöæÆW'ö7V7wV7G öfGV%ö6¶ÔöWæGæ7âV'VwV'VVFW6GVFÖVææFwöÖVæ wögVwöæ'V6övæGöæG'öWvöWGGVwö'ÆFæÆÆGV ÆV'æVF'öfV77öæ7â")
    'According to the caption on the bronze marker placed by\nthe Multnomah Chapter of the Daughters of the American\nRevolution on May 12, 1939, "College Hall (is) the oldest\nbuilding in continuous use for Educational purposes west\nof the Rocky Mountains. Here were educated men and women\nwho have won recognition throughout the world in all the\nlearned professions.'
    """
    return ''.join(chr(int(f'{ord(c):02x}'[::-1], 16)) for c in string)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
