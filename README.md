# miniodockerize
1.docker-compose up -d (in the directory where yml is)
2.then go to  localhost:9001 and u will see minio console.login with
Username: minio_user
Password: minio_password
3.**Generate Access Tokens:**
Before we get to the code, we must generate an access token from the MinIO console. Head on over to the MinIO Console and navigate to Identity -> Service Accounts -> Create Service Accounts -> Create. You will then see a modal with your Access Key and Secret Key. Write these down, as this is the only time the secret will be displayed.
4.pip3 install minio
5.then after updating your access key and secret key in the code,
run:python3 file_uploader.py
6.similarly run other files to get that services.
7.u will notice the change in minio console Monitoring > Metrics that how many buckets and objects are there .
