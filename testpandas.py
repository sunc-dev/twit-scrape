# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:06:15 2019

@author: csunj
"""


c = twint.Config()
c.Username="CPC_HQ"
c.Hide_output = True
c.Pandas = True
twint.run.Search(c)

df = twint.storage.panda.User_df
twint.storage.panda.clean()
twint.run.Lookup(c)

df = twint.storage.panda.User_df
print(df)