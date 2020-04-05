## AWS Get Secret

A library letting you easily retrieve a secret value from Aws Secrets Manager 

#### Remarks

The project is written by [Deividas Tamkus](https://github.com/deitam), supervised by 
[Laimonas Sutkus](https://github.com/laimonassutkus) and is owned by 
[iDenfy](https://github.com/idenfy). This is an open source
library intended to be used by anyone. [iDenfy](https://github.com/idenfy) aims
to share its knowledge and educate market for better and more secure IT infrastructure.

#### Related technology

This project utilizes the following technology:

- *AWS* (Amazon Web Services).
- *AWS SecretsManager*.

#### Install

The project is built and uploaded to PyPi. Install it by using pip.

```bash
pip install aws-get-secret
```

Or directly install it through source.

```bash
./build.sh -ic
```

### Description

This project allows you to get secret values from Aws Secrets Manager by just knowing secret's ID.

### Examples

To retrieve a secret called `MyCoolSecret` use the following code snippet below.

```python
from aws_get_secret.get_secret import GetSecret

secret_getter = GetSecret()
secret_value = secret_getter.MyCoolSecret

print(f'My super secret is: {secret_value}!')
```
