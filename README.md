# AWS-Bedrock

AWS Bedrock is a fully managed service by Amazon Web Services (AWS) that makes it easy for developers to build and scale generative AI applications. It provides access to a variety of powerful large language models (LLMs) from leading AI companies, such as Anthropic, Stability AI, Mistral, and Amazon's own models. Bedrock allows users to leverage these models without having to manage the underlying infrastructure or model training themselves.

**Key Features:**

1. Access to Multiple LLMs:
AWS Bedrock provides access to a variety of pre-trained models from different vendors, including those built by Amazon (e.g., Titan models), as well as other companies like Anthropic (e.g., Claude), Stability AI, and Mistral. This allows users to select the best model for their needs (e.g., for natural language processing tasks like text generation, summarization, translation, etc.).

2. Fully Managed Service:
AWS Bedrock takes care of the infrastructure, scaling, and management of AI models, so you don’t need to worry about setting up servers or handling the training process. It handles the operational complexity of deploying and running AI models in production environments.

3. Scalability:
Since it’s part of AWS, Bedrock scales automatically depending on the size and requirements of your application. You can request and generate responses from models without needing to manage the hardware or underlying systems.

4. Integration with AWS Ecosystem:
Bedrock integrates seamlessly with other AWS services like Amazon S3, AWS Lambda, Amazon SageMaker, and more. You can store model outputs in S3, trigger model invocations with Lambda, and perform other operations in the broader AWS ecosystem.

5. Security and Compliance:
Bedrock inherits AWS's robust security and compliance features, such as encryption, identity management with AWS IAM, and more. This makes it suitable for applications that require high levels of data privacy and regulatory compliance.

**Use Cases:**
  - Conversational AI: Build intelligent chatbots and virtual assistants that can carry on natural, human-like conversations.
  - Content Generation: Use LLMs for tasks like text generation, summarization, content creation, etc.
  - Customer Support: Automate responses to customer inquiries or generate recommendations.
  - Data Extraction and Analysis: Use models to analyze text, extract insights, and summarize information.

**Integrating AWS Bedrock with lambda and API gateway**

**Architecture:**

![image](https://github.com/user-attachments/assets/343d3c51-7ceb-4b3d-86ab-5fb0af345020)

  - User Interaction: The user initiates a request via an API call.
  - Amazon API Gateway: Acts as the front-end interface, handling incoming API requests and forwarding them to AWS Lambda.
  - AWS Lambda: A serverless function that processes the request, interacting with other AWS services as needed.
  - AWS Bedrock: Lambda calls AWS Bedrock, which provides foundation models for AI/ML tasks such as text generation, summarization, or other AI-powered functionalities.
  - Amazon S3 (Simple Storage Service): Lambda can also interact with S3 for storing or retrieving data, such as logs, processed outputs, or user inputs.

**Implementation:**

Step 1: Go to AWS management console and open AWS Bedrock service

Step 2: Navigate on the left pane and to the bottom and open "Model access". Select the models and save.

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

Step 11: Go to method request and enable request validation.
  - request validator = "Validate query string parameters and headers"

Step 12: Go to integration request and edit the mapping template
  - content type = application/json
  - templete body =
      {
          "prompt" : "$input.params('prompt')"
      }

Step 13: Deploy API to new stage

Step 14: In API gateway service go to "resources", "GET" method and then test the API by providing prompt.
  Example: prompt=Please explain the components in Kubernetes  architecture
