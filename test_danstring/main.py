# move this file outside of the create_wheel_file directory and run it directly from the command line
# after installing the danstring-0.1-py3-none-any.whl file with pip install

import danstring

testString = 'A string of some length'
testStringLength = danstring.ds_length(testString)
print(f'The string \"{testString}\" has a length of {testStringLength}')
testString = testStringLength = None

testString1 = 'a partial '
testString2 = 'string'
wrongWord = 'partial'
rightWord = 'complete'
outputString = danstring.ds_concat(testString1, testString2)
outputString = danstring.ds_replace(outputString, wrongWord, rightWord)
print(f'The two strings \"{testString1}\" and \"{testString2}\" were combined to make \"{outputString}\"')
testString1 = testString2 = wrongWord = rightWord = outputString = None

ts1 = ts2 = 'speaking'
firstEqualTest = danstring.ds_compare(ts1, ts1)
ts3 = 'yelling'
ts4 = danstring.ds_upper(ts3)
secondEqualTest = danstring.ds_compare(ts3, ts4)

if firstEqualTest and not secondEqualTest:
    print(f'{ts1} is {ts2} but {ts3} is not {ts4}.')

ts1 = ts2 = ts3 = ts4 = firstEqualTest = secondEqualTest = None
