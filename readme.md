# EMAIL ORGANIZER

## Features

1. **Download** the emails from your gmail inbox.
2. **Filter** the emails based on rules you define in rules.json file.
3. **Mark** the filtered emails as READ/UNREAD.
4. **Move** the messages/emails. 
5. If you are moving email to a label that doesn't exist. Label will get **created** first. Then, email will be moved.


## Folder Structure Details

- auth.py - contains the function that connects to gmail API by calling build method. 
- utils.py - contains function for validating json file containing rule. And, date parsing function.
- fetch_email.py - Main file to download the emails from gmail and parse them. 
- database_helper.py - Has all the database related functions.
- process_emails.py - Reads the rules json, makes required API calls for performing needed action. 
- tests/ - Tests folder contains all the test cases. 
- constants.py - has scope URLs. 

### Sample Rules JSON

```
[
    {
        "select": "all",
        "rules": [{
            "field": "subject",
            "value": "Assignment",
            "condition": "contains"
        }],
        "action": {"command": "mark", "value": "unread"}
    }
]
```
## IMPORTANT NOTE

1. Possible values of key `field` inside rules list - `subject`, `mail_to`,
`mail_from`, `email_received_date`, `body`.
2. Possible values for key `condition` - `contains`, `does not contains`, `equal`, `does not equal` when field is string type.
3. Possible values for key `condition` when field is `email_received_date` - `equal`, `does not equal`, `greater than`, `less than`.    


## STEPS TO RUN THE PROJECT

### Part 1

1. Fetch  OAuth Credentials from console.cloud.google.com. Click on the link
to see step by step how to access [credentials](credentials.md) from google.

2. Clone the repository using command.

```
git clone git@github.com:mridubhatnagar/email_client.git

```

3. Go inside the project repo email_client. 

```
cd email_client
```

4. Create and activate the virtual environment.
`emailclient` is the virtual environment name. You can give any name of your choice.

```
python3 -m venv ~/emailclient
source ~/emailclient/bin/activate
```

5. Once environment is activated. Install all the needed dependencies.
By running the command.

```
pip install -r requirements.txt
```

6. Run the below command. 

```
export ENV=local
```

7. Initialize SQLite database. File `fetch_email.py` accepts `init` as
command line argument. This command will initialize the database. 

```
python fetch_email.py init
```

8. Once the database is created. Run `fetch_email.py` followed by the count of emails you wish to download. 

```
python fetch_email.py 10
```
9. Using any SQLite desktop client. You would be able to verify database and table has got created. And, requested number of emails would have got inserted
in the database. 


### Part 2

1. Update the rules json. In the format as given below.

```
[
    {
        "select": "all",
        "rules": [{
            "field": "subject",
            "value": "Assignment",
            "condition": "contains"
        }],
        "action": {"command": "mark", "value": "unread"}
    }
]
```

2. Run the application.
```
python process_email.py
```
3. `process_email.py` will filter downloaded emails based on the rules. And, perform the requested action.

4. Compare the expected result with the changes that have happened in your gmail.


## STEPS TO RUN TEST CASES

1. Export the correct enviornment

```
export ENV=test
```

2. Run the below command. Go in the project repository.

```
pytest tests\<filename> -s 
```

