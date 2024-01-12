
import argparse
import os
import yaml


class Config:
    def __init__(self):
        self.secret_key = None
        self.min_email_length = None
        self.min_password_length = None
        self.min_name_length = None

        self.configure_from_command_line()
        self.configure_from_environment()
        self.configure_from_yaml()

    def configure_from_command_line(self):
        parser = argparse.ArgumentParser(description='Application Configuration')
        parser.add_argument('--secret_key', type=str, help='Secret Key')
        parser.add_argument('--min_email_length', type=int, help='Minimum Email Length')
        parser.add_argument('--min_password_length', type=int, help='Minimum Password Length')
        parser.add_argument('--min_name_length', type=int, help='Minimum Name Length')

        args = parser.parse_args()

        self.secret_key = args.secret_key
        self.min_email_length = args.min_email_length
        self.min_password_length = args.min_password_length
        self.min_name_length = args.min_name_length

    def configure_from_environment(self):
        self.secret_key = os.environ.get('SECRET_KEY', self.secret_key)

        min_email_length = os.environ.get('MIN_EMAIL_LENGTH')
        self.min_email_length = int(min_email_length) if min_email_length is not None else self.min_email_length

        min_password_length = os.environ.get('MIN_PASSWORD_LENGTH')
        self.min_password_length = int(
            min_password_length) if min_password_length is not None else self.min_password_length

        min_name_length = os.environ.get('MIN_NAME_LENGTH')
        self.min_name_length = int(min_name_length) if min_name_length is not None else self.min_name_length

    def configure_from_yaml(self):
        try:
            with open('config.yaml', 'r') as file:
                yaml_data = yaml.safe_load(file)

                if yaml_data:
                    print("Loaded YAML data:", yaml_data)

                    self.secret_key = yaml_data.get('SECRET_KEY', self.secret_key)
                    self.min_email_length = yaml_data.get('MIN_EMAIL_LENGTH', self.min_email_length)
                    self.min_password_length = yaml_data.get('MIN_PASSWORD_LENGTH', self.min_password_length)
                    self.min_name_length = yaml_data.get('MIN_NAME_LENGTH', self.min_name_length)
        except FileNotFoundError:
            pass

config_instance = Config()