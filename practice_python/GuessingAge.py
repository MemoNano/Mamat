"""
Create a Python script that finds out your age in a maximum of 8 tries! The script can ask you only one type of
question: guessing your age! (e.g. “Are you 67 years old?”) And you can answer only one of these three options:

less
more
correct

Based on your answer the computer can come up with another guess until it finds out your exact age.
"""

answer = ['less', 'more', 'correct']
age = input("Are you 65 years old? ")

if age == 'less':
    age = input("Are you 35 years old?")
    if age == 12:



