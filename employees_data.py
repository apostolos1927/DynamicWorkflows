# Databricks notebook source
employees = [
    {"id": 101, "name": "Alice", "email": ['alice@example.com', 'alice@example2.com', 'alice@example3.com']},
    {"id": 102, "name": "Bob", "email": ['bob@example.com', 'bob@example2.com', 'bob@example3.com']},
    {"id": 103, "name": "Charlie", "email": ['charlie@example.com', 'charlie@example2.com', 'charlie@example3.com']}
]
dbutils.jobs.taskValues.set(key='employees',value=employees)
