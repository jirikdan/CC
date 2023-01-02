from simplegist import Simplegist

ghGist = Simplegist(username='jirikdan', api_token='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')
print(ghGist.profile().listall())
# or provide USERNAME and API_TOKEN in config.py file, so just, ghGist = Gist()
# with all the arguments
ghGist.profile().edit(description='_NEW_DESCRIPTION',name='gistfile1.txt',content='_UPDATED_CONETNT_GOES_HERE')

# with required arguments
#ghGist.profile().edit(id='_GISTID',content='_UPDATED_CONTENT_GOES_HERE')