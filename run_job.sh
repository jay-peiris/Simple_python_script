#!/bin/bash
# Simple shell script to test shell script file type detection

echo "Running Python job test script..."
echo "Current directory: $(pwd)"
echo "Python version: $(python3 --version)"

# Run the Python script
python3 test_python_job.py output.json

if [ $? -eq 0 ]; then
    echo "Job completed successfully!"
    exit 0
else
    echo "Job failed!"
    exit 1
fi

