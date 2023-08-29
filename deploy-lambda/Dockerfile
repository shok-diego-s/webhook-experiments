FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y gcc musl-dev linux-headers
COPY . ./
RUN pip install -r requirements.txt
CMD ["app.lambda_handler"]