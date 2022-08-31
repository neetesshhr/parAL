import sys

sys.stdout = open("filetext.txt", "w", errors="ignore")

sys.stdout.close()

with open("randomfile.txt", "w") as external_file:
    add_text = "This text will be added to the file"
    print(add_text, file=external_file)
    external_file.close()


import contextlib
 
file_path = 'randomfile.txt'
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        print("This text will be added to the file")

x = np.loadtxt("Numbers.txt")
print('Total:', np.sum(x))
print('Average:', np.average(x))
print('Max:', np.amax(x))
print('Min:', np.amin(x))