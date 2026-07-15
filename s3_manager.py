
import boto3
import os



def get_s3_client():

    return boto3.client(

        "s3",

        region_name=
        os.getenv(
            "AWS_REGION",
            "us-east-1"
        )

    )



def upload_file(
    filename,
    bucket
):

    s3=get_s3_client()


    s3.upload_file(

        filename,

        bucket,

        filename

    )


    return {

        "message":
        "File uploaded successfully",

        "bucket":
        bucket,

        "file":
        filename

    }
