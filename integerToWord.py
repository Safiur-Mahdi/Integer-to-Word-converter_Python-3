# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:30:53 2021

@author: safiur
"""
import time

twentyOrLess = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
multiplesOfTen = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
thousandOrMore = ['Thousand','Million','Billion']

def integerToWordConverter( integerNumber ):
    """A recursive function to convert a non-negative integer to word
    :param integerNumber: non-negative integer number
    """
    if integerNumber == 0:
        return []
    if integerNumber < 20:
        return [ twentyOrLess[integerNumber] ]
    if integerNumber < 100:
        return [ multiplesOfTen[integerNumber // 10] ] + integerToWordConverter( integerNumber % 10 )
    if integerNumber < 1000:
        return [ twentyOrLess[integerNumber // 100 ], 'Hundred' ] + integerToWordConverter( integerNumber % 100 )
    for power_, thousandPower in enumerate( thousandOrMore, 1 ):
        if integerNumber < 1000**(power_+1):
            return integerToWordConverter( integerNumber // 1000 ** power_ ) + [ thousandPower ] + integerToWordConverter( integerNumber % 1000 ** power_ )

def main( integerNumber ):
    result = integerToWordConverter( integerNumber )
    print( ' '.join(result) if result else 'Zero')

if __name__ == '__main__':
    try:
        integerNumber = int( input("Please enter a non-negative integer number: ") )
        start = time.time()
        main ( integerNumber )
        end =  time.time()
        print(f'\nTotal execution time: {end-start:.2f} seconds.')
    except ValueError:
        print('Please enter a non-negative integer number only!')
    except Exception as ex:
        print( ex )
