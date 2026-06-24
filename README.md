# Calculator API

This is a simple calculator API I built using Python. It handles basic math operations through HTTP endpoints.

## What it does

You can send requests to it and it will add, subtract, multiply or divide two numbers for you. I also added a check so it doesn't crash when you try to divide by zero.

## Endpoints

- `/add` - adds two numbers
- `/subtract` - subtracts two numbers  
- `/multiply` - multiplies two numbers
- `/divide` - divides two numbers (returns an error if you divide by zero)

## How to use

Just pass in `a` and `b` as parameters in the URL, for example:

\`\`\`
GET /add?a=10&b=5
\`\`\`

This will return 15.

## Why I built this

This was a homework project to practice building APIs. I wanted to keep it simple but also handle edge cases like dividing by zero which would normally throw an error.
