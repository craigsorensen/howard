# Howard Checker
This script checks the Howard Stern website to see if there is a new show posted. If a new show is found, it will send a push notification via pushover.net api.


### Requirements
- Install all requirements as noted in the requirements.txt file.
- Subscription to pushover.net is required for push notifcations

### Setup 
1. Create file called .pushover.txt in the root of your home dir. 
2. Set permissions on .pushover.txt to 600
3. Create new application on pushover.net and get the application token
4. Add your user and application token to the .pushover.txt file as shown below. They should be on two separate lines with no whitespace.

> token:add_app_token_here
>
> user:add_user_key_here

5. The application will use these to authenticate to the pushover service.

