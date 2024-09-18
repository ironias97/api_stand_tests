from contextlib import nullcontext

import data
import sender_stand_request


ssr = sender_stand_request


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def positive_assert(first_name):
    user_body=get_user_body(first_name)
    # print(user_body)
    user_response= ssr.post_new_user(user_body)
    # print(user_response.status_code)
    # print(user_response.json())
    assert user_response.status_code == 201
    assert  user_response.json()['authToken'] != ""

    users_table_response = ssr.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # print(users_table_response.text)
    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    str_error = "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
    user_body = get_user_body(first_name)
    user_response = ssr.post_new_user(user_body)
    # print(user_response.status_code)
    # print(user_response.json()['message'])
    assert int(user_response.status_code) == 400
    assert user_response.json()['message'] == str_error

def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert('Aa')

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert('Aaaaaaaaaaaaaaa')

def test_create_user_1_letter_in_first_name_get_success_response():
    negative_assert_symbol('A')

def test_create_user_16_letter_in_first_name_get_success_response():
    negative_assert_symbol('Aaaaaaaaaaaaaaaa')

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol('Juan luis')

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",");

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol(1234)

def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)

def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)


