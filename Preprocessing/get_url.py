def get_url():

    import pandas as pd

    df1=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191129.export1.csv')
    df2=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191128.export1.csv')
    df3=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191127.export1.csv')
    df4=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191126.export1.csv')
    df5=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191125.export1.csv')
    df6=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191124.export1.csv')
    df7=pd.read_csv('C:/Sharpest_Minds/projects/NLP_projects/data_files/20191123.export1.csv')

    df7.head()

    df = pd.concat([df1,df2,df3,df4,df5,df6,df7], axis=0)

    df=df.dropna()

    df.head()

    df.shape

    urls = df['sourceurl'].unique()

    df.to_csv('sourceurl.csv', header=True, index=None)
    
    return urls
get_url()
    

