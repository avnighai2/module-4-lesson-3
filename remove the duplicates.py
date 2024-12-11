studentData = { 'id1':
    {'name': ['Sara'],
     'class': ['V'],
     'subject interogation':['english, math, science']
    },

'id2':
 {'name': ['David '],
     'class': ['V'],
     'subject interogation':['english, math, science']
    },

'id3':
 {'name': ['Sara'],
     'class': ['V'],
     'subject interogation':['english, math, science']
    },

'id4':
 {'name': ['Surya'],
     'class': ['V'],
     'subject interogation':['english, math, science']
    },
}
result = {}

for key,value in studentData.items():
    if value not in result.values():
        result[key]=value

print(result)