# EMAIL CLIENT

## Features

1. **Download** the emails from your gmail inbox.
2. **Filter** the emails based on rules you define in rules.json file.
3. **Mark** the filtered emails as READ/UNREAD.
4. **Move** the messages/emails. 
5. If you are moving email to a label that doesn't exist. Label will get **created** first. Then, email will be moved.

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

## STEPS TO GENERATE CREDENTIALS TO ACCESS GMAIL API

1. To access gmail API. You would need to get access. Login into 
`console.cloud.google.com`. Click on the tab shown in the image below. 

![google cloud console homescreen](/screenshots/homescreen.png)

2. Next screen, you would see would be same as below. Here, follow the arrow.
Click on `create project` option.

![create or select project screen](/screenshots/create_project_1.png)

3. Fill in the details i.e Project Name. And, then click on create app. 
As pointed by the arrow in image.

![fill the create project details form](/screenshots/create_project_2.png)

4. Once project is created. You will be redirected to the homescreen. 
Now, in the right hand side tab. Select name of your newly created project.
Here, `assignment`. Click on enable APIs and services. Follow the arrow.

![click on enable API & Services](/screenshots/api_services_1.png)

5. Click on enable APIs and services. Follow the arrow. Search
for gmail API.

![click on enable API & Services](/screenshots/api_services_2.png)

6. From the result. Select GMAIL API. Click on Enable. 
To enable GMAIL API. From here, you'll be redirected back to API and services screen. 

7. From the left hand side menu. Select Credentials. After selecting credentials. Configure consent screen. Follow the arrow.

![configure consent screen](/screenshots/configure_consent_screen.png)

8. You'll see 2 choice boxes. Select External. Then click on create button.

![configure consent screen](/screenshots/consent_screen_2.png)

9. Next, you'll see app information form. Fill the following fields in the form. 
- App name (Project name and app name can be same)
- User Support Email
- Developer Contact Information

10. After saving the details in previous step. It'll ask you to add or remove
scope. Click on Add or remove scope. And, add the below mentioned URL in the
given table and save.

```
'https://www.googleapis.com/auth/gmail.modify'

```
11. Once all details are saved. Go back to credentials. Click on create credentials. And, select OAuth Client ID. From the dropdown. Select
type of application as dekstop app. 

12. On the next screen it will ask you to give name to the credentials. 
Once done. It will show client ID and client screat key. On the
same screen there is option to download the credentials json. 
Download the file. 

13. Rename the downloaded file to `credentials.json` and move it to 
your project folder i.e `email_client`.



## STEPS TO RUN THE PROJECT

### Part 1

1. Clone the repository using command.

```
git clone git@github.com:mridubhatnagar/email_client.git

```

2. Go inside the project repo email_client. 

```
cd email_client
```

3. Create and activate the virtual environment.
`emailclient` is the virtual environment name. You can give any name of your choice.

```
python3 -m venv ~/emailclient
source ~/emailclient/bin/activate
```

4. Once environment is activated. Install all the needed dependencies.
By running the command.

```
pip install -r requirements.txt
```

5. Initialize SQLite database. File `fetch_email.py` accepts `init` as
command line argument. This command will initialize the database. 

```
python fetch_email.py init
```

6. Once the database is created. Run `fetch_email.py` followed by the count of emails you wish to download. 

```
python fetch_email.py 10
```
7. Using any SQLite desktop client. You would be able to verify database and table has got created. And, requested number of emails would have got inserted
in the database. 


### Part 2

1. Update the rules json. In the format given as example in readme.
2. Run the application.
```
python process_email.py
```
3. `process_email.py` will filter downloaded emails based on the rules. And, perform the requested action.

4. Compare the expected result with the changes that have happened in your gmail.
