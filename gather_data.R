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

source("~/GitHub/Get-Raw-Data/download.R")
downloadMultKaggleZip("street-view-getting-started-with-julia","train.zip")
downloadMultKaggleZip("street-view-getting-started-with-julia","test.zip")
downloadMultKaggleZip("street-view-getting-started-with-julia","trainResized.zip")
downloadMultKaggleZip("street-view-getting-started-with-julia","testResized.zip")
downloadKaggle("street-view-getting-started-with-julia","trainLabels.csv")
downloadKaggle("street-view-getting-started-with-julia","resizeData.py")
downloadKaggle("street-view-getting-started-with-julia","sampleSubmission.csv")
downloadMultKaggleZip("street-view-getting-started-with-julia","source-code-files.zip","/sourcecodefiles")

datalist <- list(
        train=read.csv(
                paste(wd,"\\",trnFile, sep=""), header=TRUE, as.is=TRUE), 
        test=read.csv(
                paste(wd,"\\",tstFile, sep=""), header=TRUE, as.is=TRUE)
        )