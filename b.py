posting = b"r\n" + b"HTTP/1.1 405 Method Not Allowed"

print(posting)


posting = b"r\n".join([b"HTTP/1.1 405 Method Not Allowed"])

print(posting)