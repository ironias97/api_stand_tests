import sender_stand_request
import data
import create_user_test
cut = create_user_test
# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # r=sender_stand_request.get_logs()
    # print(r.status_code)
    # print(r.headers)
    #r=sender_stand_request.get_users_table()
    #r=sender_stand_request.post_new_user(data.user_body)
    # r=sender_stand_request.post_product_kits(data.product_ids)
    # print(r.json())
    # print(r.status_code)
    # create_user_test.test_create_user_2_letter_in_first_name_get_success_response()
    # create_user_test.test_create_user_1_letter_in_first_name_get_success_response()

    cut.test_create_user_2_letter_in_first_name_get_success_response()
    cut.test_create_user_15_letter_in_first_name_get_success_response()
    cut.test_create_user_1_letter_in_first_name_get_success_response()
    cut.test_create_user_16_letter_in_first_name_get_success_response()
    cut.test_create_user_has_space_in_first_name_get_error_response()
    cut.test_create_user_has_special_symbol_in_first_name_get_error_response()
    cut.test_create_user_has_number_in_first_name_get_error_response()
    cut.test_create_user_no_first_name_get_error_response()
    cut.test_create_user_empty_first_name_get_error_response()
    cut.test_create_user_number_type_first_name_get_error_response()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
