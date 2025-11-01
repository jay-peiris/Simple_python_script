# Python Job Test Repository

This is a simple test repository for testing the Python job GitHub sync functionality.

## Files

- `test_python_job.py` - Main Python script that processes data
- `requirements.txt` - Python dependencies (empty for now, standard library only)

## Usage

```bash
# Run the script
python test_python_job.py

# Run with output file
python test_python_job.py output.json
```

## Testing the Sync

1. Create a Python job in the orchestrator
2. Link this GitHub repository to the job
3. Set the `entrypoint` to: `test_python_job.py`
4. Optionally set `github_path` to a subdirectory if your scripts are in a subfolder
5. Click "Sync from GitHub"
6. The files should appear in the job's Files section:
   - `test_python_job.py` → type: `script`
   - `requirements.txt` → type: `requirements`

