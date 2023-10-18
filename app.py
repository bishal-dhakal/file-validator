import os

ALLOWED_TYPES = ['docx','doc','txt','jpg','jpeg','pdf','xls','csv','png','gif']
file_name = 'hello.docx'

def test():
    root, ext = os.path.splitext(file_name)
    extension = ext[1:].lower()
    try:
        if extension in ALLOWED_TYPES:
            print('file uploaded')
    except Exception as e:
            raise e
test()
