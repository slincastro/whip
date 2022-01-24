import os


class JsonManager:

    def complete_json(self, path):
        backup_file = path + '.bak'

        with open(path, 'r') as read_obj, open(backup_file, 'w') as write_obj:
            write_obj.write("[")

            for line in read_obj:
                write_obj.write(line)

            write_obj.write("{}")
            write_obj.write("]")

        os.remove(path)
        os.rename(backup_file, path)
