# Python Login System

A simple command-line login system built in Python that uses password hashing and an SQLite database to securely store user credentials. Includes basic user registration, login functionality, and admin access to view registered users.

## Features

- Create user accounts
- Secure password hashing using SHA-256
- SQLite database for storing usernames and hashed passwords
- Admin-only login and user list access
- Duplicate username prevention
- Command-line interface

## Technologies Used

- Python 3
- SQLite (`sqlite3`)
- Hashing with `hashlib`

## Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Running the App

1. Clone the repository:
   ```bash
   git clone https://github.com/samcowette/LoginPractice.git
   cd LoginPractice
