from github import Github
import pandas as pd

g=Github("28bb6ff892e7dbf8b39fba3000c28bdcc7805083")# access token
repo=g.get_repo('OAID/AutoKernel')
stargazers=repo.get_stargazers_with_dates()
print(len(list(stargazers)))


ret=[]
idx=0
for s in stargazers:
    idx+=1
    if(idx+1)%10==0:
        print(idx)
    info=dict()
    usr= s.user
    info['day']=str(s.starred_at).split()[0]
    info['name']=usr.name
    info['location']=usr.location
    info['company']=usr.company
    info['email']=usr.email
    info['html'] = s.raw_data['user']['html_url']
    info['pub_repos']=usr.public_repos
    info['followers']=usr.followers
    info['followings']=usr.following
    info['blog']=usr.blog
    info['bio']=usr.bio
    ret.append(info)

df = pd.DataFrame(ret)
columns = ['day','name','location','company','email','html','pub_repos','followers','followings','blog','bio']
df.to_csv("autokernel-2020.xlsx",index=False,columns=columns)