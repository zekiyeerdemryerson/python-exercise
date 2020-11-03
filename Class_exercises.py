#Write a Python class to convert an integer to a roman numeral

class Converter:
    @staticmethod
    def ConvertToRoman(number):
        romanValues=[(1,"I"),(5,"V"),(9,"IX"),(10,"X"),(50,"L"),(90,"XC"),(100,"C"),(400,"CD"),(900,"CM"),(1000,"M")]
        result=""
        for key,value in reversed(romanValues):
            div= number//key
            if div>0:
                result+=div*value
                number-=div*key
        return print(f"Roman Number is: {result}")

       

result=Converter.ConvertToRoman(1278)








