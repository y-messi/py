# wrapping of data ie combining variable and mehtods
# by default the class is public

class encap:
    a = 10
    def dispaly(self):
        print("hello cads")

object = encap()
object.dispaly()    # hello cads
print(object.a)     # 10
        