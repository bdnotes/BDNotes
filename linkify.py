import os
extensions=('pdf', 'doc', 'txt', 'md', 'png', 'jpg')
def clear_index():
    with open("index.md", "w"):
        pass


def find_all_notes():
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

def write_accordioning():
    with open("_includes/accordions.html", "w") as index:
        index.write("""
 <script>
      $(function() {
        $( ".accordion" ).accordion({
          collapsible: true,
          active: false
        });
      });
    </script>""")
        for root, dirs, files in os.walk("."):
            for dir_ in dirs:
                full = os.path.join(root, dir_)
                if not full.startswith(("./.", "./_")) and dir_ != 'sass' and full.count("/") < 2:
                    print(dir_, full)
                    tag = '<div class="accordion"><h3>{0}</h3><ul>'.format(dir_)
                    for root2, subdirs, subfiles in os.walk(dir_):
                        for file in subfiles:
                            full = os.path.join(root2, file)
                            _, class_, name = full.split("/")
                            for_, _ = name.split(".")
                            print(full)
                            tag += '<li><a href="/BDNotes/{0}" class="accordion-inner">{1} notes for {2}</a></li>'.format(full, class_, for_)
                    tag += '</ul></div>'
                    index.write(tag + "\n")
write_accordioning()                  
# write_all_file_links_to_index()
