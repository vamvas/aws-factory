# lambda_function.py
import json
import boto3
import joblib
from io import BytesIO

s3 = boto3.client('s3')

def download_model():
    bucket = 'trained-ml-models-repository'
    key = 'models/decision_tree_model.pkl'
    response = s3.get_object(Bucket=bucket, Key=key)
    model_str = response['Body'].read()
    model = joblib.load(BytesIO(model_str))
    return model



def lambda_handler(event, context):
    # body = json.loads(event['body'])
    # input_data = body['input']
    # prediction = model.predict([input_data])
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({'prediction': prediction.tolist()})
    # }
    model = download_model()
    
    return model