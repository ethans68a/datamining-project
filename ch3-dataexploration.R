install.packages("Hmisc")
library(Hmisc)
test <- c(1,2,3)
save(test,file="testdata")
load(file="./testdata")

names(dframe)
names(dframe)[1] <- "bananas"

write.csv(dframe, "./dummmyData.csv", row.names = FALSE)
install.packages(c("readxl","writexl")) 
library(readxl)
library(writexl)
# write_xlsx()

data(iris)
nrow(iris)
dim(iris)
str(iris)
iris[1:10, "Sepal.Length"]
iris$Sepal.Length[1:10] # same as above line
summary(iris)
describe(iris)

# doesn't make sense to copy function calls from PowerPoint so see https://rutgers.instructure.com/courses/147735/files/19245462?module_item_id=5389543
# density plot is not used very often