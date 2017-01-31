import omdb
import os
import ast

# open file for testing
# os.chdir('')
# file = open('test.doc', 'w') # For Test purpose

# Omit these words from filenames
RESERVED = ['Mastered', 'Extended', 'p', 'AAC', 'UnRated', 'Dual Audio', \
            'Dual', 'Audio', 'EngHindisbaz', '', 'BRRip', 'AACPRiSTiNE', \
            'repack', 'DVD', 'webrip', 'DVDRip', 'DVDSCR', 'Unrated', \
            'BluRay', 'avi', 'XviD', 'HDRip', 'DvDrip', 'Dvdrip', 'BrRip', \
            'mkv', 'Series', 'Trilogy']

def get_filenames():
    files = input('Please enter path of directory: ')
    tmp = []
    try:
        print("Please wait...Working on it!!!")
        for no_of_files, filenames in enumerate(os.listdir(files)):
            # file.write(str(no_of_files) + '.' + ' ' + clean(filenames)+ '\n') # For writing to a file
            # print("%d. %s" %(no_of_files, clean(filenames)))
            tmp.append(clean(filenames))

    except Exception as e:
        error = str(e) + '\n\b' + 'Try Again !!!'
        print(error)
    ## file.close()
    print("Total number of files: %d" % no_of_files)

    # Search omdb database
    try:
        for index in range(len(tmp)):
            movies = omdb.search_movie(tmp[index])
            print(20 * '*')
            print('Search String: ', tmp[index])
            print('Name' + 4 * '\t')
            print(20 * '-')
            try:

                for lists in range(len(movies)):
                    names = movies[lists].title
                    binary_obj = omdb.request(t=names)
                    decode = binary_obj.content.decode()
                    json = ast.literal_eval(decode)
                    if 'imdbRating' in json:
                        print(str(lists + 1) + '.' + ' ' + names + 4* '\t' + json['imdbRating'])
                    else:
                        break
            except Exception as e:
                print('Error: ', e)

        print(20 * '')
    except:
        print('Error. Run program again!!!')
    return tmp

def clean(filename = ''):
    tmp =[]
    emp_str = ''

    for files in filename:
        if files.isalpha():
            emp_str += files
        elif files.isspace() or files == '.':
            tmp.append(emp_str)
            tmp.append(' ')
            emp_str = ''
        else:
            continue

    if ' ' not in emp_str:
        tmp.append(emp_str)
        tmp.append(' ')

    for names in tmp:
        if names.lower() in RESERVED or names.upper() in RESERVED or names in RESERVED:
            tmp.remove(names)
        else:
            continue

    return ''.join(tmp).rstrip(' ').lstrip()

get_filenames()

# print(clean('12 Angry Men 1957 720p')) # Test purposes
