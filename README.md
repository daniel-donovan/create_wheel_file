# create_wheel_file
A small project to learn how to create a python .whl file

My danstring.py file just reimplements some string manipulation as a proof-of-concept.

There are two batch build files in the repo. Both are designed to be ran in Windows environments:
    'build_whl_using_setuppy.bat' uses a working-but-soon-to-be-deprecated method
        The "wheel" module needs to be installed
    'build_whl_using_build.bat' uses the new build style
        The "wheel" AND "build" modules need to be installed.


A sample execution:
C:\Users\Dan\coding>**dir**
    Directory of C:\Users\Dan\coding
        08/31/2023  05:53 PM             1,163 main.py
        08/31/2023  03:52 PM    <DIR>          python

C:\Users\Dan\coding>**python main.py**
    Traceback (most recent call last):
        File "C:\Users\Dan\coding\main.py", line 4, in <module>
        import danstring
    **ModuleNotFoundError: No module named 'danstring'**

C:\Users\Dan\coding>**pip install python\create_wheel_file\dist\danstring-0.1-py3-none-any.whl**

    Processing c:\users\dan\coding\python\create_wheel_file\dist\danstring-0.1-py3-none-any.whl
    Installing collected packages: danstring
    Successfully installed danstring-0.1

C:\Users\Dan\coding>**python main.py**
    The string "A string of some length" has a length of 23
    The two strings "a partial " and "string" were combined to make "a complete string"
    speaking is speaking but yelling is not YELLING.