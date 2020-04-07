import base64
import boto3

from botocore.exceptions import ClientError


class GetSecret:
    def __init__(self):
        self.__client = boto3.client(service_name='secretsmanager')

    def __getattr__(self, item):
        try:
            get_secret_value_response = self.__client.get_secret_value(
                SecretId=item
            )
        except ClientError:
            raise AttributeError(f'The requested secret {item} was not found.')

        # Secrets Manager decrypts the secret value using the associated KMS CMK
        # Depending on whether the secret was a string or binary, only one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            text_secret_data = get_secret_value_response['SecretString']
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']
            text_secret_data = base64.b64decode(binary_secret_data)

        return text_secret_data
