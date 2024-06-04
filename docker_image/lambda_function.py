import json
import boto3
import joblib
from io import BytesIO
# import sklearn

s3 = boto3.client('s3')
def download_model():
    response = s3.get_object(
        Bucket='trained-ml-models-repository',
        Key='models/logistic_model.pkl')

    model_str = response['Body'].read()
    model = joblib.load(BytesIO(model_str))

    return model

model = download_model()

def lambda_handler(event, context):
    body = json.loads(event['body'])
    input_data = body['input']
    prediction = model.predict([input_data])
    
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': prediction.tolist()})
    }