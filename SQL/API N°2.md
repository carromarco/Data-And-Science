![image](https://github.com/carromarco/Data-And-Science/assets/117318209/25f6fc6a-df0c-46de-afc5-24f0e4689b33)

Select HUB_Fisico.IdStock, HUB_Fisico.Descrip, SUM(SAT_Stocks.CantStock)
From HUB_Fisico
Join SAT_Stocks ON HUB_Fisico.IdStock = SAT_Stocks 
