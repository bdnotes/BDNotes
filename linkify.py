import os

def clear_index():
    with open("index.md", "w"):
        pass


def find_all_notes(extensions=('pdf', 'doc', 'txt', 'md', 'png', 'jpg')):
    for root, dirs, files in os.walk("."):
        for file in files:
            full = os.path.join(root, file)
            if full.count("/") >= 2 and file.endswith(extensions) and not full.startswith("./_"):
                yield full[1:]


def write_all_file_links_to_index():
    clear_index()
    with open("index.md", "w") as index:
        index.write("---\nlayout: default\n---\n")
        for file in find_all_notes():
            _, class_, noteName = file.split("/")
            noteName, _ = noteName.split(".")
            index.write("[{0} Notes for {1}]({2})\n\n".format(class_, noteName, file))

print(list(find_all_notes()))
# write_all_file_links_to_index()
