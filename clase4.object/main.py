class persona:

      def __init__(self, p_name, id):
            print('hi def init')
            self.m_name = p_name
            self.id = id


      def sing(self):
            print(self.m_name + ' is singin')

      def show_id(self):
            return (str(self.id)) + ' es mi edad'

p1 = persona('oliver', 55433)
p2 = persona('alvaro', 77343)

print(p1.m_name)
print(p1.id)

p1.sing()
print(p1.show_id())
print(p2.show_id())