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


