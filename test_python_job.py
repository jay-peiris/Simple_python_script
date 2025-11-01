#!/usr/bin/env python3
"""
Simple Python Job Script for Testing GitHub Sync
This script demonstrates a basic data processing job.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def process_data(input_data):
    """
    Simple data processing function.
    
    Args:
        input_data: Dictionary with data to process
        
    Returns:
        Dictionary with processed results
    """
    results = {
        'processed_at': datetime.now().isoformat(),
        'input_count': len(input_data),
        'processed_items': []
    }
    
    for key, value in input_data.items():
        processed_item = {
            'key': key,
            'value': str(value).upper() if isinstance(value, str) else value * 2,
            'type': type(value).__name__
        }
        results['processed_items'].append(processed_item)
    
    return results

def main():
    """Main function to run the job."""
    print("=" * 50)
    print("Python Job Test Script")
    print("=" * 50)
    
    # Example input data
    input_data = {
        'name': 'Test Job',
        'count': 42,
        'status': 'running',
        'timestamp': datetime.now().isoformat()
    }
    
    print(f"\nInput Data:")
    print(json.dumps(input_data, indent=2))
    
    # Process the data
    print("\nProcessing data...")
    results = process_data(input_data)
    
    print(f"\nResults:")
    print(json.dumps(results, indent=2))
    
    # Write output to file if output path provided
    if len(sys.argv) > 1:
        output_path = Path(sys.argv[1])
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults written to: {output_path}")
    else:
        print("\nNo output file specified. Use: python test_python_job.py <output.json>")
    
    print("\n" + "=" * 50)
    print("Job completed successfully!")
    print("=" * 50)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

