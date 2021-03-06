import os


def split_file(file_name, no_of_users=1):
    file = open(file_name, 'rb')
    data = file.read()
    file.close()
    print(len(data))
    chunk_size = len(data) // no_of_users

    if len(data) % no_of_users != 0:
        chunk_size += 1

    no_of_chunks = len(data) // chunk_size
    if len(data) % chunk_size != 0:
        no_of_chunks += 1

    print(chunk_size)

    files = [file_name.split('.')[0] + '_' + str(i+1) for i in range(no_of_chunks)]
    for i in range(no_of_users):
        file = open(os.path.join('split', files[i % no_of_chunks]), 'wb')
        file.write(data[:chunk_size])
        file.close()
        data = data[chunk_size:]


if __name__ == "__main__":
    split_file("test_archive.zip", 3)
