**Password Strength Checker API**

This project implements a Password Strength Checker using Python and AWS Lambda. The API assesses the strength of a password based on:

Presence of uppercase, lowercase, numeric, and special characters.
Whether the password contains common words or the user's first or last name.
Length of the password, and other factors.
The API responds with a score and message indicating whether the password is weak, strong, or falls somewhere in between.

Features
Checks for the inclusion of personal information (first/last name) in the password.
Validates password length.
Uses rules to detect common passwords from a list (common.txt).
Provides feedback based on a scoring mechanism to classify passwords into "weak", "fine", "good", and "great".
Setup Instructions
1. AWS Lambda Setup
To replicate this setup, follow these steps to deploy the function as an AWS Lambda service:

**Create a Lambda Function:**

Go to the AWS Lambda Console.
Click Create Function.
Choose Author from scratch.
Set the function name to password-strength-checker.
Select Python 3.x as the runtime environment.
In the execution role, choose Create a new role with basic Lambda permissions.
Click Create Function.
Deploy Code to Lambda:

In the Lambda function code editor, replace the default code with the contents of lambda_function.py from this repository.
You can upload the common.txt file using the Upload button in the Lambda console, or include it in a deployment package.
Click Deploy to save the function.
Set Environment Variables (optional but recommended):

Set environment variables in Lambda for your API (to store values like the common.txt path).
You can do this in the Lambda console by going to the Configuration tab, and adding key-value pairs under Environment Variables.
2. API Gateway Setup
To expose the Lambda function as a REST API:

**Create an API:**

Go to the API Gateway Console.
Click Create API and select REST API.
Configure the API name, description, and endpoint type.
Integrate API with Lambda:

In the Resources tab, click Actions > Create Method and choose POST.
For Integration Type, select Lambda Function.
Specify your Lambda function (password-strength-checker) and save.
Enable CORS (optional):

Select your method (POST), then click Actions > Enable CORS. This allows your API to be called from a web browser.
**Deploy API:**

Go to Stages > Create Stage (e.g., prod).
Once created, deploy the API by selecting Deploy API.
Note the Invoke URL for your API Gateway; this is the endpoint to which you'll send HTTP requests.

Once your API is deployed, you can test the password strength checker by sending a POST request to your API endpoint.

For Example API Request will look like:


**curl -X POST <YOUR_API_URL> \
-H "Content-Type: application/json" \
-d '{"password": "myPassword123!", "first_name": "John", "last_name": "Doe"}'
Replace <YOUR_API_URL> with the actual API Gateway endpoint URL.**

** Response:**

**{
  "status": "good",
  "message": "Your password is good.",
  "score": 5
}**

4. **Local Development**
If you want to run the password strength checker locally for development or testing:

**Clone the repository:
git clone https://github.com/ManasiKarpe/PasswordChecker.git
cd PasswordChecker
Install dependencies:**

pip install -r requirements.txt
Run the function:
You can call the check_password_strength() function directly in Python or integrate it with a local API testing framework like Flask.





Security and Best Practices
1. Do not expose your actual API URL publicly. Instead, use environment variables or placeholders in your documentation to avoid unwanted access.
2. Use API keys or OAuth tokens for authenticated access to the API if required.
3. Consider applying rate limiting and throttling to prevent abuse and protect against DDoS attacks.
