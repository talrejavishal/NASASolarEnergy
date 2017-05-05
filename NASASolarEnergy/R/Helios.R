#reading the data
dataset_solar <- read.csv("Hi-seas_crew_data")


#building the model (Linear Regression)
model <- svm(RADIATION ~ PRESSURE + HUMIDITY + TEMPERATURE + WIND_DIRECTION_DEGREES + 
                WIND_SPEED + TEMPERATURE2 + PRESSURE2,data=dataset_solar_train)

#testing on the model 
prediction <- predict(model,dataset_solar_test)

#calculating the error
error <- dataset_solar_test$RADIATION - prediction

#A function to create RMS error
rmse <- function(error)
{
  sqrt(mean(error^2))
}

#Calculating the RMSE of the model for Linear regression on the test data
LRpredictionrmse <- rmse(error)


