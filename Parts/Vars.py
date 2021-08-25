from PyQt5.QtWidgets import QMessageBox

_ATE_VERSION_ = 1.0
_ATE_SEPARATOR_ = "█"
_CSV_DELIMITER_ = ','

def checkVersion(ver : int):
    if ver == _ATE_VERSION_: return
    QMessageBox.about(
        None, "!!تحذير", f"النسخة {_ATE_VERSION_} غير مدعومة.\n(ستتم العملية على أي حال.)"
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
