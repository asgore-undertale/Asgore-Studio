from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze

Samples = { 'ﺋﺎ' : 'ﯪ', 'ﺌﺎ' : 'ﯫ', 'ﺋﻪ' : 'ﯬ', 'ﺌﻪ' : 'ﯭ', 'ﺋﻮ' : 'ﯮ', 'ﺌﻮ' : 'ﯯ', 'ﺋﻲ' : 'ﰄ', 'ﺌﻲ' : 'ﱩ',
            'ﺋﻴ' : 'ﯸ', 'ﺋﻰ' : 'ﰃ', 'ﺌﻰ' : 'ﱨ', 'ﺋﺞ' : 'ﰀ', 'ﺋﺢ' : 'ﰁ', 'ﺋﻢ' : 'ﰂ', 'ﺑﺞ' : 'ﰅ', 'ﺑﺢ' : 'ﰆ',
            'ﺑﺦ' : 'ﰇ', 'ﺑﻢ' : 'ﰈ', 'ﺑﻰ' : 'ﰉ', 'ﺑﻲ' : 'ﰊ', 'ﺗﺞ' : 'ﰋ', 'ﺗﺢ' : 'ﰌ', 'ﺗﺦ' : 'ﰍ', 'ﺗﻢ' : 'ﰎ',
            'ﺗﻰ' : 'ﰏ', 'ﺗﻲ' : 'ﰐ', 'ﺛﺞ' : 'ﰑ', 'ﺛﻢ' : 'ﰒ', 'ﺛﻰ' : 'ﰓ', 'ﺛﻲ' : 'ﰔ', 'ﺟﺢ' : 'ﰕ', 'ﺟﻢ' : 'ﰖ',
            'ﺣﺞ' : 'ﰗ', 'ﺣﻢ' : 'ﰘ', 'ﺧﺞ' : 'ﰙ', 'ﺧﺢ' : 'ﰚ', 'ﺧﻢ' : 'ﰛ', 'ﺳﺞ' : 'ﰜ', 'ﺳﺢ' : 'ﰝ', 'ﺳﺦ' : 'ﰞ',
            'ﺳﻢ' : 'ﰟ', 'ﺻﺢ' : 'ﰠ', 'ﺻﻢ' : 'ﰡ', 'ﺿﺞ' : 'ﰢ', 'ﺿﺢ' : 'ﰣ', 'ﺿﺦ' : 'ﰤ', 'ﺿﻢ' : 'ﰥ', 'ﻃﺢ' : 'ﰦ',
            'ﻃﻢ' : 'ﰧ', 'ﻇﻢ' : 'ﰨ', 'ﻋﺞ' : 'ﰩ', 'ﻋﻢ' : 'ﰪ', 'ﻏﺞ' : 'ﰫ', 'ﻏﻢ' : 'ﰬ', 'ﻓﺞ' : 'ﰭ', 'ﻓﺢ' : 'ﰮ',
            'ﻓﺦ' : 'ﰯ', 'ﻓﻢ' : 'ﰰ', 'ﻓﻰ' : 'ﰱ', 'ﻓﻲ' : 'ﰲ', 'ﻗﺢ' : 'ﰳ', 'ﻗﻢ' : 'ﰴ', 'ﻗﻰ' : 'ﰵ', 'ﻗﻲ' : 'ﰶ',
            'ﻛﺎ' : 'ﰷ', 'ﻛﺞ' : 'ﰸ', 'ﻛﺢ' : 'ﰹ', 'ﻛﺦ' : 'ﰺ', 'ﻛﻞ' : 'ﰻ', 'ﻛﻢ' : 'ﰼ', 'ﻛﻰ' : 'ﰽ', 'ﻛﻲ' : 'ﰾ',
            'ﻟﺞ' : 'ﰿ', 'ﻟﺢ' : 'ﱀ', 'ﻟﺦ' : 'ﱁ', 'ﻟﻢ' : 'ﱂ', 'ﻟﻰ' : 'ﱃ', 'ﻟﻲ' : 'ﱄ', 'ﻣﺞ' : 'ﱅ', 'ﻣﺢ' : 'ﱆ',
            'ﻣﺦ' : 'ﱇ', 'ﻣﻢ' : 'ﱈ', 'ﻣﻰ' : 'ﱉ', 'ﻣﻲ' : 'ﱊ', 'ﻧﺞ' : 'ﱋ', 'ﻧﺢ' : 'ﱌ', 'ﻧﺦ' : 'ﱍ', 'ﻧﻢ' : 'ﱎ',
            'ﻧﻰ' : 'ﱏ', 'ﻧﻲ' : 'ﱐ', 'ﻫﺞ' : 'ﱑ', 'ﻫﻢ' : 'ﱒ', 'ﻫﻰ' : 'ﱓ', 'ﻫﻲ' : 'ﱔ', 'ﻳﺞ' : 'ﱕ', 'ﻳﺢ' : 'ﱖ',
            'ﻳﺦ' : 'ﱗ', 'ﻳﻢ' : 'ﱘ', 'ﻳﻰ' : 'ﱙ', 'ﻳﻲ' : 'ﱚ', 'ﹼﹲ' : 'ﱞ', 'ﹼﹴ' : 'ﱟ', 'ﹼﹶ' : 'ﱠ', 'ﹼﹸ' : 'ﱡ',
            'ﹼﹺ' : 'ﱢ', 'ﺌﺮ' : 'ﱤ', 'ﺌﺰ' : 'ﱥ', 'ﺌﻢ' : 'ﱦ', 'ﺌﻦ' : 'ﱧ', 'ﺒﺮ' : 'ﱪ', 'ﺒﺰ' : 'ﱫ', 'ﺒﻢ' : 'ﱬ',
            'ﺒﻦ' : 'ﱭ', 'ﺒﻰ' : 'ﱮ', 'ﺒﻲ' : 'ﱯ', 'ﺘﺮ' : 'ﱰ', 'ﺘﺰ' : 'ﱱ', 'ﺘﻢ' : 'ﱲ', 'ﺘﻦ' : 'ﱳ', 'ﺘﻰ' : 'ﱴ',
            'ﺘﻲ' : 'ﱵ', 'ﺜﺮ' : 'ﱶ', 'ﺜﺰ' : 'ﱷ', 'ﺜﻢ' : 'ﱸ', 'ﺜﻦ' : 'ﱹ', 'ﺜﻰ' : 'ﱺ', 'ﺜﻲ' : 'ﱻ', 'ﻔﻰ' : 'ﱼ',
            'ﻔﻲ' : 'ﱽ', 'ﻘﻰ' : 'ﱾ', 'ﻘﻲ' : 'ﱿ', 'ﻜﺎ' : 'ﲀ', 'ﻜﻞ' : 'ﲁ', 'ﻜﻢ' : 'ﲂ', 'ﻜﻰ' : 'ﲃ', 'ﻜﻲ' : 'ﲄ',
            'ﻠﻢ' : 'ﲅ', 'ﻠﻰ' : 'ﲆ', 'ﻠﻲ' : 'ﲇ', 'ﻤﺎ' : 'ﲈ', 'ﻤﻢ' : 'ﲉ', 'ﻨﺮ' : 'ﲊ', 'ﻨﺰ' : 'ﲋ', 'ﻨﻢ' : 'ﲌ',
            'ﻨﻦ' : 'ﲍ', 'ﻨﻰ' : 'ﲎ', 'ﻨﻲ' : 'ﲏ', 'ﻴﺮ' : 'ﲑ', 'ﻴﺰ' : 'ﲒ', 'ﻴﻢ' : 'ﲓ', 'ﻴﻦ' : 'ﲔ', 'ﻴﻰ' : 'ﲕ',
            'ﻴﻲ' : 'ﲖ', 'ﺋﺠ' : 'ﲗ', 'ﺋﺤ' : 'ﲘ', 'ﺋﺨ' : 'ﲙ', 'ﺋﻤ' : 'ﲚ', 'ﺋﻬ' : 'ﲛ', 'ﺑﺠ' : 'ﲜ', 'ﺑﺤ' : 'ﲝ',
            'ﺑﺨ' : 'ﲞ', 'ﺑﻤ' : 'ﲟ', 'ﺑﻬ' : 'ﲠ', 'ﺗﺠ' : 'ﲡ', 'ﺗﺤ' : 'ﲢ', 'ﺗﺨ' : 'ﲣ', 'ﺗﻤ' : 'ﲤ', 'ﺗﻬ' : 'ﲥ',
            'ﺜﻤ' : 'ﳥ', 'ﺟﺤ' : 'ﲧ', 'ﺟﻤ' : 'ﲨ', 'ﺣﺠ' : 'ﲩ', 'ﺣﻤ' : 'ﲪ', 'ﺧﺠ' : 'ﲫ', 'ﺧﻤ' : 'ﲬ', 'ﺳﺠ' : 'ﲭ',
            'ﺳﺤ' : 'ﲮ', 'ﺳﺨ' : 'ﲯ', 'ﺳﻤ' : 'ﲰ', 'ﺻﺤ' : 'ﲱ', 'ﺻﺨ' : 'ﲲ', 'ﺻﻤ' : 'ﲳ', 'ﺿﺠ' : 'ﲴ', 'ﺿﺤ' : 'ﲵ',
            'ﺿﺨ' : 'ﲶ', 'ﺿﻤ' : 'ﲷ', 'ﻃﺤ' : 'ﲸ', 'ﻇﻤ' : 'ﲹ', 'ﻋﺠ' : 'ﲺ', 'ﻋﻤ' : 'ﲻ', 'ﻏﺠ' : 'ﲼ', 'ﻏﻤ' : 'ﲽ',
            'ﻓﺠ' : 'ﲾ', 'ﻓﺤ' : 'ﲿ', 'ﻓﺨ' : 'ﳀ', 'ﻓﻤ' : 'ﳁ', 'ﻗﺤ' : 'ﳂ', 'ﻗﻤ' : 'ﳃ', 'ﻛﺠ' : 'ﳄ', 'ﻛﺤ' : 'ﳅ',
            'ﻛﺨ' : 'ﳆ', 'ﻛﻠ' : 'ﳇ', 'ﻛﻤ' : 'ﳈ', 'ﻟﺠ' : 'ﳉ', 'ﻟﺤ' : 'ﳊ', 'ﻟﺨ' : 'ﳋ', 'ﻟﻤ' : 'ﳌ', 'ﻟﻬ' : 'ﳍ',
            'ﻣﺠ' : 'ﳎ', 'ﻣﺤ' : 'ﳏ', 'ﻣﺨ' : 'ﳐ', 'ﻣﻤ' : 'ﳑ', 'ﻧﺠ' : 'ﳒ', 'ﻧﺤ' : 'ﳓ', 'ﻧﺨ' : 'ﳔ', 'ﻧﻤ' : 'ﳕ',
            'ﻧﻬ' : 'ﳖ', 'ﻫﺠ' : 'ﳗ', 'ﻫﻤ' : 'ﳘ', 'ﻳﺠ' : 'ﳚ', 'ﻳﺤ' : 'ﳛ', 'ﻳﺨ' : 'ﳜ', 'ﻳﻤ' : 'ﳝ', 'ﻳﻬ' : 'ﳞ',
            'ﺌﻤ' : 'ﳟ', 'ﺌﻬ' : 'ﳠ', 'ﺒﻤ' : 'ﳡ', 'ﺒﻬ' : 'ﳢ', 'ﺘﻤ' : 'ﳣ', 'ﺘﻬ' : 'ﳤ', 'ﺜﻬ' : 'ﳦ', 'ﺴﻤ' : 'ﳧ',
            'ﺴﻬ' : 'ﳨ', 'ﺸﻤ' : 'ﳩ', 'ﺸﻬ' : 'ﳪ', 'ﻜﻠ' : 'ﳫ', 'ﻜﻤ' : 'ﳬ', 'ﻠﻤ' : 'ﳭ', 'ﻨﻤ' : 'ﳮ', 'ﻨﻬ' : 'ﳯ',
            'ﻴﻤ' : 'ﳰ', 'ﻴﻬ' : 'ﳱ', 'ﻃﻰ' : 'ﳵ', 'ﻃﻲ' : 'ﳶ', 'ﻋﻰ' : 'ﳷ', 'ﻋﻲ' : 'ﳸ', 'ﻏﻰ' : 'ﳹ', 'ﻏﻲ' : 'ﳺ',
            'ﺳﻰ' : 'ﳻ', 'ﺳﻲ' : 'ﳼ', 'ﺷﻰ' : 'ﳽ', 'ﺷﻲ' : 'ﳾ', 'ﺣﻰ' : 'ﳿ', 'ﺣﻲ' : 'ﴀ', 'ﺟﻰ' : 'ﴁ', 'ﺟﻲ' : 'ﴂ',
            'ﺧﻰ' : 'ﴃ', 'ﺧﻲ' : 'ﴄ', 'ﺻﻰ' : 'ﴅ', 'ﺻﻲ' : 'ﴆ', 'ﺿﻰ' : 'ﴇ', 'ﺿﻲ' : 'ﴈ', 'ﺷﺞ' : 'ﴉ', 'ﺷﺢ' : 'ﴊ',
            'ﺷﺦ' : 'ﴋ', 'ﺷﻢ' : 'ﴌ', 'ﺷﺮ' : 'ﴍ', 'ﺳﺮ' : 'ﴎ', 'ﺻﺮ' : 'ﴏ', 'ﺿﺮ' : 'ﴐ', 'ﻄﻰ' : 'ﴑ', 'ﻄﻲ' : 'ﴒ',
            'ﻌﻰ' : 'ﴓ', 'ﻌﻲ' : 'ﴔ', 'ﻐﻰ' : 'ﴕ', 'ﻐﻲ' : 'ﴖ', 'ﺴﻰ' : 'ﴗ', 'ﺴﻲ' : 'ﴘ', 'ﺸﻰ' : 'ﴙ', 'ﺸﻲ' : 'ﴚ',
            'ﺤﻰ' : 'ﴛ', 'ﺤﻲ' : 'ﴜ', 'ﺠﻰ' : 'ﴝ', 'ﺠﻲ' : 'ﴞ', 'ﺨﻰ' : 'ﴟ', 'ﺨﻲ' : 'ﴠ', 'ﺼﻰ' : 'ﴡ', 'ﺼﻲ' : 'ﴢ',
            'ﻀﻰ' : 'ﴣ', 'ﻀﻲ' : 'ﴤ', 'ﺸﺞ' : 'ﴥ', 'ﺸﺢ' : 'ﴦ', 'ﺸﺦ' : 'ﴧ', 'ﺸﻢ' : 'ﴨ', 'ﺸﺮ' : 'ﴩ', 'ﺴﺮ' : 'ﴪ',
            'ﺼﺮ' : 'ﴫ', 'ﻀﺮ' : 'ﴬ', 'ﺷﺠ' : 'ﴭ', 'ﺷﺤ' : 'ﴮ', 'ﺷﺨ' : 'ﴯ', 'ﺷﻤ' : 'ﴰ', 'ﺳﻬ' : 'ﴱ', 'ﺷﻬ' : 'ﴲ',
            'ﻃﻤ' : 'ﴳ', 'ﺴﺠ' : 'ﴴ', 'ﺴﺤ' : 'ﴵ', 'ﺴﺨ' : 'ﴶ', 'ﺸﺠ' : 'ﴷ', 'ﺸﺤ' : 'ﴸ', 'ﺸﺨ' : 'ﴹ', 'ﻄﻤ' : 'ﴺ',
            'ﻈﻤ' : 'ﴻ', 'ﺎﹰ' : 'ﴼ', 'ﺍﹰ' : 'ﴽ',
            'ﺗﺠﻤ' : 'ﵐ', 'ﺘﺤﺞ' : 'ﵑ', 'ﺗﺤﺠ' : 'ﵒ', 'ﺗﺤﻤ' : 'ﵓ', 'ﺗﺨﻤ' : 'ﵔ', 'ﺗﻤﺠ' : 'ﵕ', 'ﺗﻤﺤ' : 'ﵖ', 'ﺗﻤﺨ' : 'ﵗ',
            'ﺠﻤﺢ' : 'ﵘ', 'ﺟﻤﺤ' : 'ﵙ', 'ﺤﻤﻲ' : 'ﵚ', 'ﺤﻤﻰ' : 'ﵛ', 'ﺳﺤﺠ' : 'ﵜ', 'ﺳﺠﺤ' : 'ﵝ', 'ﺴﺠﻰ' : 'ﵞ', 'ﺴﻤﺢ' : 'ﵟ',
            'ﺳﻤﺤ' : 'ﵠ', 'ﺳﻤﺠ' : 'ﵡ', 'ﺴﻤﻢ' : 'ﵢ', 'ﺳﻤﻤ' : 'ﵣ', 'ﺼﺤﺢ' : 'ﵤ', 'ﺻﺤﺤ' : 'ﵥ', 'ﺼﻤﻢ' : 'ﵦ', 'ﺸﺤﻢ' : 'ﵧ',
            'ﺷﺤﻤ' : 'ﵨ', 'ﺸﺠﻲ' : 'ﵩ', 'ﺸﻤﺦ' : 'ﵪ', 'ﺷﻤﺨ' : 'ﵫ', 'ﺸﻤﻢ' : 'ﵬ', 'ﺷﻤﻤ' : 'ﵭ', 'ﻀﺤﻰ' : 'ﵮ', 'ﻀﺨﻢ' : 'ﵯ',
            'ﺿﺨﻤ' : 'ﵰ', 'ﻄﻤﺢ' : 'ﵱ', 'ﻃﻤﺤ' : 'ﵲ', 'ﻃﻤﻤ' : 'ﵳ', 'ﻄﻤﻲ' : 'ﵴ', 'ﻌﺠﻢ' : 'ﵵ', 'ﻌﻤﻢ' : 'ﵶ', 'ﻋﻤﻤ' : 'ﵷ',
            'ﻌﻤﻰ' : 'ﵸ', 'ﻐﻤﻢ' : 'ﵹ', 'ﻐﻤﻲ' : 'ﵺ', 'ﻐﻤﻰ' : 'ﵻ', 'ﻔﺨﻢ' : 'ﵼ', 'ﻓﺨﻤ' : 'ﵽ', 'ﻘﻤﺢ' : 'ﵾ', 'ﻘﻤﻢ' : 'ﵿ',
            'ﻠﺤﻢ' : 'ﶀ', 'ﻠﺤﻲ' : 'ﶁ', 'ﻠﺤﻰ' : 'ﶂ', 'ﻟﺠﺠ' : 'ﶃ', 'ﻠﺠﺞ' : 'ﶄ', 'ﻠﺨﻢ' : 'ﶅ', 'ﻟﺨﻤ' : 'ﶆ', 'ﻠﻤﺢ' : 'ﶇ',
            'ﻟﻤﺤ' : 'ﶈ', 'ﻣﺤﺠ' : 'ﶉ', 'ﻣﺤﻤ' : 'ﶊ', 'ﻤﺤﻲ' : 'ﶋ', 'ﻣﺠﺤ' : 'ﶌ', 'ﻣﺠﻤ' : 'ﶍ', 'ﻣﺨﺠ' : 'ﶎ', 'ﻣﺨﻤ' : 'ﶏ',
            'ﻣﺠﺨ' : 'ﶒ', 'ﻫﻤﺠ' : 'ﶓ', 'ﻫﻤﻤ' : 'ﶔ', 'ﻧﺤﻤ' : 'ﶕ', 'ﻨﺤﻰ' : 'ﶖ', 'ﻨﺤﻢ' : 'ﶗ', 'ﻧﺠﻤ' : 'ﶘ', 'ﻨﺠﻰ' : 'ﶙ',
            'ﻨﻤﻲ' : 'ﶚ', 'ﻨﻤﻰ' : 'ﶛ', 'ﻴﻤﻢ' : 'ﶜ', 'ﻳﻤﻤ' : 'ﶝ', 'ﺒﺨﻲ' : 'ﶞ', 'ﺘﺠﻲ' : 'ﶟ', 'ﺘﺠﻰ' : 'ﶠ', 'ﺘﺨﻲ' : 'ﶡ',
            'ﺘﺨﻰ' : 'ﶢ', 'ﺘﻤﻲ' : 'ﶣ', 'ﺘﻤﻰ' : 'ﶤ', 'ﺠﻤﻲ' : 'ﶥ', 'ﺠﺤﻰ' : 'ﶦ', 'ﺠﻤﻰ' : 'ﶧ', 'ﺴﺨﻰ' : 'ﶨ', 'ﺼﺤﻲ' : 'ﶩ',
            'ﺸﺤﻲ' : 'ﶪ', 'ﻀﺤﻲ' : 'ﶫ', 'ﻠﺠﻲ' : 'ﶬ', 'ﻠﻤﻲ' : 'ﶭ', 'ﻴﺤﻲ' : 'ﶮ', 'ﻴﺠﻲ' : 'ﶯ', 'ﻴﻤﻲ' : 'ﶰ', 'ﻤﻤﻲ' : 'ﶱ',
            'ﻘﻤﻲ' : 'ﶲ', 'ﻨﺤﻲ' : 'ﶳ', 'ﻗﻤﺤ' : 'ﶴ', 'ﻟﺤﻤ' : 'ﶵ', 'ﻌﻤﻲ' : 'ﶶ', 'ﻜﻤﻲ' : 'ﶷ', 'ﻧﺠﺤ' : 'ﶸ', 'ﻤﺨﻲ' : 'ﶹ',
            'ﻟﺠﻤ' : 'ﶺ', 'ﻜﻤﻢ' : 'ﶻ', 'ﻠﺠﻢ' : 'ﶼ', 'ﻨﺠﺢ' : 'ﶽ', 'ﺠﺤﻲ' : 'ﶾ', 'ﺤﺠﻲ' : 'ﶿ', 'ﻤﺠﻲ' : 'ﷀ', 'ﻔﻤﻲ' : 'ﷁ',
            'ﺒﺤﻲ' : 'ﷂ', 'ﻛﻤﻤ' : 'ﷃ', 'ﻋﺠﻤ' : 'ﷄ', 'ﺻﻤﻤ' : 'ﷅ', 'ﺴﺨﻲ' : 'ﷆ', 'ﻨﺠﻲ' : 'ﷇ',
            'ﺍﻟﻠﻪ' : 'ﷲ', 'ﺍﻛﺒﺮ' : 'ﷳ', 'ﻣﺤﻤﺪ' : 'ﷴ', 'ﺻﻠﻌﻢ' : 'ﷵ', 'ﺭﺳﻮﻝ' : 'ﷶ', 'ﺻﻠﻰ ﺍﻟﻠﻪ ﻋﻠﻴﻪ ﻭﺳﻠﻢ' : 'ﷺ', 'ﻋﻠﻴﻪ' : 'ﷷ',
            'ﻭﺳﻠﻢ' : 'ﷸ', 'ﺻﻠﻰ' : 'ﷹ', 'ﺟﻞ ﺟﻼﻟﻪ' : 'ﷻ', 'ﺭﻳﺎﻝ' : '﷼', 'ﺑﺴﻢ ﺍﻟﻠﻪ ﺍﻟﺮﺣﻤﻦ ﺍﻟﺮﺣﻴﻢ' : '﷽'
    }
maxSampleLength = 2
# available = '﷼﷽'

def returnMostPrevalent(text):
    sample, num = '', 0
    for k in Samples.keys():
        if len(k) > maxSampleLength or len(k) < 2: continue
        counter = text.count(k)
        if len(k) > len(sample) and counter > 0: sample, num = k, counter
        elif num < counter: sample, num = k, counter # and sample in available
    return sample, num

def analyzeText(text, num):
    if not text: return
    if maxSampleLength < 2: return
    _, i = '', 0
    
    _ += f'الطول الأصلي\t\t{len(text)}\n'
    text = Un_Freeze(text)
    _ += f'بعد التجميد\t\t{len(text)}\n\nالمجموعات البصرية وعدد ورودها:\n'
    
    while True:
        if i == num: break
        k, count = returnMostPrevalent(text)
        if not k: break
        
        i += 1
        text = text.replace(k, Samples[k])
        _ += f'[{Samples[k]}]   [{count}]\tصار الطول   {len(text)} (-{count})\n'
    
    _ += f'\nالطول بعد الاختزال\t{len(text)}'
    return text, _