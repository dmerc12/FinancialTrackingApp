import unittest.mock as mock
from datetime import datetime, timedelta, date

from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.CustomError import CustomError
from Entities.Deposit import Deposit

deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao)

successful_deposit = Deposit(0, -1, -1, datetime.now().date(), 'test description', 5.00)
current_deposit_id = 1
updated_deposit = Deposit(current_deposit_id, -1, -1, datetime.now().date() - timedelta(days=7),
                          'updated description', 10.00)

def test_create_deposit_category_id_not_integer():
    try:
        test_deposit = Deposit(0, -1, '', datetime.now().date(), 'description', 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_create_deposit_category_not_set():
    try:
        test_deposit = Deposit(0, -1, 0, datetime.now().date(), 'description', 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "A category must be set, please try again!"

def test_create_deposit_category_not_found():
    try:
        test_deposit = Deposit(0, -1, -579356834926, datetime.now().date(), 'description', 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_create_deposit_date_not_date():
    try:
        test_deposit = Deposit(0, -1, -1, str(datetime.now().date()), 'description', 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a date, please try again!"

def test_create_deposit_date_default():
    try:
        test_deposit = Deposit(0, -1, -1, date(1900, 1, 1), 'description', 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_create_deposit_description_not_string():
    try:
        test_deposit = Deposit(0, -1, -1, datetime.now().date(), 5, 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_create_deposit_description_empty():
    try:
        test_deposit = Deposit(0, -1, -1, datetime.now().date(), '', 10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_create_deposit_amount_negative_or_0():
    try:
        test_deposit = Deposit(0, -1, -1, datetime.now().date(), 'description', -10.00)
        deposit_sao.create_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_create_deposit_user_id_not_integer():
    pass

def test_create_deposit_user_not_found():
    pass

def test_create_deposit_success():
    result = deposit_sao.create_deposit(successful_deposit)
    assert result.deposit_id != 0

def test_get_deposit_id_not_integer():
    try:
        deposit_sao.get_deposit('')
        assert False
    except CustomError as error:
        assert str(error) == "The deposit ID field must be an integer, please try again!"

def test_get_deposit_not_found():
    try:
        deposit_sao.get_deposit(-3869529838)
        assert False
    except CustomError as error:
        assert str(error) == "Deposit not found, please try again!"

def test_get_deposit_success():
    result = deposit_sao.get_deposit(current_deposit_id)
    assert result is not None

def test_get_all_deposits_none_found():
    with mock.patch.object(deposit_sao.deposit_dao, 'get_all_deposits', return_value=[]):
        try:
            deposit_sao.get_all_deposits(successful_deposit.user_id)
            assert False
        except CustomError as error:
            assert str(error) == "No deposits found, please try again!"

def test_get_all_deposits_success():
    result = deposit_sao.get_all_deposits(successful_deposit.user_id)
    assert len(result) > 0

def test_get_deposits_by_category_category_id_not_integer():
    try:
        deposit_sao.get_deposits_by_category("nope")
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_get_deposits_by_category_none_found():
    try:
        deposit_sao.get_deposits_by_category(-2)
        assert False
    except CustomError as error:
        assert str(error) == "No deposits found, please try again!"

def test_get_deposits_by_category_category_not_found():
    try:
        deposit_sao.get_deposits_by_category(-5849732023984)
        assert False
    except CustomError as error:
        assert str(error) == "No deposits found, please try again!"

def test_get_deposits_by_category_success():
    result = deposit_sao.get_deposits_by_category(successful_deposit.category_id)
    assert len(result) > 0

def test_get_deposits_by_date_date_not_date():
    try:
        deposit_sao.get_deposits_by_date(13336820)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a string, please try again!"

def test_get_deposits_by_date_date_default():
    try:
        deposit_sao.get_deposits_by_date(date(1900, 1, 1))
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_get_deposits_by_date_none_found():
    try:
        deposit_sao.get_deposits_by_date(datetime.now().date())
        assert False
    except CustomError as error:
        assert str(error) == "No deposits found, please try again!"

def test_get_deposits_by_date_success():
    result = deposit_sao.get_deposits_by_date(successful_deposit.date)
    assert len(result) > 0

def test_get_deposits_total_by_category_success():
    pass

def test_get_deposits_total_by_month_success():
    pass

def test_get_deposits_total_by_year_success():
    pass

def test_get_deposits_by_description_key_words_success():
    pass

def test_update_deposit_user_id_not_integer():
    pass

def test_update_deposit_user_not_found():
    pass

def test_update_deposit_category_id_not_integer():
    try:
        test_deposit = Deposit(current_deposit_id, -1, '', datetime.now().date(), 'test description', 5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_update_deposit_category_not_found():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1578576467, datetime.now().date(), 'test description', 5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_update_deposit_date_not_date():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1, str(datetime.now().date()), 'test description', 5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a date, please try again!"

def test_update_deposit_date_default():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1, date(1900, 1, 1), 'test description', 5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_update_deposit_description_not_string():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1, datetime.now().date(), 6, 5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_update_deposit_description_empty():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1, datetime.now().date(), '', 5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_update_deposit_amount_not_float():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1, datetime.now().date(), 'test description', '5.00')
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_update_deposit_amount_negative_or_0():
    try:
        test_deposit = Deposit(current_deposit_id, -1, -1, datetime.now().date(), 'test description', -5.00)
        deposit_sao.update_deposit(test_deposit)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_update_deposit_success():
    result = deposit_sao.update_deposit(updated_deposit)
    assert result.date != successful_deposit.date and result.description != successful_deposit.description and \
           result.amount != successful_deposit.amount

def test_delete_deposit_not_found():
    try:
        deposit_sao.delete_deposit(-37542792)
        assert False
    except CustomError as error:
        assert str(error) == "Deposit not found, please try again!"

def test_delete_deposit_id_not_integer():
    try:
        deposit_sao.delete_deposit('')
        assert False
    except CustomError as error:
        assert str(error) == "The deposit ID field must be an integer, please try again!"

def test_delete_deposit_success():
    result = deposit_sao.delete_deposit(current_deposit_id)
    assert result

def test_delete_all_deposits_user_id_not_integer():
    pass

def test_delete_all_deposits_user_not_found():
    pass

def test_delete_all_deposits_success():
    pass
