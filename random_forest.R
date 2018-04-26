library(dplyr)
library(randomForest)
library(ggplot2)
datac <- read.csv("output.csv", stringsAsFactors=FALSE)
datac <- filter(datac, TV!='null', Internet!='null', Kitchen!='null', Air_Conditioning!='null', Free_Parking!='null', price!='null', neighbourhood!='null', accommodates!='null', review_scores_rating!='null')
datac$TV <- as.factor(datac$TV)
datac$Internet <- as.factor(datac$Internet)
datac$Kitchen <- as.factor(datac$Kitchen)
datac$Air_Conditioning <- as.factor(datac$Air_Conditioning)
datac$Free_Parking <- as.factor(datac$Free_Parking)
datac$neighbourhood <- as.factor(datac$neighbourhood)
datac$accommodates <- as.factor(datac$accommodates)
datac$price <- as.numeric(datac$price)
datac$review_scores_rating <- as.numeric(datac$review_scores_rating)



#Plot the importance of the features for rating scores
fit <- randomForest(review_scores_rating ~TV+Internet+ Kitchen+ Air_Conditioning+ Free_Parking+ neighbourhood+accommodates, datac, importance = TRUE, ntree = 2000)
importance.features <- tibble::rownames_to_column(data.frame(fit$importance[,c(1)]))
colnames(importance.features) <- c("rowname", "value")

ggplot(importance.features, aes(x = reorder(rowname, -value), y = value)) +
  geom_bar(stat = "identity", position = "dodge", fill="#56B4E9", colour="black") +
  xlab("Factors") + ylab("Count") + ggtitle("Importance of each factor for rating") +
  coord_flip()
#Plot the importance of the features for price
fit1 <- randomForest(price ~TV+Internet+ Kitchen+ Air_Conditioning+ Free_Parking+ neighbourhood+accommodates, datac, importance = TRUE, ntree = 2000)
importance.features <- tibble::rownames_to_column(data.frame(fit1$importance[,c(1)]))
colnames(importance.features) <- c("rowname", "value")

ggplot(importance.features, aes(x = reorder(rowname, -value), y = value)) +
  geom_bar(stat = "identity", position = "dodge", fill="#56B4E9", colour="black") +
  xlab("Amenities") + ylab("Count") + ggtitle("Importance of each factor for price") +
  coord_flip()
