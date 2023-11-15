import traceback

from meal import india
import os, json
path = os.path.dirname(os.path.abspath(india.__file__))
print(path)

list_dir = os.listdir(path)
def dumpException(e):
    print('Exception: %s' % e)
    traceback.print_tb(e.__traceback__)


def getJsonData(file):

    try:

        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        dumpException(e)




list_item = []
for each in list_dir:
    if '.json' in each:
        print(each)
        data = getJsonData(path + '/' + each)


