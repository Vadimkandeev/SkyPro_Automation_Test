from string_utils import StringUtils
import pytest

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
@pytest.mark.parametrize(
        "str, result", 
        [
    ("revolution", "Revolution"),
    ("Revolution", "Revolution"),
    ("революция", "Революция"),
    ("123456", "123456"),
    ("№;%:", "№;%:"),
    ("大友克洋武器よさらば", "大友克洋武器よさらば")]
    )
def test_capitalize(str, result):
    stringUtils = StringUtils()
    resp = stringUtils.capitalize(str)
    assert resp == result
#-----------------------------------------------------------------

# Принимает на вход текст и удаляет пробелы в начале, если они есть--------------
@pytest.mark.parametrize("str, result", 
        [
    (" Computer","Computer"), 
    ("          NewRetroWave", "NewRetroWave"), 
    ("Some words with space", "Some words with space")]
    )
def test_trim(str, result):
    stringUtils = StringUtils()
    resp = stringUtils.trim(str) 
    assert resp == result
#-----------------------------------------------------------------
 
# Принимает на вход текст с разделителем и возвращает список строк.
@pytest.mark.parametrize(
        "str, separator, result", 
        [
    ("abc*def*ghi", "*", ["abc", "def", "ghi"]), 
    ("abc0   0ghi", "0", ["abc", "   ", "ghi"]), 
    ("абв*еёж*зий", "*", ["абв", "еёж", "зий"]), 
    ("123*456*789", "*", ["123", "456", "789"])]
    )
def test_positive_to_list(str, separator, result):
    stringUtils = StringUtils()
    resp = stringUtils.to_list(str, separator)
    assert resp == result
    
 #Ожидаемо негативный тест-----------------
@pytest.mark.xfail(
    "123/456/789", "*", ["123", "456", "789"] 
)
def test_negative_to_list(str, separator, result):
    stringUtils = StringUtils()
    # Принимает на вход текст с разделителем и возвращает список строк.
    resp = stringUtils.to_list(str, separator)
    assert resp == result
#-----------------------------------------------------------------

# Поиск символа в строке------------------------
#
# Возвращаемый результат True-------------
@pytest.mark.parametrize(
        "str, simbol", 
        [
    ("I am working right now", "o"), 
    ("大友克洋武器よさらば", "友"), 
    ("2222 5545669997322", "7"), 
    ("мама мыла раму", "р"), 
    ("@#$*&^^&^", "&")]
    )
def test_true_contains(str, simbol):
    stringUtils = StringUtils()
    resp = stringUtils.contains(str, simbol)
    assert resp == True

# Возвращаемый результат False-----------------
@pytest.mark.parametrize(
        "str, simbol",
        [
    ("I am working right now", "z"), 
    ("大友克洋武器よさらば", "R"), 
    ("2222 5545669997322", "8"), 
    ("мама мыла раму", "p"), 
    ("@#$*&^^&^", "+")]
    )
def test_false_contains(str, simbol):
    stringUtils = StringUtils()
    # Поиск символа в строке
    resp = stringUtils.contains(str, simbol)
    assert resp == False 
#------------------------------------------------------------------


# Удаление подстроки из строки--------------------
@pytest.mark.parametrize(
        "str, sub_str, result", 
        [
    ("I am working right now", "right ", "I am working now"), 
    ("казнить нельзя помиловать", "казнить ", "нельзя помиловать"), 
    ("1223 4566 58 45", "58 ", "1223 4566 45"), 
    ("大友克洋武器よさらば", "克洋", "大友武器よさらば"), 
    ("ПРОИСХОЖДЕНИЕ ВСЕЛЕННОЙ", "ПРОИС", "ХОЖДЕНИЕ ВСЕЛЕННОЙ")] 
    )
def test_delete_symbol(str, sub_str, result):
    stringUtils = StringUtils()
    resp = stringUtils.delete_symbol(str, sub_str)
    assert resp == result
#------------------------------------------------------------------

   
# Возвращает True при совпадении начального символа строки с заданным 
#
# Возвращаемый результат True-------------
@pytest.mark.parametrize(
        "str, simbol", 
        [
    ("Преследуя блики света", "П"), 
    ("Other works", "O"), 
    ("222 888 666", "2")]
    )
def test_true_starts_with(str, simbol):
    stringUtils = StringUtils()
    resp = stringUtils.starts_with(str, simbol)
    assert resp == True

# Возвращаемый результат False-------------
@pytest.mark.parametrize(
        "str, simbol", 
        [
    ("Преследуя блики света", "w"), 
    ("Other works", "q"), 
    ("222 888 666", "5")]
    )
def test_false_starts_with(str, simbol):
    stringUtils = StringUtils()
    # Возвращает True при совпадении начального символа строки с заданным 
    resp = stringUtils.starts_with(str, simbol)
    assert resp == False
#------------------------------------------------------------------

    
# Возвращает True при совпадении конечного символа строки с заданным 
#
# Возвращаемый результат True-------------
@pytest.mark.parametrize(
        "str, simbol", 
        [
    ("Преследуя блики света", "а"), 
    ("Other works", "s"), 
    ("222 888 666", "6")]
    )
def test_true_end_with(str, simbol):
    stringUtils = StringUtils()
    resp = stringUtils.end_with(str, simbol)
    assert resp == True

# Возвращаемый результат False-------------
@pytest.mark.parametrize(
        "str, simbol", 
        [
    ("Преследуя блики света", "e"), 
    ("Other works", "w"), 
    ("222 888 666", "9")]
    )
def test_false_end_with(str, simbol):
    stringUtils = StringUtils()
    resp = stringUtils.end_with(str, simbol)
    assert resp == False   
#------------------------------------------------------------------  

# Возвращает True  усли строка пуста
#
# Возвращаемый результат True-------------
def test_false_is_empty():
    stringUtils = StringUtils()
    resp = stringUtils.is_empty("Минимальная комплектация")
    assert resp == False

# Возвращаемый результат False-------------
def test_true_is_empty():
    stringUtils = StringUtils()
    resp = stringUtils.is_empty("")
    assert resp == True
#------------------------------------------------------------------     


#Преобразует список в строку  с заданным разделителем
@pytest.mark.parametrize(
        "lst, separator, result", 
        [
    (["и", "н", "т", "е", "г", "р", 'а', 'ц', 'и', 'о', "н", "н", "ы", "м"], "-", "и-н-т-е-г-р-а-ц-и-о-н-н-ы-м"), 
    (["w", "e", "a", "t", "h", "e", "r"], "-", "w-e-a-t-h-e-r"), 
    (["1", "2", "3", "4", "5", "6", "7", "8", "9"], "-", "1-2-3-4-5-6-7-8-9"), 
    (["大", "友", "克", "洋", "武", "器", "よ", "さ", "ら", "ば"], "-", "大-友-克-洋-武-器-よ-さ-ら-ば")]
    )
def test_list_to_string(lst, separator, result):
    stringUtils = StringUtils()
    resp = stringUtils.list_to_string(lst, separator)
    assert resp == result
#------------------------------------------------------------------    