
with open("textfile_file_i_o_1.txt") as f:
    content = f.read()

content = content.replace("donkey", "@@@@@@@@@@")

with open("textfile_file_i_o_1.txt","w") as f:
    f.write(content)