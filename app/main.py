import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return
    source, target = parts[1], parts[2]
    if not os.path.exists(source):
        print(f"Файл {source} не існує")
        return
    if source == target:
        return
    with open(source, "r") as file_in, open(target, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
