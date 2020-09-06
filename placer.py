#!/usr/bin/env python3

import namebank
import people
import random

students = []
teachers = []

def generateGroup(amt, creator, group):
  while len(group) < amt:
    currentlast = random.choice(namebank.lastnames)
    currentfirst = random.choice(namebank.firstnames)
    newTeacher = creator(currentfirst, currentlast)
    group.append(newTeacher)
    
def assignTeachers():
  for i in range(len(students)):
    students[i].assignTeacher(teachers[i % len(teachers)])
    
def assignDays():
  #group our students by lastname
  studentHash = {}
  for current in students:
    if not current.lastname in studentHash:
      studentHash[current.lastname] = []
    studentHash[current.lastname].append(current)
  sln = list(studentHash)
  #we bucket the lastname with the most going down to the least
  sln.sort(key=lambda s: len(studentHash[s]), reverse=True)
  for currentln in sln:
    teacherList = getTeacherList(studentHash[currentln])
    day = findLowerDay(teacherList)
    for currentStudent in studentHash[currentln]:
      currentStudent.assignDay(day)
        
def getTeacherList(studentList):
  teacherList = []
  for current in studentList:
    if not current.teacher in teacherList:
      teacherList.append(current.teacher)
  return teacherList
  
def findLowerDay(teacherList):
  #current maxes for teachers on day1 and day2
  mday1 = 0
  mday2 = 0
  for currentTeacher in teacherList:
    #get this teacher's counts and set them to the max if greater
    cday1 = sum(1 for y in currentTeacher.students if y.day == 1)
    if cday1 > mday1:
      mday1 = cday1
    cday2 = sum(1 for y in currentTeacher.students if y.day == 2)
    if cday2 > mday2:
      mday2 = cday2
  #now we know the most students any of these teachers have on either day
  #we choose the day with fewer students
  #tie goes to day2
  if mday1 < mday2:
    return 1
  else:
    return 2
      
generateGroup(20, people.Teacher, teachers)
generateGroup(500, people.Student, students)
students.sort(key=lambda student: student.lastname)
assignTeachers()
assignDays()

for currentTeacher in teachers:
  print(currentTeacher)
  currentTeacher.showDay(1)
  currentTeacher.showDay(2)
  
for i in range(1, 3):
  print('Day {}'.format(i))
  daylist = [s for s in students if s.day == i]
  daylist.sort(key=lambda student: student.lastname)
  for currentStudent in daylist:
    print('  {}'.format(currentStudent))