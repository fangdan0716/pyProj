import uuid

def get_uuid():
       return uuid.uuid1()
if __name__ == '__main__':
    print(str(get_uuid()))
    print(type(str(get_uuid())))