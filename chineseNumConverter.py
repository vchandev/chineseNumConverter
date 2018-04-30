def convert(num):
  
  chineseNum = ''
  quotient = 0
  upperQuotient = 0
  upperRemainder = 0
  remainder = num
  
  chineseDict = {int(10000): str('萬'),
                       1000: '千',
                        100: '百',
                         10: '十',
                          9: '九',
                          8: '八',
                          7: '七',
                          6: '六',
                          5: '五',
                          4: '四',
                          3: '三',
                          2: '二',
                          1: '一'
                }
  
  for key, value in chineseDict.items():
    
    quotient = int(remainder/key)
    
    if quotient == 0:
      continue
    
    if quotient >= 1:
      if quotient > 10:
        upperRemainder = int(quotient)
        
        for k, v in chineseDict.items():
          
          upperQuotient = int(upperRemainder/k)
          
          if upperQuotient == 0:
            continue
          
          if upperRemainder < 10:
            chineseNum += v
            break
          
          if upperRemainder >= 10 and upperRemainder < 20:
            chineseNum += chineseDict.get(k)
        
          if upperRemainder >= 20:
            chineseNum += chineseDict.get(upperQuotient)
            chineseNum += chineseDict.get(k)
            
          upperRemainder = int(upperRemainder%k)
        
      if quotient < 10 and remainder > 20:
        chineseNum += chineseDict.get(quotient)
        chineseNum += chineseDict.get(key)
      else:
        chineseNum += chineseDict.get(key)
  
    remainder = int(remainder%key)
  
  return chineseNum

def main():
  n = 0
  result = ''
  n = input("Enter a number(1-9,999,999):")
  n = int(n)
  if n < 1 or n > 9999999:
    print('Invalid Number')
  else:
    convert(n)
    result = convert(n)
    print("Chinese numeral: ", result)
  
main()