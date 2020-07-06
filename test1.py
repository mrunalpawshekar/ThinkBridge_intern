import number_to_word
import pytest
#english
def test_1() :
        assert number_to_word.numToWords(12," ") == "twelve  "

def test_2():
        assert number_to_word.convertToEnglish(789) == " seven hundred eighty nine "

def test_3():
        assert number_to_word.hindinumbers(1234," ")== "    एकहज़ार  दोसौ  चौंतीस "

def test_4():
        assert number_to_word.marathinumbers(1234," ")== "      एकहजार  दोनशे  चौतीस "

def test_5():
        assert number_to_word.hindinumbers(999999999," ")== "  निन्यानवेकरोड़  निन्यानवेलाख  निन्यानवेहज़ार  नौसौ  निन्यानवे "

def test_6():
        assert number_to_word.marathinumbers(999999999," ")== "  नव्व्याण्णवकोटी  नव्व्याण्णवलाख  नव्व्याण्णवहजार  नऊशे  नव्व्याण्णव "

def test_7():
        assert number_to_word.numToWords(20,"") == "twenty "
def test_8():
        assert number_to_word.hindinumbers(789654235," ")== "  अठहतरकरोड़  छियानवेलाख  चौवनहज़ार  दोसौ  पैंतीस "
def test_9():
        assert number_to_word.marathinumbers(789654235," ")== "  अठ्ठ्याहत्तरकोटी  शहाण्णवलाख  चोपन्नहजार  दोनशे  पस्तीस "

def test_10():
        assert number_to_word.convertToEnglish(45986) == " forty five thousand nine hundred eighty six "