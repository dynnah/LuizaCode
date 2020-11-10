"""Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. 
The password will be considered strong enough if 
its length is greater than or equal to 10 symbols
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it."""

def checkio(data: str) -> bool:
  length = len(data)
  if (length < 10):
      return False

  digit = False
  uppercase = False
  lowercase = False
  i = 0

  while (i<length and (not(digit) or not(uppercase) or not(lowercase))):
     characters = data[i]
     if (characters.isupper()):
        uppercase = True
     elif (characters.isdigit()):
         digit = True
     elif (characters.islower()):
         lowercase = True
         i+=1

  return (digit and uppercase and lowercase)   
   

#Nao escreve abaixo dessa linha
if __name__ == '__main__':
    print('Example:')
    print(checkio('bAse730onE4'))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Terminou?")