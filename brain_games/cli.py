#!/usr/bin/env python3
import prompt


def welcome_user():
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


if __name__ == '__main__':
    welcome_user()