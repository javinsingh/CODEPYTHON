class India:
    def capital(self):
        print("my capital is New Delhi")
    def language(self):
        print("my language is Hindi")
    def development(self):
        print("i am a developing country")
class USA:
    def capital(self):
        print("my capital is Washington DC")
    def language(self):
        print("my language is English")
    def development(self):
        print("i am a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_usa, obj_ind):
    country.capital()
    country.language()
    country.development()


