# AWS-bedrock

Step 1: Go to AWS management console and open AWS Bedrock service

Step 2: Navigate on the left pane a to the bottom and open "Model acccess". Select the models and save.

Step 3: Navigate to AWS Lambda service.
  - Select "Author from scratch"
  - function name = bedrock-lambda
  - Select runtime as "Python.xx" version
  - Create function

Step 4: Open the lambda function and paste the code which is present in repository.

Step 5: Go to the configuration of lambda function and increase the timeout limit to 3 mins.

Step 6: Add permissions to the assigned role.

Step 7: Open API gateway service and create an API.

Step 8: Create a resource
  - resource path = /
  - resource name = chaatbot

Step 9: Create a method
  - method type = "GET"
  - integration type = Lambda
  - lambda function = bedrock-lambda

Step 10: Go to method request and edit "URL query string parameters" to add the prompt
  - name = prompt
  - Check the "required option"

Step 10: Go to method request and enable request validation.
  - request validator = "Validate query string parameters and headers"

Step 11: Go to integration request and edit the mapping template
  - content type = application/json
  - templete body =
      {
          "prompt" : "$input.params('prompt)"
      }

Step 12: Deploy API to new stage

Step 13: In API gateway service go to "resources", "GET" method and then test the API by providing prompt.
  Example: prompt=Please explain the components in Kubernetes  architecture
