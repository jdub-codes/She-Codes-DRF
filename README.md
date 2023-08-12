# Pennies for Pawsitivity
by Jenny Waller \
She Codes crowdfunding project - DRF Backend.
## About
Pennies for Pawsitivity is a crowd funding website for
## API Specification
| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |
## Database Schema
{{ Insert your database schema }}
![image info goes here](./docs/image.png)
## Wireframes
{{ Insert your wireframes }}
![image info goes here](./docs/image.png)
## Submission Documentation
{{ Fill this section out for submission }}
Deployed Project: [Deployed website](https://penniespawsitivity.fly.dev/projects/)
### How To Run
{{ What steps to take to run this code }}
### Updated Database Schema
![image info goes here](crowdfunding/img/schema.png)
### Updated Wireframes
![image info goes here](crowdfunding/img/wireframes.png)
### How To Register a New User
* go to Insomnia
* set to "post" request
* use the address "https://penniespawsitivity.fly.dev/users/"
* In the JSON, input data for the new user:
{
    "username":"type username here",
    "password":"type password here",
    "email":"type email address here"
}
* Send request, expected output should be a "200 OK" success message, and preview of new user details.
![image info goes here](img/Create a new user.png)
### Screenshots
* A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](crowdfunding/img/GETrequest.png)
* A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](crowdfunding/img/POSTrequest.png)
* A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](crowdfunding/img/Usertoken.png)