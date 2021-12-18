library(leaps)
library(MLmetrics)

setwd("~/Documents/Fall-2021/datamining/spotify-project")
spotify_clean <- read.csv("csv/spotify-2000-clean.csv")
spotify_df <- data.frame(spotify_clean)
spotify_tr_df <- spotify_df[1:1200,]
spotify_test_df <- spotify_df[1201:nrow(spotify_df),]

# remove irrelevant (categorical) attributes
spotify_tr_df_valence <-
  subset(spotify_tr_df,
         select = -c(Title, Artist, Year, Popularity, TopGenre))
spotify_test_df <-
  subset(spotify_test_df,
         select = -c(Title, Artist, Year, Popularity, TopGenre))

# multiple linear regression, numeric only - predict valence
# need to verify LINE assumptions and also do cross validation to confirm
# also do variable selection

m1 <- lm(Valence ~ ., data = spotify_tr_df_valence)
print(summary(m1))
plot(m1$res ~ m1$fitted)

# plot residuals vs Xi1 ... Xik
names_clean <- setdiff(names(spotify_tr_df_valence), c("Valence"))
for (colname in names_clean) {
  plot(
    m1$res ~ spotify_tr_df_valence[, colname],
    main = paste("Residuals vs", colname),
    ylab = "Residuals",
    xlab = colname
  )
}

X <-
  spotify_tr_df_valence[,!names(spotify_tr_df_valence) %in% c("Valence")]
y <- spotify_tr_df_valence[, "Valence"]
out <-
  summary(regsubsets(X, y, nbest = 2, nvmax = ncol(X))) # 'nbest' is the number of top models shown for subset size
tab1 <-
  cbind(out$which, out$rsq, out$adjr2, out$cp) # organize the results into a table
print(tab1)
step(m1)

pred1 <- predict.lm(m1, newdata = spotify_test_df, type = "response")

spotify_table_preds <- cbind(spotify_test_df,pred1)

print(MAPE(spotify_table_preds$pred1,spotify_table_preds$Valence))
