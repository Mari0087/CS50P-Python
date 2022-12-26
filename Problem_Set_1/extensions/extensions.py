f = input("file name : ")
f = f.lower().strip()
if ".gif" in f:
    print("image/gif")
elif ".jpg" in f or ".jpeg" in f:
    print("image/jpeg")
elif ".png" in f:
    print("image/png")
elif ".pdf" in f:
    print("application/pdf")
elif ".txt" in f:
    print("text/plain")
elif ".zip" in f :
    print("application/zip")
else:
    print("application/octet-stream")
