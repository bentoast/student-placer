#!/usr/bin/env python3

class Student:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.day = 0
    
  def __repr__(self):
    return '{} {}'.format(self.firstname, self.lastname)
    
  def assignTeacher(self, teacher):
    self.teacher = teacher
    self.teacher.assignStudent(self)
    
  def assignDay(self, day):
    self.day = day
    
class Teacher:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.students = []
    
  def __repr__(self):
    return '{} {} ({})'.format(self.firstname, self.lastname, len(self.students))
    
  def assignStudent(self, student):
    self.students.append(student)
    
  def showClass(self):
    for current in self.students:
      print('  {} ({})'.format(current, len(self.students)))
      
  def showDay(self, day):
    daylist = [s for s in self.students if s.day == day]
    print('  Day {} ({}):'.format(day, len(daylist)))
    for current in daylist:
      print('    {}'.format(current))