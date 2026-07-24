




room_number ={
    'CS101':1244,
    'CS102':3004,
    'CS103':4501,
    'NT110':6755,
    'CM241':1411
}
course_instructor = {
    'CS101':'Alvarado',
    'CS102':'Haynes',
    'CS103':'Rich',
    'NT110':'Burke',
    'CM241':'Lee'
}

meeting_times ={
     'CS101' :'8:00 a.m.',
     'CS102' : '9:00 a.m.',
      'CS103' :'10:00 a.m.',
      'NT110':'11:00 a.m.',
       'CM241'  :'1:00 p.m'
       
}

course = input("Enter the course number: ")

if course in room_number:
    print(f"Room Number: {room_number[course]}")
    print(f"Instructor: {course_instructor[course]}")
    print(f"Meeting Time: {meeting_times[course]}")
else:
    print("Course not found.")