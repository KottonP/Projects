# Title     : Data Analysis 1Lab
# Objective : R intro and Descriptive Statistics
# Created by: PanosVamv
# Created on: 16/4/2020

H <- read.table('http://www.math.ntua.gr/~fouskakis/hours.txt',
                header=TRUE, na.strings='1000', stringsAsFactors=FALSE) # Data insertion

print(class(H)) # Type of H
H <- subset(H, select = -id) # Removal of id column
H <- transform(H, season=factor(season), sex=factor(sex)) # Transform season and sex column to categorical
levels(H$sex) <- c("Male", "Female") # Assign Male -> 0 & Female -> 1 , for the "sex" column


# 4th Question
s <- summary(H$hobbies)  # List containing the central tendencies of the "hobbies" column
q <- c(s[2], s[3], s[5]) # Vector containing the quartile bounds q1,q2,q3
n <- length(H$hobbies)
hobbielist <- H$hobbies
h4 <- numeric(n)

for (i in 1:n)
  if (hobbielist[i] < q[1]) {
    h4[i] <- 1
  } else if (hobbielist[i] > q[1] & hobbielist[i] < q[2]) {
    h4[i] <- 2
  } else if (hobbielist[i] > q[2] & hobbielist[i] < q[3]) {
    h4[i] <- 3
  } else {
    h4[i] <- 4
  }

contable <- table(h4, H$age)  # The contingency table of the new hobbie variable and age