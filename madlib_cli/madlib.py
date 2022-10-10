import re

path="assets/make_me_a_video_game_template.txt"

### Test the code ##

def read_template(test_path):
    '''
    test_path: str
    return: str
    '''
    with open(test_path) as reader:
        content= reader.read()
        return content
   

def parse_template(content):
    '''
    content: str
    return: tuple[ str , tuple ]
    '''
    
    strip_content=re.sub(r'{[^}]*}','{}', content)
    words=tuple(re.findall('{[^}]*}', content))
    list=[]

    for i in range(len(words)):
        list.append(words[i][1:-1])
    
    keys=tuple(list)

    return(strip_content,keys)


def merge(stripped_text,keys):
    '''
    stripped_text: str
    keys: tuple
    return: str
    '''
    with open("assets/dark_and_stormy_night_ouput.txt", "w") as f:
        final_story=stripped_text.format(*keys)
        f.write(final_story)
        return final_story





def madlib():
    '''
    output: str
    '''
    content=read_template(path)
    parse_template_contant=parse_template(content)
    strip_content=parse_template_contant[0]
    keys=parse_template_contant[1]

    ask=input("Do you want to play?(y/n): ")
    if ask != "y":
        print("Goodbye :)")
    else:
        def welecome_msg():
            '''
            output: str
            '''
            print('''
    ** Welecome to madlib game **
    ** MadLib is a word replacement game **
    ** so you will enter some words and then **
    ** it will be replaced in a paragraph it **
    ** may be funny and you will laugh ... **
    ** just answer the questions and press enter.. **
    ''')

        def insert_data_from_user():
            '''
            return: list
            '''
            list=[]
            for key in keys:
                list.append(input(f"give me {key}: "))
            print("\n")
            return list

        def merge_story(stripped_text,keys):
            '''
            stripped_text: str
            keys: tuple
            return: str
            '''
            with open("assets/make_me_a_video_game_output.txt", "w") as f:
                final_story=stripped_text.format(*keys)
                f.write(final_story)
                return final_story

        welecome_msg()
        stories=merge_story(strip_content,insert_data_from_user())
        print(stories)
madlib()