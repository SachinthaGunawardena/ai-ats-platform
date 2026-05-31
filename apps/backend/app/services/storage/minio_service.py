from minio import Minio

client = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "resumes"

found = client.bucket_exists(bucket_name)

if not found:
    client.make_bucket(bucket_name)