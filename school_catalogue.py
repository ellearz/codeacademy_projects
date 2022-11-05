class School:
  def __init__(self,name,level,numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents =numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self,new_number):
    self.numberOfStudents = new_number

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

class Primary(School):
  def __init__(self,name,numberOfStudents,pickupPolicy):
    super().__init__(name,"primary",numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getpickupPolicy(self):
    return self.getpickupPolicy

  def __repr__(self):
    var = super().__repr__()
    return var + f" Pickup after {self.pickupPolicy} pm"

class Middle(School):
  pass

class High(School):
  def __init__(self,name,numberOfStudents,sportsTeam):
    super().__init__(name,"high",numberOfStudents)
    self.sportsTeam = sportsTeam
  def getSportsTeams(self):
    return self.sportsTeam

  
