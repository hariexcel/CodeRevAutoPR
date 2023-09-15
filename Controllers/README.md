

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains three files. 
"Billing.py" defines a method for calculating monthly charges. 
"Subscription.py" contains a class for handling subscription upgrades, including authentication. 
"login.py" provides a template for implementing a login functionality.


### `Billing.py`

📝 This file defines a method named `monthlyCharges` that takes a token as a string and returns a float.


### `Subscription.py`

📄 This file contains a class named Subscription.   
🔄 The purpose of this class is to handle subscription upgrades.   
🔒 It requires a session parameter.   
⬆️ The upgradeSubscription method is defined without any implementation.   
🔀 There are two identical definitions of the upgradeSubscription method.   
🔗 The second definition includes a return statement that calls another method.   
📝 The called method is Account.upgrade, which requires authentication.   
🔐 The authentication is done using an Auth.user method with a bearer token.   
🔑 The user ID is obtained from the session parameter.


### `login.py`

📄 This file contains a class called "login"     
🔑 The class has an initializer method that takes a username and password as parameters     
🔒 There is an empty method called "authenticate" for adding authentication logic     
💭 The purpose of this file is to provide a template for implementing a login functionality

<!-- Living README Summary -->