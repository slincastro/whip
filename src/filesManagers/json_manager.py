import os
import subprocess


def complete_json(path):
    backup_file = path + '.bak'

    with open(path, 'r') as read_obj, open(backup_file, 'w') as write_obj:
        write_obj.write("[")

        for line in read_obj:
            write_obj.write(line)

        write_obj.write("{}")
        write_obj.write("]")

    os.remove(path)
    os.rename(backup_file, path)


def generate_json(repository_path, commits_file_path):
    scriptPath = "./scripts/gitLogs.sh"
    subprocess.check_call(scriptPath + " %s %s" % (repository_path, commits_file_path), shell=True)
    complete_json(commits_file_path)
