# dinosaurs question

# You will be supplied with two data files in CSV format. The first file contains staticstics about various dinosours. The second file contains additional data.

# Write a program to read in the data files from disk. it must then print the names of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# speed=((STRIDE_LENGTH/LEG_LENGTH)-1)*SQRT(LEG_LENGTH*g)
# Where g = 98m/s^2(gravitational constant)

# dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# TyrannosaurusRex,2.5,carnivore

# dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# TyrannosaurusRex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal