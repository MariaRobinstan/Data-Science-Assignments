class UnivariateClass():
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for column in dataset.columns:
            if (dataset[column].dtypes=='object'):
                Qual.append(column)
            else:
                Quan.append(column)
        return Quan,Qual
    