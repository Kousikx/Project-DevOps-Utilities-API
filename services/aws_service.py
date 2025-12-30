import boto3
from datetime import datetime, timezone, timedelta

#aware_local_now = datetime.now(timezone.utc).astimezone()


def get_bucket_info():
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets()["Buckets"]
    current_time = datetime.now()
    current_datetime = datetime.now(timezone.utc).astimezone()
    print(current_datetime)

    old_buckets = []
    new_buckets = []

    for buckets in buckets:
        buckets_name = buckets["Name"]
        creation_date = buckets["CreationDate"]
        days_ago_90 = current_datetime - timedelta(days=90) 
        if creation_date < days_ago_90:
            old_buckets.append(buckets_name)
        else:
            new_buckets.append(buckets_name)

    return{
        "total_buckets": len(buckets),
        "new_buckets": len(new_buckets),
        "old_buckets": len(old_buckets),
        "new_buckets_names": new_buckets,
        "old_buckets_names": old_buckets

    }
