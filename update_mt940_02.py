import sys

# Mapping defined in the following dictionary. 
# Any new conversions should be added in the following dictionary

replaceLetter = {'____': '',
                 '_': '',
                 '#': ' ',
                 '&': ' ',
                 '*': ' ',
                 ';': ' ',
                 '$': 'D',
                 'RE:': 'REF',
                 ':25:220137031': ':25:AE640211000000220137031',
                 ':25:220137058': ':25:AE140211000000220137058',
                 ':25:220137007': ':25:AE330211000000220137007',
                 ':25:220183009': ':25:AE640211000000220183009',
                 ':25:202239005': ':25:AE410211000000202239005'}


# Function for replacing the text mentioned in the above dictionary

def replaceText(replaceLetter, filedata):
    newdata = filedata
    for i in replaceLetter.items():
        newdata = newdata.replace(i[0], i[1])
    return (newdata)


# Reading the file for conversion

f = open(str(sys.argv[1]), 'r')
filedata = f.read()
f.close()

finalData = replaceText(replaceLetter, filedata)

# Writing a file after conversion

newFileName = '.'.join(
    [str(sys.argv[1]).split('.')[0], 'mt940'])  # removing txt extension and adding mt940 extension to new file name
f = open(newFileName, 'w+')
f.write(finalData)
f.close()

print('\nThis is a program to format the MT940 files')
print('*****************************************************')
print('Formatting file : ' + str(sys.argv[1]))
print('New file : ' + newFileName)
print('*****************************************************')
