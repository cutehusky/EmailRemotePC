from importlib.util import find_spec
from os import system

packages = ['PIL',
            'pynput',
            'psutil',
            'cv2',
            'customtkinter']

for package in packages:
    if find_spec(package) is None:
        print(f'| {package} is not installed. Installing...')
        if package == 'PIL':
            system('pip install Pillow')
        elif package == 'cv2':
            system('pip install opencv-python')
        else:
            system(f'pip install {package}')
    else:
        print(f'| {package} is installed.')

print('''
----------Setup complete----------
You can proceed to run the program
----------------------------------
''')
