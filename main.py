# def unique_names(names1, names2):
#     a = list(set(names1) & set(names2))
#     b = list(list(set(names1)-set(names2)) + list(set(names2)-set(names1)))
#     c = a + b
#     return c

# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia













# def group_by_owners(files):
#     l = sorted( list( set( files.values() ) ) )
#     d = { author : list( filter( lambda title : files[title] == author, files ) ) for author in l }
#     return d

# if __name__ == "__main__":    
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
#     }   
#     print(group_by_owners(files))

files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    } 


l = sorted( list( set( files.values() ) ) )
d = { author : list( filter( lambda title : files[title] == author, files ) ) for author in l }
print(d)
