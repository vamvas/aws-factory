FROM public.ecr.aws/lambda/python:3.11

COPY lambda_function.py ${LAMBDA_TASK_ROOT}/
COPY requirements.txt ${LAMBDA_TASK_ROOT}/

RUN python3.11 -m pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}/"

CMD ["lambda_function.lambda_handler"]