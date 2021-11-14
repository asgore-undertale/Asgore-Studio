from PyQt5.QtWidgets import QMessageBox

_ACT_VERSION_ = 1.0 # act : asgore converting table
_AFT_VERSION_ = 1.0 # aft : asgore font table
_AFF_VERSION_ = 1.0 # aff : asgore font file
_A_SEPARATOR_ = "█"
_AFF_MIN_SEPARATOR = "/"
_AFF_FILLER = "•"
_CSV_DELIMITER_ = ","
_ZTA_SEPARATOR_ = "█"
_ZTA_RANGE_ = "\{(.*?):(.*?)\}"

_ACT_DESC_ = f'\nVERSION="{_ACT_VERSION_}"\nSEPARATOR="[_SEPARATOR_]"\n#####################\nالحرف[_SEPARATOR_]أول[_SEPARATOR_]وسط[_SEPARATOR_]آخر[_SEPARATOR_]منفصل\n'
_AFT_DESC_ = f'\nVERSION="{_AFT_VERSION_}"\nSEPARATOR="[_SEPARATOR_]"\n#####################\nChar[_SEPARATOR_]X[_SEPARATOR_]Y[_SEPARATOR_]Width[_SEPARATOR_]Height[_SEPARATOR_]Xoffset[_SEPARATOR_]Yoffset[_SEPARATOR_]Xadvance\n'
_AFF_DESC_ = f'\nVERSION="{_AFF_VERSION_}"\nSEPARATOR="[_SEPARATOR_]"\n#####################\nChar[_SEPARATOR_]X[_SEPARATOR_]Y[_SEPARATOR_]Width[_SEPARATOR_]Height[_SEPARATOR_]Xoffset[_SEPARATOR_]Yoffset[_SEPARATOR_]Xadvance\n'

def checkVersion(ver, index):
    try: ver = float(ver)
    except: return
    
    if   index == 0: _VERSION_ = _ACT_VERSION_
    elif index == 1: _VERSION_ = _AFT_VERSION_
    elif index == 2: _VERSION_ = _AFF_VERSION_
    else: return
    
    if ver == _VERSION_: return
    QMessageBox.about(
        None, "!!تحذير", f"النسخة {_VERSION_} غير متوافقة.\n(ستتم العملية على أي حال.)"
        )

ArabicChars = '؟،؛ـءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيپچڤ'
FreezedArabicChars = 'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼﭬﭭﭫﭪﭼﭽﭻﭺﭘﭙﭗﭖ'
CharsConnectBoth = 'ئبتثجحخسشصضطظعغفقكلمنهيپچڤـ'
CharsConnectBefore = 'آأؤإاةدذرزوى'
Harakat = 'َﱠﳲﱠﳳﱢﳴﱞﱟﹰﹱﹲﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿًٌٍَُِّْ'
EnglishChars = '?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
ExtendedASCII = '¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'
Symbols = '!"#$%&\'()*+,-./:;<=>@[\\]^_`{|}~'
Numbers = '0123456789٠١٢٣٤٥٦٧٨٩'
neutralChars = ' '
Returns = '\n\r'
bowsList = ['()', '[]', '{}', '<>', '＜＞', '「」', '《》', '〈〉', '『』', '【】', '〔〕', '〖〗', '〘〙', '〚〛',
    '❨❩', '❪❫', '❬❭', '❮❯', '❰❱', '❲❳', '❴❵'
]
