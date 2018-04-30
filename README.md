# chineseNumConverter

Unlike numerals written in Western languages which are grouped by thousands (1,000s), Chinese numerals are grouped by ten-thousands (10,000s) instead. This means Chinese numeral units advance every 4 places instead of 3, which makes translating between regular numbers and Chinese numerals often disorienting. Here is a Python program that performs quick and easy conversion between regular numbers to Chinese numerals.

Chinese numerals often work differently than their Western counterparts. For example, instead of "eleven", it is 十一 (ten + one). For 20, it is 二十 (two * ten); for 200, it is 二百 (two * hundred); and for 2,000, it is 二千 (two * thousand). But after that, it is not (twenty * thousand) in Chinese numerals. Instead, it is 二萬 (two * ten-thousand) and every 4 unit places, it repeats with the higher unit place. Therefore, for 200,000, it is 二十萬 (twenty * ten-thousands) and so on.

For smaller numbers under 100,000, the program tries division at every unit place level. For example, for 5,234, it appends the the value of the unit from each unit place level (key) and the unit itself (value). The final string is returned and printed.

<img width="200" alt="screen shot 2018-04-29 at 11 51 25 pm" src="https://user-images.githubusercontent.com/25806927/39414660-536d9598-4c08-11e8-8586-2851c14c6c1e.png">

For larger numbers than 100,000, the unit value at the 10,000 is first evaluated. For example, the (55* ten-thousand) in 556,000 is first evaluated. The string first builds the "55" + "ten-thousand", and then finally "6,000". The challenging part was designing the algorithm in such a way that the significant unit place does not appear before the higher units are evaluated. The second for loop is used to evaluate all of the higher units first before coming back to the rest of the lower digits.

<img width="210" alt="screen shot 2018-04-29 at 11 57 13 pm" src="https://user-images.githubusercontent.com/25806927/39414761-422f2430-4c09-11e8-8e3d-189aa49e7841.png">

With this, we can translated numbers that are in the millions. Such as:

2,547,923

<img width="271" alt="screen shot 2018-04-29 at 11 59 46 pm" src="https://user-images.githubusercontent.com/25806927/39414775-7ab2c2ee-4c09-11e8-9a3f-ece1c1d7ca1f.png">

Or even:

9,999,999

<img width="268" alt="screen shot 2018-04-30 at 12 01 12 am" src="https://user-images.githubusercontent.com/25806927/39414782-a1ff1762-4c09-11e8-98bc-aa86ae5160e5.png">




