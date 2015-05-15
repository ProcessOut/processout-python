ProcessOut Python Server
=====================

This module manages invoices for the server-side of an application that uses
the ProcessOut SDK.

ProcessOut makes you able to manage a bunch of payment gateways - such as PayPal,
Crypto currencies, Payza or Dwolla, with no efforts. Learn more on the
[ProcessOut's website](https://www.processout.com).

Dependencies
------------

* Python 2.4 or higher
* requests

Installation
------------

The module's installation is done by a simple git clone

``` sh
git clone https://github.com/ProcessOut/ProcessOut-python-server .
```

-------------------------

Prerequisites
-------------

### Import the module

``` python
from processout.processout import ProcessOut
```

### Instantiate a new ProcessOut instance

``` python
projectId     = '21184268-76fa-4b33-99a0-63fb15f9041a'
projectSecret = 'key-24a2061d0fd2853b75728073d5406de437d525b2ff941fe34ca061cb2180d0f8'

processout = ProcessOut(projectId, projectSecret)
```

Usage
-----

### Create a new invoice from scratch

``` python
invoice = processout.newInvoice(
	'1 copy of a wonderful product at $4.99 USD',
	4.99,
	1,
	'USD'
)
```

##### Available attributes:

- *attribute*  - *example*
- ItemName     - **Amazing product**
- ItemPrice    - **4.20**
- ItemQuantity - **2**
- Currency     - **USD**
- Taxes        - **4.20**
- Shipping     - **4.20**
- Discount     - **10** *Note: percentage, not taken into account in the total price*

### Create a new invoice from a tailored invoice

``` python
invoice = processout.newTailoredInvoice('f7dec519feb3106efa1ee96189a222c3')
```

##### Shared invoice attributes

The following attributes are shared between Invoice and TailoredInvoice instances

- EnableCoupon - *Decide weither or not to accept coupon codes on the invoice*
- ReturnUrl    - *URL to which the customer will be redirected upon purchase*
- CancelUrl    - *URL to which the customer will be redirected upon cancellation*
- NotifyUrl    - *URL being called by ProcessOut to send callbacks upon transaction updates*
- Custom       - *A custom field containing anything you want, sent back within all callbacks*
- Sandbox      - *Decide weither or not to activate the sandbox mode*

#### Attributes getters and setters

Every attributes has its own getter and setter, as such:

``` python
@property
def custom(self):
    return self._custom

@custom.setter
def custom(self, value):
    self._custom = value
```

### Getting the link to an invoice

``` python
print(invoice.getLink())
```

### Receiving callbacks / Web hooks

Callbacks can be used to automate transaction management once a payment has been
placed by one of your customers. One example could be adding credit to an account
once the user has paid his subscription.

However, it doesn't stop there. ProcessOut also supports chargebacks handling,
and much more. Please refer to the
[API documentation](http://docs.processout.apiary.io/#) to learn what data is
sent through callbacks.

Once a callback has been sent to your server, you need to check its authenticity,
as such:

``` python
if not processout.checkCallbackData(data['transaction_id'],
		data['hmac_signature']):
	print('Bad callback')

# Continue normally here, the callback is verified
# One common thing to do would be to check the price, currency, etc...
```

-------------------------

Full API documentation
----------------------

### Apiary

The ProcessOut's full API documentation can be found on
[Apiary](http://docs.processout.apiary.io). It contains all the needed
information, including the callbacks data, and much more.
