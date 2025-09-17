def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name, destination_file_name = parts[1], parts[2]

    if source_file_name == destination_file_name:
        return
    try:
        with (open(source_file_name, "rb") as file_in,
              open(destination_file_name, "wb") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        pass
