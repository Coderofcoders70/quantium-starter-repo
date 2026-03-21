#!/bin/bash

# 1. Activate the virtual environment
# Note: In a bash environment (like Git Bash or Linux CI), 
# the path uses forward slashes.
source .venv/Scripts/activate

# 2. Execute the test suite
# Pytest will return an exit code: 0 for success, non-zero for failure.
pytest test_app.py

# 3. Capture the exit code of the pytest command
TEST_RESULT=$?

# 4. Return the result
if [ $TEST_RESULT -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed. Please check the logs."
    exit 1
fi