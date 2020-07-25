"""Module containing the Settings API. Module uses Annotations. For more info check  PEP-3107 """
# imports go here


class Settings:

    @staticmethod
    def set_account_new_password(user_name: str, account_current_password: str, account_new_password: str,
                                 account_confirm_new_password: str) -> int:
        """
        API method to update the account user password.
        :param user_name: account users' user name.
        :param account_current_password: account users' current password.
        :param account_new_password: account users' new password.
        :param account_confirm_new_password: account user's new password for confirmation.
                                                should be same as account_new_password.
        :return: int: 0 -> OK
                      1 -> Incorrect current password
                      2 -> new password & confirm new password, do not match
                      3 -> both incorrect current password & new passwords do not match.
        """
        flag_correctness = False
        flag_consistency = False
        # Check for current pwd
        stored_hashed_pwd = DatabaseManager.get_database().get_user_hashed_password(user_name)
        if not PasswordHelpers.verify_password(provided_password=account_current_password,
                                               stored_password=stored_hashed_pwd[0]):
            flag_correctness = True
        # Check for consistency of both new passwords
        if account_new_password != account_confirm_new_password:
            flag_consistency = True
        # Check for flags
        if flag_correctness and flag_consistency:
            return 3
        elif flag_correctness:
            return 1
        elif flag_consistency:
            return 2

        user_object = DatabaseManager.get_database().load_user(user_name)
        user_object.password = account_new_password
        DatabaseManager.get_database().modify_user_details(user_object)

        return 0
