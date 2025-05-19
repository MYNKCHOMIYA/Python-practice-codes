class employee:
      def proformance (self,incre,name):
            self.name = name
            proformance = int(input("\nenter the proformance in percentage"))
            self.incre = proformance/100
            return self.incre
class salary(employee):
      def salary(self,performance):
            salary = int(input("enter the salary:"))
            total_salary= salary*(employee.proformance)
            print(f"before increment = {salary},after increment = {total_salary}")
            
emp =salary()

      