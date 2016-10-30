setwd("~/GitHub/First-Steps-With-Julia")

dir("test")

files <- dir("testResized")[grep("\\.Bmp", dir("testResized"))]
ids <- as.numeric(gsub("\\.Bmp","",files))
ids <- ids[order(ids)]

summary(ids)
str(ids)

sub <- as.data.frame(ids)
colnames(sub)[1] <- "ID"

sub$Class <- "B"

str(sub)
summary(sub)
head(sub)

write.csv(sub, "bz_sample_submission.csv", row.names = FALSE, quote = FALSE)
