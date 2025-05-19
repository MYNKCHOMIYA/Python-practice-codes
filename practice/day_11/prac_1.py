class vector2d:
      def __init__(self,x,y):
            self.x = x
            self.y = y

      def display(self):
            return f"2d vector : ({self.x},{self.y})"
      
class vector3d(vector2d):
      def __init__(self,x,y,z):
       super().__init__(x,y)
       self.z =z

      def display(self):
            return f"3d vector :({self.x},{self.y},{self.z})"
      
vec2d = vector2d(3,4)
vec3d= vector3d(3,4,5)

print(vec2d.display())
print(vec3d.display())