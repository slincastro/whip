import subprocess

_LOG_FORMAT = r'{"name": "%aN", "email": "%aE", "date": "%aD"},'


def generate_json(repository_path):
    print(f'Repository path: {repository_path}')
    run_results = subprocess.run(
        [
            "git",
            "--git-dir",
            repository_path + "/.git",
            "log",
            f"--pretty=format:{_LOG_FORMAT}"
        ],
        capture_output=True
    )
    json_str = run_results.stdout.decode()
    return '[' + json_str[:-1] + ']'
