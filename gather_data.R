wd <- "~/GitHub/First-Steps-With-Julia"

setwd(wd)

# The following files are provided
#   - train.zip
#   - test.zip
#   - trainResized.zip
#   - testResized.zip
#   - trainLabels.csv
#   - resizeData.py
#   - sampleSubmission.csv
#   - source-code-files.zip

# source("~/GitHub/Get-Raw-Data/download.R")
# downloadKaggle("street-view-getting-started-with-julia","train.zip")
# downloadKaggle("street-view-getting-started-with-julia","test.zip")
# downloadKaggle("street-view-getting-started-with-julia","trainResized.zip")
# downloadKaggle("street-view-getting-started-with-julia","testResized.zip")
# downloadKaggle("street-view-getting-started-with-julia","trainLabels.csv")
# downloadKaggle("street-view-getting-started-with-julia","resizeData.py")
# downloadKaggle("street-view-getting-started-with-julia","sampleSubmission.csv")
# downloadKaggle("street-view-getting-started-with-julia","source-code-files.zip")


## MANUAL STEP - Extract the zip files

trnFile <- "train.csv"
tstFile <- "test.csv"

datalist <- list(
        train=read.csv(
                paste(wd,"\\",trnFile, sep=""), header=TRUE, as.is=TRUE), 
        test=read.csv(
                paste(wd,"\\",tstFile, sep=""), header=TRUE, as.is=TRUE)
        )