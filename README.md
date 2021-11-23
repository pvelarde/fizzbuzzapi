# Fizzbuzz app

## Overview

A Django app that has three enpoints:

- /fizzbuzz (GET/POST)
  * GET returns a list of all entries stored
  * POST returns a new entry created

- /fizzbuzz/## (GET) where ## is an integer
  * GET returns the data of a specified entry

## Building

After cloning repo create a Python virtual environment

> python3 -m venv djangoenv

Activate environment (Linux/Mac)

> source djangoenv/bin/activate

Change directory to fizzbuzzapi/fizzbuzz

> cd fizzbuzzapi/fizzbuzz

Make migrations

> python manage.py makemigrations fizzapi

Migrate

> python manage.py migrate

Runserver

> python manage.py runserver
