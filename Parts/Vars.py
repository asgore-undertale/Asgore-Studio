from PyQt5.QtWidgets import QMessageBox

_ACT_VERSION_ = 1.0
_AFT_VERSION_ = 1.0
_ACT_SEPARATOR_ = "█"
_CSV_DELIMITER_ = ','

def checkActVersion(ver):
    try: ver = float(ver)
    except: return
    if ver == _ACT_VERSION_: return
    QMessageBox.about(
        None, "!!تحذير", f"النسخة {_ACT_VERSION_} غير متوافقة.\n(ستتم العملية على أي حال.)"
        )

def checkAftVersion(ver):
    try: ver = float(ver)
    except: return
    if ver == _AFT_VERSION_: return
    QMessageBox.about(
        None, "!!تحذير", f"النسخة {_AFT_VERSION_} غير متوافقة.\n(ستتم العملية على أي حال.)"
        )

ArabicChars = '؟،؛ـءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيپچڤ'
FreezedArabicChars = 'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼﭬﭭﭫﭪﭼﭽﭻﭺﭘﭙﭗﭖ'
CharsConnectBoth = 'ئبتثجحخسشصضطظعغفقكلمنهيپچڤـ'
CharsConnectBefore = 'آأؤإاةدذرزوى'
Harakat = 'َﱠﳲﱠﳳﱢﳴﱞﱟﹰﹱﹲﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿًٌٍَُِّْ'
EnglishChars = '?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
Symbols = '!"#$%&\'()*+,-./:;<=>@[\\]^_`{|}~'
Numbers = '0123456789٠١٢٣٤٥٦٧٨٩'
neutralChars = ' '
Returns = '\n\r'
bowsList = ['()', '[]', '{}', '<>', '＜＞', '「」', '《》', '〈〉', '『』', '【】', '〔〕', '〖〗', '〘〙', '〚〛',
    '❨❩', '❪❫', '❬❭', '❮❯', '❰❱', '❲❳', '❴❵'
]
