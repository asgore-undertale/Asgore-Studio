from PyQt5.QtWidgets import QMessageBox

_ATE_VERSION_ = 1.0
_ATE_SEPARATOR_ = "█"
_CSV_DELIMITER_ = ','

def checkVersion(ver : int):
    if ver != _ATE_VERSION_:
        QMessageBox.about(
            None, "!!تحذير", f"النسخة {_ATE_VERSION_} غير مدعومة.\n(ستتم العملية على أي حال.)"
            )

ArabicChars = '؟،؛ـءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيپچڤ'
FreezedArabicChars = 'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼﭬﭭﭫﭪﭼﭽﭻﭺﭘﭙﭗﭖ'
Space = ' '
Harakat = 'َﹰﹱﹲﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿًٌٍَُِّْ'
CharsConnectBoth = 'ئبتثجحخسشصضطظعغفقكلمنهيپچڤـ'
CharsConnectBefore = 'آأؤإاةدذرزوى'
EnglishChars = '?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
Numbers = '0123456789٠١٢٣٤٥٦٧٨٩'
Symbols = '!"#$%&\'()*+,-./:;<=>@[\\]^_`{|}~'
ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'    