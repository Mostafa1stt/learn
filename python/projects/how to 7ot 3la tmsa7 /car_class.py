class Outer:
  def __init__(self,age):
    self.name = "Emil"
    self.age = age

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.age} {self.outer.name}")

outer = Outer(45)
inner = outer.Inner(outer)
inner.display() 
