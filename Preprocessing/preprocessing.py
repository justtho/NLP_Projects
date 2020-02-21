def get_gdelt_file_links():

    import requests
    import lxml.html as lh

    gdelt_base_url = 'http://data.gdeltproject.org/events/'

    # Getting the list of file links from GDELT inorder to download the files 

    page = requests.get(gdelt_base_url+'index.html')
    doc = lh.fromstring(page.content)
    link_list = doc.xpath("//*/ul/li/a/@href")
    # separate out those links that begin with four digits 
    file_list = [x for x in link_list if str.isdigit(x[0:4])]
    
    return file_list
#  get_gdelt_file_links()

    
file_list = get_gdelt_file_links()

# Download files
 
def get_download_files():
    
    infilecounter = 0

    import os.path
    import urllib
    import urllib.request
    import zipfile
    import glob
    import operator

    local_path = 'C:/Sharpest_Minds/projects/NLP_projects/data_files/'

    for compressed_file in file_list[infilecounter:]:
        print( compressed_file),
        
        # storing the compressed file 
        while not os.path.isfile(local_path+compressed_file): 
            print( 'downloading,'),
            urllib.request.urlretrieve(url=gdelt_base_url+compressed_file, 
                            filename=local_path+compressed_file)
            
        # extract the contents of the compressed file to a temporary directory    
        print( 'extracting,'),
        z = zipfile.ZipFile(file=local_path+compressed_file, mode='r')    
        z.extractall(path=local_path+'tmp/')
        
        infilecounter +=1
        print( 'done')

get_download_files()

def extract_source_url():

    import glob
    import pandas as pd
    import os.path
    import urllib
    import urllib.request
    import zipfile
    import operator

    local_path = 'C:/Sharpest_Minds/projects/NLP_projects/data_files/'

    # Get the GDELT field names from a header file
    colnames = pd.read_excel(r'C:\Sharpest_Minds\projects\NLP_projects\data_files\header.xlsx', sheet_name='Sheet1', 
                            index_col=1)['Field Name']

    # Build DataFrames from each of the intermediary files
    files = glob.glob(local_path+'tmp/'+'*')
    DFlist = []
    for active_file in files:
        print( active_file)
        DFlist.append(pd.read_csv(active_file, sep='\t', header=None, dtype=str,
                                names=colnames, index_col=['GLOBALEVENTID']))

    # Merge the file-based dataframes and save a pickle
    df = pd.concat(DFlist)

    df1 = df[['SOURCEURL']]

    urls = df1['SOURCEURL'].unique()

    df1.to_csv('sourceurl_new.csv', header=True, index=None)

extract_source_url()