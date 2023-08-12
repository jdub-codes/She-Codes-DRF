# Pennies for Pawsitivity
This is a DRF backend project for SheCodes by Jenny Waller.

## About
Pennies for Pawsitivity is a crowd funding website for cat charities to raise funds.
## API Specification
| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |
## Database Schema
{{ Insert your database schema }}
![image info goes here](screenshots/)
## Wireframes
{{ Insert your wireframes }}
![image info goes here](screenshots/)
## Submission Documentation
{{ Fill this section out for submission }}
Deployed Project: [Pennies for Pawsitivity](https://penniespawsitivity.fly.dev/projects/)
### How To Run
{{ What steps to take to run this code }}
### How To Register a New User
* go to Insomnia
* set to "post" request
* use the address "https://penniespawsitivity.fly.dev/users/"
* In the JSON, input data for the new user. For example:
{
    "username":"JWaller",
    "password":"1234",
    "email":"jdub.dance@icloud.com"
}
* Send request, expected output should be a "200 OK" success message, and preview of new user details.
![Creat a new user](screenshots/Create_a_new_user.png)
### Screenshots
* A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![Returns all projects](screenshots/Returns_all_projects.png)
* A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![Create a new project](screenshots/Create_a_new_project.png)
* A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](screenshots/Token_return.png)