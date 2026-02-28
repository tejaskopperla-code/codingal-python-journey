class Dog:

    species = str = "Canine"

    def __init__ (self,breeds,name) :

        self.breeds = breeds
        self.name = name

    def display_details(self):
        print("Desgination : ", self.name ,"Breed : ", self.breeds , "Classfication : ",self.species )


obj_A = Dog (breeds = "German Shepard ", name = "Stevan")
obj_B = Dog(breees = "Husky",name = "Husk")

obj_A.display_details()
obj_B.display_details()