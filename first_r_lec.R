setwd("~/Documents/Fall-2021/datamining")
# random samples from normal distribution
# args: how many you want to choose
# randomly choose numbers from the normal distribution
x <- rnorm(1000)
plot(x)

l <- list(one=1,two=c(1,2))
data <- rnorm(100)
plot(data,type="l",col="gold")

hist(data)

dframe <- data.frame(a=c(3,4,5),b=c(1,2,3),c=c(6,7,8))

write.table(dframe,file="tst0.txt",row.names = F)
j <- c(1,2,NA)
max(j) # NOT AVAILABLE, but you can ignore NA
max(j,na.rm = T)

text <- "apples"
date1 <- strptime(c("20210923000000"),format="%Y%m%d%H%M%S")