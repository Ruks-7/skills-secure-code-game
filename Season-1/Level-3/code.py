# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os

class TaxPayer:

    def safe_path(path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.normpath(os.path.join(base_dir, path))
        if base_dir != os.path.commonpath([base_dir, filepath]):
            return None
        return filepath

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        if not path:
            raise Exception("Error: Profile picture is required for all users")

        # Call safe_path with path as the argument
        safe_path = self.safe_path(path, os.path.dirname(os.path.abspath(__file__)))

        return safe_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):

        if not path:
            raise Exception("Error: Tax form is required for all users")

        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that tax data is returned on screen after this
        return tax_data