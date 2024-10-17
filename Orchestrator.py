# Databricks notebook source
from concurrent.futures import ThreadPoolExecutor
# Define the data
employees = [
    {"id": 101, "name": "Alice", "email": ['alice@example.com', 'alice@example2.com', 'alice@example3.com']},
    {"id": 102, "name": "Bob", "email": ['bob@example.com', 'bob@example2.com', 'bob@example3.com']},
    {"id": 103, "name": "Charlie", "email": ['charlie@example.com', 'charlie@example2.com', 'charlie@example3.com']}
]

# Flatten the list of emails and map them so each can be run as a separate task
email_jobs = [(emp['name'], email) for emp in employees for email in emp['email']]
print(email_jobs)


def submitNotebook(email):
    try:
      dbutils.notebook.run("EmailProcessor", timeout_seconds=200, arguments={"email": email})
    except Exception as e:
      print('exception is ',e)

with ThreadPoolExecutor(max_workers=9) as ec:
    for name, email in email_jobs:
      ec.submit(submitNotebook, email) 
