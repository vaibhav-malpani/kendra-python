# Kendra Python
This is a simple flask application that can help you build a web server and connect with Amazon Kendra hosted on AWS.

# Steps to get started with AWS kendra

1. Follow this blog to build you first dataset --> https://medium.com/vaibhav-malpanis-blog/build-your-custom-search-engine-using-machine-learning-amazon-kendra-d7832411c6ad
2. Copy the index_id from AWS console and paste it in kendra.py file.
3. pip install flask flask_cors boto3
4. python run.py

To test the code run the below mentioned curl command:

curl --location --request POST 'localhost:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"query": "<your query>"
}'
